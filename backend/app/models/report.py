from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    report_type = Column(String(100), nullable=False)
    summary = Column(String(2000), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
