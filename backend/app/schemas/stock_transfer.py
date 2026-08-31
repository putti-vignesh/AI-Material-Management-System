from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class StockTransferBase(BaseModel):
    transfer_number: str
    material_name: str
    source_warehouse: str
    destination_warehouse: str
    quantity: float
    status: str = "Completed"
    remarks: Optional[str] = None


class StockTransferCreate(StockTransferBase):
    pass


class StockTransferRead(StockTransferBase):
    id: int
    transfer_date: datetime

    class Config:
        from_attributes = True
