from typing import Optional
from pydantic import BaseModel


class SupplierBase(BaseModel):
    name: str
    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class SupplierCreate(SupplierBase):
    pass


class SupplierRead(SupplierBase):
    id: int

    class Config:
        from_attributes = True
