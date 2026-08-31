from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class QualityInspectionBase(BaseModel):
    grn_number: str
    purchase_request_id: str
    material_name: str
    ordered_quantity: float
    received_quantity: float
    accepted_quantity: float = 0
    rejected_quantity: float = 0
    batch_number: Optional[str] = None
    inspector_name: Optional[str] = None
    inspection_remarks: Optional[str] = None
    defects_found: Optional[str] = None
    quality_status: str = "Pending"
    warehouse_location: Optional[str] = None


class QualityInspectionCreate(QualityInspectionBase):
    pass


class QualityInspectionRead(QualityInspectionBase):
    id: int
    inspection_date: datetime
    created_at: datetime

    class Config:
        from_attributes = True


class GoodsReceivingBase(BaseModel):
    grn_number: str
    po_number: str
    supplier_name: str
    material_name: str
    batch_number: Optional[str] = None
    ordered_quantity: float
    received_quantity: float
    unit: str
    received_by: Optional[str] = None
    warehouse_location: Optional[str] = None
    invoice_number: Optional[str] = None
    remarks: Optional[str] = None
    transport_details: Optional[str] = None
    damage_or_short: Optional[str] = None
    receiving_status: str = "Received"


class GoodsReceivingCreate(GoodsReceivingBase):
    pass


class GoodsReceivingRead(GoodsReceivingBase):
    id: int
    receiving_date: datetime
    invoice_date: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True
