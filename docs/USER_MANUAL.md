# User & Admin Operating Manual
## Project 28: AI Material Management System

---

## 1. Getting Started

### 1.1 Accessing the Application
1. Launch the system using `.\start_project.ps1` or run:
   ```bash
   cd backend
   python -m uvicorn app.main:app --reload --port 8000
   ```
2. Open `frontend/index.html` in your web browser.

### 1.2 Default Credentials
- **Username**: `admin`
- **Password**: `admin123`

---

## 2. Feature Walkthrough

### 2.1 Dashboard Overview
- View key metrics: Total Materials, Active Suppliers, Warehouses, and Pending Requests.
- Review low-stock warning banners.
- View interactive stock distribution graphs.
- Use the **AI Chatbot Widget** to ask natural language questions like *"What is the quantity of Cement?"*.

### 2.2 Material Master Management (`materials.html`)
- Click **Add Material** to create new raw material records.
- Enter specifications, storage rules, minimum stock levels, reorder thresholds, and unit valuation.
- Filter, edit, or delete material items.

### 2.3 Purchase Requests & Purchase Orders (`purchase_requests.html`, `purchase_orders.html`)
- Departments raise purchase requests.
- Click **Approve** on a purchase request to advance it.
- Open **Purchase Orders** to issue formal orders to vendors.
- Click **Recommend Supplier** to use AI to select the best vendor based on lead time and historical reliability.

### 2.4 Goods Receiving & Quality Inspections (`goods_receiving.html`, `quality_inspections.html`)
- Warehouse staff create Goods Receiving Notes (GRNs) for incoming deliveries.
- Quality inspectors log batch numbers, accepted quantities, rejected quantities, and defect descriptions.

### 2.5 Inventory & Stock Control (`inventory.html`)
- Log Stock In and Stock Out transactions.
- Track material issue slips linked to reference codes.

### 2.6 Reports & Analytics (`reports.html`)
- View monthly inventory summaries and AI demand forecasting charts.
