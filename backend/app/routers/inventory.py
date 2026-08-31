from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.inventory_transaction import InventoryTransaction
from app.schemas.inventory import InventoryTransactionCreate, InventoryTransactionRead
from app.utils.auth import get_current_user

router = APIRouter(tags=["inventory"])


@router.get("/inventory", response_model=List[InventoryTransactionRead])
def get_inventory(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=200), db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(InventoryTransaction).offset(skip).limit(limit).all()


@router.post("/inventory", response_model=InventoryTransactionRead)
def create_inventory_transaction(payload: InventoryTransactionCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    transaction = InventoryTransaction(**payload.model_dump())
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction
