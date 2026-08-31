from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.database import Base


class InventoryTransaction(Base):
    __tablename__ = "inventory_transactions"

    id = Column(Integer, primary_key=True, index=True)
    material_name = Column(String(255), nullable=False)
    transaction_type = Column(String(50), nullable=False)
    quantity = Column(Float, default=0.0)
    reference = Column(String(255), nullable=True)
    remarks = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
