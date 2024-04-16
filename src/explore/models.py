from sqlalchemy import Column, Enum, String, DateTime, JSON
from datetime import datetime

from src.explore.database import Base


class LLMRequest(Base):
    __tablename__ = "llm_requests"
    id = Column(String, primary_key=True, index=True)
    initiated = Column(DateTime, default=datetime.utcnow)
    input = Column(String, nullable=False)
    response_shape = Column(JSON, nullable=False)
    llm_type = Column(String, default="gpt-3.5")

