from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base


class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(String(100), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    unit = Column(String(50), nullable=False)
    quantity = Column(Float, default=0.0)
    reserved_quantity = Column(Float, default=0.0)  # Reserved for active projects
    unit_price = Column(Float, default=0.0)  # Valuation price per unit
    minimum_stock = Column(Float, default=0.0)
    reorder_level = Column(Float, default=0.0)
    storage_location = Column(String(255), nullable=True)
    supplier = Column(String(255), nullable=True)
    status = Column(String(50), default="Active")
    specifications = Column(Text, nullable=True)  # Product specifications
    storage_rules = Column(Text, nullable=True)  # Special storage instructions
    created_at = Column(DateTime(timezone=True), server_default=func.now())
