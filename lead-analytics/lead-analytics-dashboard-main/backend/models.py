from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime


# ---------------------------
# Lead Model (existing)
# ---------------------------
class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    agent_name = Column(String)
    source = Column(String)
    status = Column(String)
    revenue = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "agent_name": self.agent_name,
            "source": self.source,
            "status": self.status,
            "revenue": self.revenue,
            "created_at": str(self.created_at)
        }


# ---------------------------
# Agent Model (NEW)
# ---------------------------
class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


# ---------------------------
# Lead History Model (NEW)
# ---------------------------
class LeadHistory(Base):
    __tablename__ = "lead_history"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer)
    old_status = Column(String)
    new_status = Column(String)
    changed_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "lead_id": self.lead_id,
            "old_status": self.old_status,
            "new_status": self.new_status,
            "changed_at": str(self.changed_at)
        }