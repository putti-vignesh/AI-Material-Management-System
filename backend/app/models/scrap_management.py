from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from app.database import Base


class ScrapManagement(Base):
    __tablename__ = "scrap_records"

    id = Column(Integer, primary_key=True, index=True)
    scrap_number = Column(String(100), unique=True, nullable=False, index=True)
    material_name = Column(String(255), nullable=False)
    quantity = Column(Float, nullable=False)
    reason = Column(String(255), nullable=False)  # Damaged, Expired, Excess Wastage
    warehouse_name = Column(String(255), nullable=True)
    disposal_status = Column(String(50), default="Pending")  # Pending, Disposed, Recycled
    estimated_scrap_value = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
