from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.material_return import MaterialReturn
from app.schemas.material_return import MaterialReturnCreate, MaterialReturnRead
from app.utils.auth import get_current_user

router = APIRouter(tags=["material-returns"])


@router.get("/material-returns", response_model=List[MaterialReturnRead])
def get_material_returns(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return db.query(MaterialReturn).offset(skip).limit(limit).all()


@router.post("/material-returns", response_model=MaterialReturnRead)
def create_material_return(
    payload: MaterialReturnCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    ret = MaterialReturn(**payload.model_dump())
    db.add(ret)
    db.commit()
    db.refresh(ret)
    return ret
