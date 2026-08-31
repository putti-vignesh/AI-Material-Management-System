from typing import Optional
from pydantic import BaseModel


class MaterialBase(BaseModel):
    material_id: str
    name: str
    category: str
    unit: str
    quantity: float
    minimum_stock: float
    reorder_level: float
    storage_location: Optional[str] = None
    supplier: Optional[str] = None
    status: str = "Active"
    specifications: Optional[str] = None
    storage_rules: Optional[str] = None


class MaterialCreate(MaterialBase):
    pass


class MaterialRead(MaterialBase):
    id: int

    class Config:
        from_attributes = True
