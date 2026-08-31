from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import Base, engine, SessionLocal
from app.models.inventory_transaction import InventoryTransaction
from app.models.material import Material
from app.models.purchase_request import PurchaseRequest
from app.models.purchase_order import PurchaseOrder
from app.models.stock_transfer import StockTransfer
from app.models.scrap_management import ScrapManagement
from app.models.material_return import MaterialReturn
from app.models.report import Report
from app.models.supplier import Supplier
from app.models.user import User
from app.models.warehouse import Warehouse
from app.models.quality_inspection import QualityInspection
from app.models.goods_receiving import GoodsReceiving
from app.routers import (
    auth, materials, suppliers, warehouses, purchase_requests, inventory,
    reports, chatbot, forecast, dashboard, quality_inspections, goods_receiving,
    purchase_orders, stock_transfers, scrap_management, material_returns, ai_extended
)
from app.utils.auth import hash_password

app = FastAPI(title="AI Material Management System", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


def seed_demo_data() -> None:
    db = SessionLocal()
    try:
        if not db.query(User).first():
            admin = User(
                username="admin",
                email="admin@example.com",
                password_hash=hash_password("admin123"),
                role="Admin",
            )
            db.add(admin)

        if not db.query(Material).first():
            db.add_all([
                Material(material_id="MAT-1001", name="Cement", category="Construction", unit="Bag", quantity=120, reserved_quantity=15, unit_price=350.0, minimum_stock=50, reorder_level=80, storage_location="A1", supplier="BuildCo", status="Active"),
                Material(material_id="MAT-1002", name="Steel", category="Construction", unit="Ton", quantity=85, reserved_quantity=10, unit_price=45000.0, minimum_stock=40, reorder_level=60, storage_location="B2", supplier="MetalWorks", status="Active"),
                Material(material_id="MAT-1003", name="Laptop", category="IT", unit="Unit", quantity=15, reserved_quantity=2, unit_price=65000.0, minimum_stock=10, reorder_level=12, storage_location="C3", supplier="TechHub", status="Active"),
            ])

        if not db.query(Supplier).first():
            db.add_all([
                Supplier(name="BuildCo", contact_person="Asha", email="asha@buildco.com", phone="9000000001", address="Mumbai"),
                Supplier(name="TechHub", contact_person="Rohan", email="rohan@techhub.com", phone="9000000002", address="Delhi"),
            ])

        if not db.query(Warehouse).first():
            db.add_all([
                Warehouse(name="Main Warehouse", location="Pune", capacity=5000, manager="Neha"),
                Warehouse(name="Regional Hub", location="Hyderabad", capacity=3000, manager="Kiran"),
            ])

        if not db.query(PurchaseRequest).first():
            db.add_all([
                PurchaseRequest(request_number="PR-001", material_name="Cement", quantity=50, supplier="BuildCo", priority="High", status="Pending", remarks="Urgent requirement"),
                PurchaseRequest(request_number="PR-002", material_name="Laptop", quantity=10, supplier="TechHub", priority="Medium", status="Approved", remarks="New office setup"),
            ])

        if not db.query(PurchaseOrder).first():
            db.add_all([
                PurchaseOrder(po_number="PO-2001", request_number="PR-002", supplier_name="TechHub", material_name="Laptop", quantity=10, unit_price=65000.0, total_amount=650000.0, status="Issued"),
            ])

        if not db.query(StockTransfer).first():
            db.add_all([
                StockTransfer(transfer_number="TR-501", material_name="Cement", source_warehouse="Main Warehouse", destination_warehouse="Regional Hub", quantity=20, status="Completed", remarks="Project shift transfer"),
            ])

        if not db.query(ScrapManagement).first():
            db.add_all([
                ScrapManagement(scrap_number="SCR-101", material_name="Cement", quantity=2, reason="Damaged packaging", warehouse_name="Main Warehouse", disposal_status="Recycled", estimated_scrap_value=300.0),
            ])

        if not db.query(MaterialReturn).first():
            db.add_all([
                MaterialReturn(return_number="RET-301", material_name="Steel", supplier_name="MetalWorks", quantity=1, reason="Quality Defect", status="Returned"),
            ])

        if not db.query(InventoryTransaction).first():
            db.add_all([
                InventoryTransaction(material_name="Cement", transaction_type="Stock In", quantity=30, reference="GRN-01", remarks="Received from BuildCo"),
                InventoryTransaction(material_name="Laptop", transaction_type="Stock Out", quantity=2, reference="ISS-01", remarks="Issued to IT team"),
            ])

        if not db.query(Report).first():
            db.add(Report(title="Monthly Inventory Summary", report_type="Inventory", summary="Inventory remains stable with low stock alerts monitored."))

        db.commit()
    finally:
        db.close()


seed_demo_data()

app.include_router(auth.router, prefix="/api")
app.include_router(materials.router, prefix="/api")
app.include_router(suppliers.router, prefix="/api")
app.include_router(warehouses.router, prefix="/api")
app.include_router(purchase_requests.router, prefix="/api")
app.include_router(purchase_orders.router, prefix="/api")
app.include_router(stock_transfers.router, prefix="/api")
app.include_router(scrap_management.router, prefix="/api")
app.include_router(material_returns.router, prefix="/api")
app.include_router(inventory.router, prefix="/api")
app.include_router(reports.router, prefix="/api")
app.include_router(chatbot.router, prefix="/api")
app.include_router(forecast.router, prefix="/api")
app.include_router(dashboard.router, prefix="/api")
app.include_router(quality_inspections.router, prefix="/api")
app.include_router(goods_receiving.router, prefix="/api")
app.include_router(ai_extended.router, prefix="/api")


@app.get("/")
def health_check():
    return {"status": "ok", "service": "AI Material Management System"}
