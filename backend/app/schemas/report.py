from typing import Optional
from pydantic import BaseModel


class ReportBase(BaseModel):
    title: str
    report_type: str
    summary: Optional[str] = None


class ReportCreate(ReportBase):
    pass


class ReportRead(ReportBase):
    id: int

    class Config:
        from_attributes = True
