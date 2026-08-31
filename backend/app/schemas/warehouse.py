from typing import Optional
from pydantic import BaseModel


class WarehouseBase(BaseModel):
    name: str
    location: Optional[str] = None
    capacity: float
    manager: Optional[str] = None


class WarehouseCreate(WarehouseBase):
    pass


class WarehouseRead(WarehouseBase):
    id: int

    class Config:
        from_attributes = True
