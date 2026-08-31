from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MaterialReturnBase(BaseModel):
    return_number: str
    material_name: str
    supplier_name: str
    quantity: float
    reason: str
    status: str = "Returned"


class MaterialReturnCreate(MaterialReturnBase):
    pass


class MaterialReturnRead(MaterialReturnBase):
    id: int
    return_date: datetime

    class Config:
        from_attributes = True
