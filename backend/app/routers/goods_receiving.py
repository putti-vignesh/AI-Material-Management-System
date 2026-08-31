from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.goods_receiving import GoodsReceiving
from app.schemas.quality_inspection import GoodsReceivingCreate, GoodsReceivingRead
from app.utils.auth import get_current_user

router = APIRouter(tags=["Goods Receiving"])


@router.get("/goods_receiving", response_model=list[GoodsReceivingRead])
def list_grn(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """List all goods receiving notes"""
    grn_list = db.query(GoodsReceiving).all()
    return grn_list


@router.post("/goods_receiving", response_model=GoodsReceivingRead)
def create_grn(
    grn: GoodsReceivingCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Create a new goods receiving note"""
    # Check if GRN number already exists
    existing = db.query(GoodsReceiving).filter(
        GoodsReceiving.grn_number == grn.grn_number
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="GRN number already exists")

    db_grn = GoodsReceiving(**grn.dict())
    db.add(db_grn)
    db.commit()
    db.refresh(db_grn)
    return db_grn


@router.get("/goods_receiving/{grn_id}", response_model=GoodsReceivingRead)
def get_grn(
    grn_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Get a specific goods receiving note"""
    grn = db.query(GoodsReceiving).filter(GoodsReceiving.id == grn_id).first()
    if not grn:
        raise HTTPException(status_code=404, detail="GRN not found")
    return grn


@router.put("/goods_receiving/{grn_id}", response_model=GoodsReceivingRead)
def update_grn(
    grn_id: int,
    grn: GoodsReceivingCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Update a goods receiving note"""
    db_grn = db.query(GoodsReceiving).filter(GoodsReceiving.id == grn_id).first()
    if not db_grn:
        raise HTTPException(status_code=404, detail="GRN not found")

    for key, value in grn.dict().items():
        setattr(db_grn, key, value)
    db.commit()
    db.refresh(db_grn)
    return db_grn


@router.delete("/goods_receiving/{grn_id}")
def delete_grn(
    grn_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Delete a goods receiving note"""
    db_grn = db.query(GoodsReceiving).filter(GoodsReceiving.id == grn_id).first()
    if not db_grn:
        raise HTTPException(status_code=404, detail="GRN not found")
    db.delete(db_grn)
    db.commit()
    return {"detail": "GRN deleted"}


@router.get("/goods_receiving/by-status/{status}")
def get_grn_by_status(
    status: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Get GRN filtered by receiving status"""
    grn_list = db.query(GoodsReceiving).filter(
        GoodsReceiving.receiving_status == status
    ).all()
    return grn_list
