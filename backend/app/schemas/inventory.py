from typing import Optional
from pydantic import BaseModel


class InventoryTransactionBase(BaseModel):
    material_name: str
    transaction_type: str
    quantity: float
    reference: Optional[str] = None
    remarks: Optional[str] = None


class InventoryTransactionCreate(InventoryTransactionBase):
    pass


class InventoryTransactionRead(InventoryTransactionBase):
    id: int

    class Config:
        from_attributes = True
