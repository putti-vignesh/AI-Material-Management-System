from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class QualityInspection(Base):
    __tablename__ = "quality_inspections"

    id = Column(Integer, primary_key=True, index=True)
    grn_number = Column(String(100), unique=True, nullable=False, index=True)  # Goods Receipt Number
    purchase_request_id = Column(String(100), nullable=False)
    material_name = Column(String(255), nullable=False)
    ordered_quantity = Column(Float, nullable=False)
    received_quantity = Column(Float, nullable=False)
    accepted_quantity = Column(Float, nullable=False, default=0)
    rejected_quantity = Column(Float, nullable=False, default=0)
    batch_number = Column(String(100), nullable=True)
    inspection_date = Column(DateTime, default=datetime.utcnow)
    inspector_name = Column(String(255), nullable=True)
    inspection_remarks = Column(Text, nullable=True)
    defects_found = Column(Text, nullable=True)
    quality_status = Column(String(50), default="Pending")  # Pending, Approved, Rejected, Partial
    warehouse_location = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
