from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.report import Report
from app.schemas.report import ReportCreate, ReportRead
from app.utils.auth import get_current_user

router = APIRouter(tags=["reports"])


@router.get("/reports", response_model=List[ReportRead])
def get_reports(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=200), db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(Report).offset(skip).limit(limit).all()


@router.post("/reports", response_model=ReportRead)
def create_report(payload: ReportCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    report = Report(**payload.model_dump())
    db.add(report)
    db.commit()
    db.refresh(report)
    return report
