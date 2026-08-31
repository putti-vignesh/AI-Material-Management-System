from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.material import Material
from app.schemas.material import MaterialCreate, MaterialRead
from app.utils.auth import get_current_user

router = APIRouter(tags=["materials"])


@router.get("/materials", response_model=List[MaterialRead])
def get_materials(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return db.query(Material).offset(skip).limit(limit).all()


@router.post("/materials", response_model=MaterialRead)
def create_material(payload: MaterialCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    material = Material(**payload.model_dump())
    db.add(material)
    db.commit()
    db.refresh(material)
    return material


@router.put("/materials/{material_id}", response_model=MaterialRead)
def update_material(material_id: int, payload: MaterialCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    material = db.query(Material).filter(Material.id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    for key, value in payload.model_dump().items():
        setattr(material, key, value)
    db.commit()
    db.refresh(material)
    return material


@router.delete("/materials/{material_id}")
def delete_material(material_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    material = db.query(Material).filter(Material.id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    db.delete(material)
    db.commit()
    return {"message": "Material deleted"}
