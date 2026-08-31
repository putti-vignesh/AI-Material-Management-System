from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.warehouse import Warehouse
from app.schemas.warehouse import WarehouseCreate, WarehouseRead
from app.utils.auth import get_current_user

router = APIRouter(tags=["warehouses"])


@router.get("/warehouses", response_model=List[WarehouseRead])
def get_warehouses(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=200), db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(Warehouse).offset(skip).limit(limit).all()


@router.post("/warehouses", response_model=WarehouseRead)
def create_warehouse(payload: WarehouseCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    warehouse = Warehouse(**payload.model_dump())
    db.add(warehouse)
    db.commit()
    db.refresh(warehouse)
    return warehouse


@router.put("/warehouses/{warehouse_id}", response_model=WarehouseRead)
def update_warehouse(warehouse_id: int, payload: WarehouseCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    warehouse = db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    for key, value in payload.model_dump().items():
        setattr(warehouse, key, value)
    db.commit()
    db.refresh(warehouse)
    return warehouse


@router.delete("/warehouses/{warehouse_id}")
def delete_warehouse(warehouse_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    warehouse = db.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    db.delete(warehouse)
    db.commit()
    return {"message": "Warehouse deleted"}
