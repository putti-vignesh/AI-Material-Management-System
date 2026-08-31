from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from app.database import Base


class MaterialReturn(Base):
    __tablename__ = "material_returns"

    id = Column(Integer, primary_key=True, index=True)
    return_number = Column(String(100), unique=True, nullable=False, index=True)
    material_name = Column(String(255), nullable=False)
    supplier_name = Column(String(255), nullable=False)
    quantity = Column(Float, nullable=False)
    reason = Column(String(255), nullable=False)  # Quality Defect, Surplus, Wrong Item
    status = Column(String(50), default="Returned")  # Initiated, Returned, Refunded
    return_date = Column(DateTime, default=datetime.utcnow)
