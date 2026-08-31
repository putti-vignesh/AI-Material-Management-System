from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base


class PurchaseRequest(Base):
    __tablename__ = "purchase_requests"

    id = Column(Integer, primary_key=True, index=True)
    request_number = Column(String(100), unique=True, nullable=False)
    material_name = Column(String(255), nullable=False)
    quantity = Column(Float, default=0.0)
    supplier = Column(String(255), nullable=True)
    priority = Column(String(50), default="Medium")
    urgency = Column(String(50), default="Normal")  # Critical, High, Normal, Low
    project_reference = Column(String(255), nullable=True)  # Project name or ID
    status = Column(String(50), default="Pending")
    requested_by = Column(String(100), nullable=True)
    remarks = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
