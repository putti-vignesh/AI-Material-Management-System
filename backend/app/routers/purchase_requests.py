from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.purchase_request import PurchaseRequest
from app.schemas.purchase_request import PurchaseRequestCreate, PurchaseRequestRead
from app.utils.auth import get_current_user

router = APIRouter(tags=["purchase-requests"])


@router.get("/purchase-requests", response_model=List[PurchaseRequestRead])
def get_purchase_requests(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=200), db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(PurchaseRequest).offset(skip).limit(limit).all()


@router.post("/purchase-requests", response_model=PurchaseRequestRead)
def create_purchase_request(payload: PurchaseRequestCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    purchase_request = PurchaseRequest(**payload.model_dump())
    db.add(purchase_request)
    db.commit()
    db.refresh(purchase_request)
    return purchase_request


@router.put("/purchase-requests/{request_id}", response_model=PurchaseRequestRead)
def update_purchase_request(request_id: int, payload: PurchaseRequestCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    purchase_request = db.query(PurchaseRequest).filter(PurchaseRequest.id == request_id).first()
    if not purchase_request:
        raise HTTPException(status_code=404, detail="Purchase request not found")
    for key, value in payload.model_dump().items():
        setattr(purchase_request, key, value)
    db.commit()
    db.refresh(purchase_request)
    return purchase_request
