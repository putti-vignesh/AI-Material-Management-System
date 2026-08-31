from typing import Optional
from pydantic import BaseModel


class PurchaseRequestBase(BaseModel):
    request_number: str
    material_name: str
    quantity: float
    supplier: Optional[str] = None
    priority: str = "Medium"
    urgency: str = "Normal"
    project_reference: Optional[str] = None
    status: str = "Pending"
    requested_by: Optional[str] = None
    remarks: Optional[str] = None


class PurchaseRequestCreate(PurchaseRequestBase):
    pass


class PurchaseRequestRead(PurchaseRequestBase):
    id: int

    class Config:
        from_attributes = True
