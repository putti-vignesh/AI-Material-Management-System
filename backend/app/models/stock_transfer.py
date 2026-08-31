from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from app.database import Base


class StockTransfer(Base):
    __tablename__ = "stock_transfers"

    id = Column(Integer, primary_key=True, index=True)
    transfer_number = Column(String(100), unique=True, nullable=False, index=True)
    material_name = Column(String(255), nullable=False)
    source_warehouse = Column(String(255), nullable=False)
    destination_warehouse = Column(String(255), nullable=False)
    quantity = Column(Float, nullable=False)
    status = Column(String(50), default="Completed")  # Pending, In-Transit, Completed
    remarks = Column(Text, nullable=True)
    transfer_date = Column(DateTime, default=datetime.utcnow)
