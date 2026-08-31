from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from app.database import Base


class GoodsReceiving(Base):
    __tablename__ = "goods_receiving"

    id = Column(Integer, primary_key=True, index=True)
    grn_number = Column(String(100), unique=True, nullable=False, index=True)  # Goods Receipt Number
    po_number = Column(String(100), nullable=False)  # Purchase Order reference
    supplier_name = Column(String(255), nullable=False)
    material_name = Column(String(255), nullable=False)
    batch_number = Column(String(100), nullable=True)
    ordered_quantity = Column(Float, nullable=False)
    received_quantity = Column(Float, nullable=False)
    unit = Column(String(50), nullable=False)
    receiving_date = Column(DateTime, default=datetime.utcnow)
    received_by = Column(String(255), nullable=True)
    warehouse_location = Column(String(255), nullable=True)
    invoice_number = Column(String(100), nullable=True)
    invoice_date = Column(DateTime, nullable=True)
    remarks = Column(Text, nullable=True)
    transport_details = Column(String(500), nullable=True)
    damage_or_short = Column(Text, nullable=True)
    receiving_status = Column(String(50), default="Received")  # Received, Pending QC, QC Approved, Rejected
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
