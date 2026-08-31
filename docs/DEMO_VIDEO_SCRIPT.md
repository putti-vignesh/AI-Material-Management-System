# Capstone Project Demo Video Script & Walkthrough Guide

**Project Title**: Project 28 - Material Management with AI  
**Target Duration**: 5 Minutes  
**Presenter**: Student / Development Team  

---

## 🎬 5-Minute Video Presentation Timestamp Breakdown

| Timestamp | Screen Focus | Dialogue & Script Highlights |
| :--- | :--- | :--- |
| **0:00 - 0:30** | Title Slide / Login Page | "Hello everyone. Welcome to the demonstration of Project 28: Material Management System with AI. In this capstone, we built a full-stack, AI-assisted platform targeting manufacturing, construction, and operations teams." |
| **0:30 - 1:15** | Dashboard & Material Master | "After logging in with JWT authentication, we land on the real-time Dashboard. Here we see stock metrics, active purchase requests, total inventory valuation, and recent transactions. In the Material Master module, we track stock levels, reserved stock for active jobs, unit price, and total valuation." |
| **1:15 - 2:15** | Procurement & Orders Workflow | "Next is the procurement workflow. Departments raise Purchase Requests, which feed into Purchase Orders. Our system automatically ranks vendors using historical fulfillment speeds, lead times, and reliability metrics." |
| **2:15 - 3:30** | AI Intelligence Suite & OCR | "Here is our core AI Intelligence Suite. We demonstrate 5 distinct AI capabilities:<br>1. **AI Lead-Time Predictor** forecasting vendor delivery days.<br>2. **In-Stock Substitute Suggestion Engine** finding alternatives when primary items run low.<br>3. **Wastage Anomaly & Scrap Risk Detector** scanning scrap logs.<br>4. **AI Supplier Recommendation Engine** ranking vendors.<br>5. **AI OCR Invoice Scanner** extracting PO #, invoice total, and vendor details from receipts." |
| **3:30 - 4:15** | Stock Control & Quality Checks | "In the Stock Control layer, we manage Warehouse Stock Transfers, Scrap & Wastage entries, Material Returns for rejected items, and Goods Receiving Notes (GRN) with mandatory Quality Inspections." |
| **4:15 - 5:00** | Architecture, Docker & Conclusion | "The system is fully containerized using Docker & Docker Compose orchestrating FastAPI, PostgreSQL, and Bootstrap frontend. Complete documentation including SRS, Architecture, ER Diagram, User Manual, and API Docs are available in the repository. Thank you!" |

---

## 🎥 Recording Instructions
1. Open OBS Studio or Loom.
2. Launch the backend (`uvicorn app.main:app --reload`) and open `http://127.0.0.1:8000/docs` and `frontend/dashboard.html`.
3. Follow the timestamp guide above.
