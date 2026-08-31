from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PurchaseOrderBase(BaseModel):
    po_number: str
    request_number: Optional[str] = None
    supplier_name: str
    material_name: str
    quantity: float
    unit_price: float = 0.0
    total_amount: float = 0.0
    expected_delivery_date: Optional[datetime] = None
    status: str = "Issued"


class PurchaseOrderCreate(PurchaseOrderBase):
    pass


class PurchaseOrderRead(PurchaseOrderBase):
    id: int
    order_date: datetime
    created_at: datetime

    class Config:
        from_attributes = True
