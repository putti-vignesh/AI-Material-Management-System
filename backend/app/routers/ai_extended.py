from fastapi import APIRouter, Depends, HTTPException, Query, UploadFile, File
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.material import Material
from app.models.supplier import Supplier
from app.models.goods_receiving import GoodsReceiving
from app.models.scrap_management import ScrapManagement
from app.utils.auth import get_current_user
from app.services.ai_procurement_service import AIProcurementService
import random

router = APIRouter(tags=["AI Intelligence"])


@router.get("/ai/recommend-supplier")
def recommend_supplier(
    material_name: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """AI-assisted Supplier Recommendation based on reliability & order history"""
    suppliers = db.query(Supplier).all()
    supplier_list = [{"id": s.id, "name": s.name, "contact_person": s.contact_person, "email": s.email, "phone": s.phone} for s in suppliers]
    
    res = AIProcurementService.recommend_supplier(material_name, supplier_list)
    
    # Calculate score based on past GRN receipts & mock reliability metrics
    scored_suppliers = []
    for s in suppliers:
        grn_count = db.query(GoodsReceiving).filter(GoodsReceiving.supplier_name == s.name).count()
        score = 80 + (grn_count * 2) + random.randint(1, 10)
        scored_suppliers.append({
            "supplier_id": s.id,
            "name": s.name,
            "contact_person": s.contact_person,
            "reliability_score": min(score, 99),
            "estimated_lead_time_days": random.randint(3, 7)
        })
    
    scored_suppliers.sort(key=lambda x: x["reliability_score"], reverse=True)
    best = scored_suppliers[0] if scored_suppliers else None
    
    return {
        "material_name": material_name,
        "recommended_supplier": best,
        "all_ranked_suppliers": scored_suppliers,
        "ai_explanation": res.get("ai_explanation")
    }


@router.get("/ai/predict-leadtime")
def predict_leadtime(
    supplier_name: str,
    material_name: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """AI Lead-Time Prediction Model"""
    res = AIProcurementService.predict_lead_time(supplier_name, material_name)
    grns = db.query(GoodsReceiving).filter(
        GoodsReceiving.supplier_name.ilike(f"%{supplier_name}%")
    ).all()
    
    res["historical_grn_samples"] = len(grns)
    return res


@router.get("/ai/suggest-substitutes")
def suggest_substitutes(
    material_name: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """AI Substitute Suggestion Engine when a primary material is low or out of stock"""
    materials = db.query(Material).all()
    mat_list = [{"id": m.id, "name": m.name, "quantity": m.quantity, "unit": m.unit} for m in materials]
    
    res = AIProcurementService.suggest_substitutes(material_name, mat_list)
    return res


@router.get("/ai/wastage-analysis")
def wastage_analysis(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """AI Wastage Anomaly & Scrap Risk Detection"""
    scraps = db.query(ScrapManagement).all()
    scrap_list = [{"quantity": s.quantity, "reason": s.reason} for s in scraps]
    
    res = AIProcurementService.detect_wastage_anomalies(scrap_list)
    materials = db.query(Material).all()
    high_risk_items = [m.name for m in materials if m.quantity <= m.minimum_stock]
    res["high_wastage_risk_materials"] = high_risk_items
    return res


@router.post("/ai/ocr-invoice")
async def ocr_invoice(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user)
):
    """AI OCR Document Scanner for GRN Invoice parsing"""
    try:
        content_bytes = await file.read()
        text_content = content_bytes.decode('utf-8', errors='ignore')
    except Exception:
        text_content = ""
    
    return AIProcurementService.parse_ocr_invoice(text_content, file.filename)
