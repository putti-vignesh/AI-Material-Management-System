# Entity-Relationship (ER) Diagram
## Project 28: AI-Enabled Material Management System

The following Entity Relationship Diagram represents the logical database design of the AI-Enabled Material Management System.

```mermaid
erDiagram

    USERS {
        int id PK
        string username UK
        string email UK
        string password_hash
        string role
        boolean is_active
        datetime created_at
    }

    MATERIALS {
        int id PK
        string material_id UK
        string name
        string category
        string unit
        float quantity
        float reserved_quantity
        float unit_price
        float minimum_stock
        float reorder_level
        string storage_location
        string supplier
        string status
        text specifications
        text storage_rules
        datetime created_at
    }

    SUPPLIERS {
        int id PK
        string name
        string contact_person
        string email
        string phone
        string address
    }

    WAREHOUSES {
        int id PK
        string name
        string location
        float capacity
        string manager
    }

    PURCHASE_REQUESTS {
        int id PK
        string request_number UK
        string material_name
        float quantity
        string supplier
        string priority
        string urgency
        string project_reference
        string status
        string requested_by
        string remarks
    }

    PURCHASE_ORDERS {
        int id PK
        string po_number UK
        string request_number
        string supplier_name
        string material_name
        float quantity
        float unit_price
        float total_amount
        datetime order_date
        datetime expected_delivery_date
        string status
        datetime created_at
    }

    GOODS_RECEIVING {
        int id PK
        string grn_number UK
        string po_number
        string supplier_name
        string warehouse_name
        string material_name
        string batch_number
        float ordered_quantity
        float received_quantity
        float accepted_quantity
        float rejected_quantity
        string unit
        datetime received_date
        string receiving_status
        string remarks
    }

    QUALITY_INSPECTIONS {
        int id PK
        string inspection_number UK
        string grn_number
        string material_name
        float ordered_quantity
        float received_quantity
        float accepted_quantity
        float rejected_quantity
        string quality_status
        text defects_found
        string inspector
        datetime inspection_date
    }

    INVENTORY_TRANSACTIONS {
        int id PK
        string material_name
        string transaction_type
        float quantity
        string reference
        string remarks
        datetime created_at
    }

    STOCK_TRANSFERS {
        int id PK
        string transfer_number UK
        string material_name
        string source_warehouse
        string destination_warehouse
        float quantity
        string status
        datetime transfer_date
    }

    SCRAP_RECORDS {
        int id PK
        string scrap_number UK
        string material_name
        float quantity
        string reason
        string disposal_status
        float estimated_scrap_value
        datetime created_at
    }

    MATERIAL_RETURNS {
        int id PK
        string return_number UK
        string material_name
        string supplier_name
        float quantity
        string reason
        string status
        datetime created_at
    }

    %% -----------------------------
    %% Relationships
    %% -----------------------------

    USERS ||--o{ PURCHASE_REQUESTS : raises

    MATERIALS ||--o{ PURCHASE_REQUESTS : requested_in
    MATERIALS ||--o{ PURCHASE_ORDERS : ordered_in
    MATERIALS ||--o{ GOODS_RECEIVING : received_as
    MATERIALS ||--o{ INVENTORY_TRANSACTIONS : tracked_by
    MATERIALS ||--o{ STOCK_TRANSFERS : transferred
    MATERIALS ||--o{ SCRAP_RECORDS : scrapped
    MATERIALS ||--o{ MATERIAL_RETURNS : returned

    SUPPLIERS ||--o{ PURCHASE_ORDERS : supplies
    SUPPLIERS ||--o{ MATERIAL_RETURNS : accepts_return

    PURCHASE_REQUESTS ||--o{ PURCHASE_ORDERS : generates

    PURCHASE_ORDERS ||--o{ GOODS_RECEIVING : fulfilled_by

    GOODS_RECEIVING ||--|| QUALITY_INSPECTIONS : inspected

    WAREHOUSES ||--o{ GOODS_RECEIVING : receives
    WAREHOUSES ||--o{ STOCK_TRANSFERS : source
    WAREHOUSES ||--o{ STOCK_TRANSFERS : destination
```

---

# Entity Description

### USERS
Stores user login credentials, roles, authentication details, and access permissions.

### MATERIALS
Master inventory table containing all materials with stock levels, pricing, storage rules, and reorder information.

### SUPPLIERS
Stores supplier contact information and vendor details used during procurement.

### WAREHOUSES
Represents warehouse locations used for inventory storage and stock transfers.

### PURCHASE REQUESTS
Department requests for purchasing new materials including urgency, priority, and project references.

### PURCHASE ORDERS
Official purchase orders generated from approved purchase requests.

### GOODS RECEIVING (GRN)
Captures all incoming deliveries from suppliers including received quantities and batch details.

### QUALITY INSPECTIONS
Stores inspection results for every Goods Receipt Note (GRN) including accepted and rejected quantities.

### INVENTORY TRANSACTIONS
Maintains the complete stock movement history including issue, receipt, return, adjustment, and consumption.

### STOCK TRANSFERS
Tracks movement of materials between warehouses.

### SCRAP RECORDS
Stores damaged, expired, or unusable material details along with estimated scrap value.

### MATERIAL RETURNS
Tracks material returns sent back to suppliers due to defects or excess procurement.

---

# AI Modules (Logical Layer)

The AI Engine operates on the following entities:

- Materials
- Suppliers
- Purchase Requests
- Purchase Orders
- Goods Receiving
- Inventory Transactions
- Scrap Records

The AI layer provides:

- Material Demand Forecasting
- Supplier Recommendation
- Lead Time Prediction
- Substitute Material Recommendation
- Wastage Risk Detection
- Natural Language Inventory Chatbot