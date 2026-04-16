from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Lead

router = APIRouter()


@router.get("/analytics")
def get_analytics(db: Session = Depends(get_db)):
    """Get analytics metrics for the dashboard."""

    all_leads = db.query(Lead).all()

    total_leads = len(all_leads)

    converted = 0
    for lead in all_leads:
        if lead.status == "Converted":
            converted += 1

    conversion_rate = (converted / total_leads * 100) if total_leads > 0 else 0

    # Calculate estimated revenue based on average deal size
    total_revenue = total_leads * 100

    return {
        "total_leads": total_leads,
        "conversion_rate": round(conversion_rate, 2),
        "total_revenue": total_revenue,
    }


@router.get("/analytics/leads-by-source")
def leads_by_source(db: Session = Depends(get_db)):
    """Get lead count grouped by source."""

    all_leads = db.query(Lead).all()

    source_counts = {}
    for lead in all_leads:
        source = lead.source
        if source in source_counts:
            source_counts[source] += 1
        else:
            source_counts[source] = 1

    return source_counts


@router.get("/analytics/top-agents")
def top_agents(db: Session = Depends(get_db)):
    """Get top performing agents by number of converted leads."""

    all_leads = db.query(Lead).all()

    agent_stats = {}
    for lead in all_leads:
        agent = lead.agent_name
        if agent not in agent_stats:
            agent_stats[agent] = {"total": 0, "converted": 0, "revenue": 0}

        agent_stats[agent]["total"] += 1
        if lead.status == "Converted":
            agent_stats[agent]["converted"] += 1
            agent_stats[agent]["revenue"] += lead.revenue

    sorted_agents = sorted(agent_stats.items(), key=lambda x: x[1]["converted"], reverse=True)

    result = []
    for agent_name, stats in sorted_agents[:5]:
        result.append({
            "agent_name": agent_name,
            "total_leads": stats["total"],
            "converted": stats["converted"],
            "revenue": stats["revenue"]
        })

    return result


@router.get("/leads")
def get_leads(db: Session = Depends(get_db)):
    """Fetch all leads."""

    leads = db.query(Lead).all()
    return [lead.to_dict() for lead in leads]
