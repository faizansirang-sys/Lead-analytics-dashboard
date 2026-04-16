from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Lead, Agent, LeadHistory

router = APIRouter()


# -----------------------------
# Create Agent
# -----------------------------
@router.post("/create-agent")
def create_agent(name: str, db: Session = Depends(get_db)):

    agent = Agent(name=name)
    db.add(agent)
    db.commit()
    db.refresh(agent)

    return {
        "message": "Agent created",
        "agent_id": agent.id,
        "name": agent.name
    }


# -----------------------------
# Incoming Lead (Assignment Engine)
# -----------------------------
@router.post("/api/leads/incoming")
def incoming_lead(source: str, revenue: float, db: Session = Depends(get_db)):

    agents = db.query(Agent).all()

    if not agents:
        return {"error": "No agents available"}

    selected_agent = None
    min_leads = 999

    # Find agent with fewest open leads
    for agent in agents:

        open_leads = db.query(Lead).filter(
            Lead.agent_name == agent.name,
            Lead.status != "Closed"
        ).count()

        if open_leads < min_leads and open_leads < 10:
            min_leads = open_leads
            selected_agent = agent

    if not selected_agent:
        return {"error": "All agents at maximum capacity"}

    lead = Lead(
        agent_name=selected_agent.name,
        source=source,
        status="New",
        revenue=revenue
    )

    db.add(lead)
    db.commit()
    db.refresh(lead)

    return {
        "message": "Lead created and assigned",
        "lead_id": lead.id,
        "assigned_agent": selected_agent.name
    }


# -----------------------------
# Agent Workload Endpoint
# -----------------------------
@router.get("/api/agents/workload")
def agent_workload(db: Session = Depends(get_db)):

    agents = db.query(Agent).all()

    result = []

    for agent in agents:

        open_leads = db.query(Lead).filter(
            Lead.agent_name == agent.name,
            Lead.status != "Closed"
        ).count()

        result.append({
            "agent_name": agent.name,
            "open_leads": open_leads
        })

    return result


# -----------------------------
# Update Lead Status
# -----------------------------
@router.patch("/api/leads/{lead_id}/status")
def update_lead_status(lead_id: int, status: str, db: Session = Depends(get_db)):

    lead = db.query(Lead).filter(Lead.id == lead_id).first()

    if not lead:
        return {"error": "Lead not found"}

    old_status = lead.status
    lead.status = status

    # Save status change history
    history = LeadHistory(
        lead_id=lead.id,
        old_status=old_status,
        new_status=status
    )

    db.add(history)

    # If lead rejected → reassign
    if status == "Rejected":

        agents = db.query(Agent).all()

        for agent in agents:

            open_leads = db.query(Lead).filter(
                Lead.agent_name == agent.name,
                Lead.status != "Closed"
            ).count()

            if open_leads < 10:
                lead.agent_name = agent.name
                break

    db.commit()

    return {
        "message": "Lead status updated",
        "lead_id": lead.id,
        "new_status": status
    }