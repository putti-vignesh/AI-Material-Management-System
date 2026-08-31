from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.scrap_management import ScrapManagement
from app.schemas.scrap_management import ScrapManagementCreate, ScrapManagementRead
from app.utils.auth import get_current_user

router = APIRouter(tags=["scrap-management"])


@router.get("/scrap-management", response_model=List[ScrapManagementRead])
def get_scrap_records(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return db.query(ScrapManagement).offset(skip).limit(limit).all()


@router.post("/scrap-management", response_model=ScrapManagementRead)
def create_scrap_record(
    payload: ScrapManagementCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    scrap = ScrapManagement(**payload.model_dump())
    db.add(scrap)
    db.commit()
    db.refresh(scrap)
    return scrap
