from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.material import Material
from app.models.purchase_request import PurchaseRequest
from app.models.supplier import Supplier
from app.models.warehouse import Warehouse
from app.utils.auth import get_current_user

router = APIRouter(tags=["dashboard"])


@router.get("/dashboard")
def dashboard_summary(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    materials = db.query(Material).all()
    suppliers = db.query(Supplier).all()
    warehouses = db.query(Warehouse).all()
    requests = db.query(PurchaseRequest).filter(PurchaseRequest.status == "Pending").all()
    low_stock = [m.name for m in materials if m.quantity <= m.minimum_stock]
    return {
        "material_count": len(materials),
        "supplier_count": len(suppliers),
        "warehouse_count": len(warehouses),
        "pending_requests": len(requests),
        "low_stock": low_stock,
    }
