from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.stock_transfer import StockTransfer
from app.schemas.stock_transfer import StockTransferCreate, StockTransferRead
from app.utils.auth import get_current_user

router = APIRouter(tags=["stock-transfers"])


@router.get("/stock-transfers", response_model=List[StockTransferRead])
def get_stock_transfers(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return db.query(StockTransfer).offset(skip).limit(limit).all()


@router.post("/stock-transfers", response_model=StockTransferRead)
def create_stock_transfer(
    payload: StockTransferCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    transfer = StockTransfer(**payload.model_dump())
    db.add(transfer)
    db.commit()
    db.refresh(transfer)
    return transfer
