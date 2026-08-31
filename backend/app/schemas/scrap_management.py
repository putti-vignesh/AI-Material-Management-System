from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ScrapManagementBase(BaseModel):
    scrap_number: str
    material_name: str
    quantity: float
    reason: str
    warehouse_name: Optional[str] = None
    disposal_status: str = "Pending"
    estimated_scrap_value: float = 0.0


class ScrapManagementCreate(ScrapManagementBase):
    pass


class ScrapManagementRead(ScrapManagementBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
