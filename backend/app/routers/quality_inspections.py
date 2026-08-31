from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.quality_inspection import QualityInspection
from app.schemas.quality_inspection import QualityInspectionCreate, QualityInspectionRead
from app.utils.auth import get_current_user

router = APIRouter(tags=["Quality Inspections"])


@router.get("/quality_inspections", response_model=list[QualityInspectionRead])
def list_inspections(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """List all quality inspections"""
    inspections = db.query(QualityInspection).all()
    return inspections


@router.post("/quality_inspections", response_model=QualityInspectionRead)
def create_inspection(
    inspection: QualityInspectionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Create a new quality inspection"""
    # Check if GRN already exists
    existing = db.query(QualityInspection).filter(
        QualityInspection.grn_number == inspection.grn_number
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="GRN number already exists")

    db_inspection = QualityInspection(**inspection.dict())
    db.add(db_inspection)
    db.commit()
    db.refresh(db_inspection)
    return db_inspection


@router.get("/quality_inspections/{inspection_id}", response_model=QualityInspectionRead)
def get_inspection(
    inspection_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Get a specific quality inspection"""
    inspection = db.query(QualityInspection).filter(
        QualityInspection.id == inspection_id
    ).first()
    if not inspection:
        raise HTTPException(status_code=404, detail="Inspection not found")
    return inspection


@router.put("/quality_inspections/{inspection_id}", response_model=QualityInspectionRead)
def update_inspection(
    inspection_id: int,
    inspection: QualityInspectionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Update a quality inspection"""
    db_inspection = db.query(QualityInspection).filter(
        QualityInspection.id == inspection_id
    ).first()
    if not db_inspection:
        raise HTTPException(status_code=404, detail="Inspection not found")

    for key, value in inspection.dict().items():
        setattr(db_inspection, key, value)
    db.commit()
    db.refresh(db_inspection)
    return db_inspection


@router.delete("/quality_inspections/{inspection_id}")
def delete_inspection(
    inspection_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Delete a quality inspection"""
    db_inspection = db.query(QualityInspection).filter(
        QualityInspection.id == inspection_id
    ).first()
    if not db_inspection:
        raise HTTPException(status_code=404, detail="Inspection not found")
    db.delete(db_inspection)
    db.commit()
    return {"detail": "Inspection deleted"}


@router.get("/quality_inspections/by-status/{status}")
def get_inspections_by_status(
    status: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """Get inspections filtered by quality status"""
    inspections = db.query(QualityInspection).filter(
        QualityInspection.quality_status == status
    ).all()
    return inspections
