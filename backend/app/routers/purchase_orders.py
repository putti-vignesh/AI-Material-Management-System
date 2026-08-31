from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.purchase_order import PurchaseOrder
from app.schemas.purchase_order import PurchaseOrderCreate, PurchaseOrderRead
from app.utils.auth import get_current_user

router = APIRouter(tags=["purchase-orders"])


@router.get("/purchase-orders", response_model=List[PurchaseOrderRead])
def get_purchase_orders(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return db.query(PurchaseOrder).offset(skip).limit(limit).all()


@router.post("/purchase-orders", response_model=PurchaseOrderRead)
def create_purchase_order(
    payload: PurchaseOrderCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing = db.query(PurchaseOrder).filter(PurchaseOrder.po_number == payload.po_number).first()
    if existing:
        raise HTTPException(status_code=400, detail="PO number already exists")
    
    order = PurchaseOrder(**payload.model_dump())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


@router.put("/purchase-orders/{po_id}", response_model=PurchaseOrderRead)
def update_purchase_order(
    po_id: int,
    payload: PurchaseOrderCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    order = db.query(PurchaseOrder).filter(PurchaseOrder.id == po_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Purchase order not found")
    for key, value in payload.model_dump().items():
        setattr(order, key, value)
    db.commit()
    db.refresh(order)
    return order


@router.delete("/purchase-orders/{po_id}")
def delete_purchase_order(
    po_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    order = db.query(PurchaseOrder).filter(PurchaseOrder.id == po_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Purchase order not found")
    db.delete(order)
    db.commit()
    return {"message": "Purchase order deleted"}
