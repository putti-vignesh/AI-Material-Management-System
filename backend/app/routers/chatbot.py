from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.material import Material
from app.models.supplier import Supplier
from app.models.purchase_request import PurchaseRequest
from app.services.ai_assistant import GeminiAssistant
from app.utils.auth import get_current_user

router = APIRouter(tags=["chatbot"])


@router.post("/chatbot")
def chatbot(
    query: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    materials = db.query(Material).all()
    suppliers = db.query(Supplier).all()
    purchase_requests = db.query(PurchaseRequest).all()

    material_text = ""

    for m in materials:
        material_text += (
            f"""
Material ID: {m.material_id}
Name: {m.name}
Category: {m.category}
Quantity: {m.quantity}
Unit: {m.unit}
Minimum Stock: {m.minimum_stock}
Reorder Level: {m.reorder_level}
Supplier: {m.supplier}
Status: {m.status}

"""
        )

    supplier_text = ""

    for s in suppliers:
        supplier_text += (
            f"""
Supplier: {s.name}
Contact: {s.contact_person}
Email: {s.email}
Phone: {s.phone}

"""
        )

    purchase_text = ""

    for p in purchase_requests:
        purchase_text += (
            f"""
Purchase Request: {p.request_number}
Material: {p.material_name}
Quantity: {p.quantity}
Supplier: {p.supplier}
Priority: {p.priority}
Status: {p.status}

"""
        )

    prompt = f"""
You are an AI Procurement Assistant.

Use ONLY the information below.

======================
MATERIALS
======================

{material_text}

======================
SUPPLIERS
======================

{supplier_text}

======================
PURCHASE REQUESTS
======================

{purchase_text}

======================
USER QUESTION
======================

{query}

Answer ONLY using the data above.

If the answer is not available in the data,
reply exactly:

"I couldn't find that information in the inventory database."
"""

    assistant = GeminiAssistant()

    answer = assistant.generate_summary(prompt)

    return {"answer": answer}