# Software Requirements Specification (SRS)

# Project 28: AI-Enabled Material Management System

Version: 1.0

Prepared By:
Project Team

Technology Stack:
Python • FastAPI • PostgreSQL • HTML • CSS • JavaScript • Docker • Google Gemini AI

---

# Table of Contents

1. Introduction
2. Overall Description
3. Functional Requirements
4. Non-Functional Requirements
5. AI Functional Requirements
6. Database Requirements
7. External Interface Requirements
8. System Requirements
9. Use Case Descriptions
10. Assumptions
11. Constraints
12. Testing Requirements
13. Future Enhancements
14. References

---

# 1. Introduction

## 1.1 Purpose

The AI-Enabled Material Management System is designed to automate and simplify inventory and procurement management within an organization.

The system replaces manual spreadsheet-based inventory tracking by providing centralized stock management, warehouse monitoring, procurement planning, supplier management, purchase request processing, purchase order generation, quality inspection, stock transfers, scrap management, material returns, and AI-powered procurement assistance.

This Software Requirements Specification (SRS) describes all functional, non-functional, technical, and AI requirements of the system.

The document serves as the primary reference for developers, testers, project reviewers, and future maintenance teams.

---

## 1.2 Scope

The system supports complete material lifecycle management.

The application allows organizations to

- Maintain Material Master
- Manage Suppliers
- Manage Warehouses
- Raise Purchase Requests
- Generate Purchase Orders
- Record Goods Receiving Notes (GRN)
- Perform Quality Inspection
- Transfer Stock
- Record Scrap
- Process Material Returns
- Monitor Inventory
- Generate Reports
- Use Artificial Intelligence for procurement decision support

The project combines inventory management with Artificial Intelligence to improve procurement efficiency and reduce stock shortages.

---

## 1.3 Intended Audience

The system is designed for the following users.

### Store Managers

- Manage inventory
- Monitor stock levels
- Track warehouse activities
- Perform stock transfers

### Procurement Team

- Raise purchase requests
- Generate purchase orders
- Review AI recommendations
- Manage suppliers

### Warehouse Staff

- Receive materials
- Update inventory
- Record goods movement

### Quality Inspectors

- Inspect received materials
- Approve or reject batches
- Record quality issues

### Department Heads

- Request materials
- Monitor request status

### System Administrator

- Manage users
- Configure system settings
- Maintain master data
- Monitor system activities

---

# 2. Overall Description

## 2.1 Product Perspective

The AI Material Management System is a web-based full-stack application.

The architecture consists of four logical layers.

Presentation Layer

- HTML5
- CSS3
- Bootstrap
- JavaScript

Application Layer

- FastAPI REST API
- SQLAlchemy ORM
- JWT Authentication
- Pydantic Validation

Database Layer

- PostgreSQL Database

AI Layer

- Google Gemini AI
- Supplier Recommendation
- Lead Time Prediction
- Material Substitution
- Wastage Analysis
- AI Chatbot

The frontend communicates with FastAPI REST APIs.

FastAPI performs business logic and database operations using SQLAlchemy.

The AI module provides intelligent recommendations for procurement planning.

---

## 2.2 Product Functions

The application consists of the following modules.

### Material Management

- Add Material
- Update Material
- Delete Material
- Search Materials
- Material Categories
- Storage Rules
- Reorder Levels
- Reserved Stock

---

### Supplier Management

- Add Supplier
- Update Supplier
- Delete Supplier
- View Supplier Information

---

### Warehouse Management

- Warehouse Creation
- Capacity Management
- Warehouse Locations
- Warehouse CRUD

---

### Purchase Request Management

- Create Request
- Modify Request
- Approval Status
- Priority Management
- Department Requests

---

### Purchase Order Management

- Generate Purchase Orders
- Supplier Assignment
- Order Tracking
- Delivery Status

---

### Goods Receiving (GRN)

- Record Incoming Goods
- Batch Details
- Accepted Quantity
- Rejected Quantity
- Warehouse Assignment

---

### Quality Inspection

- Material Inspection
- Defect Recording
- Batch Approval
- Batch Rejection

---

### Inventory Management

- Current Stock
- Reserved Stock
- Material Valuation
- Reorder Monitoring

---

### Stock Transfer

- Warehouse to Warehouse Transfer
- Transfer Tracking
- Transfer Status

---

### Scrap Management

- Scrap Recording
- Disposal Status
- Estimated Scrap Value

---

### Material Returns

- Return Damaged Materials
- Vendor Returns
- Return Approval

---

### Dashboard

Provides

- Inventory Statistics
- Material Counts
- Purchase Statistics
- Warehouse Statistics
- Supplier Statistics
- AI Insights

---

### Authentication Module

- JWT Login
- Password Hashing
- Authorization
- Role-Based Access Control (RBAC)

---

### Artificial Intelligence Module

Provides intelligent decision support through

- Lead Time Prediction
- Supplier Recommendation
- Material Substitute Suggestion
- Wastage Analysis
- AI Inventory Chatbot

---

# 3. Functional Requirements

## 3.1 User Authentication

The system shall

- Authenticate users using JWT tokens.
- Encrypt passwords using bcrypt.
- Restrict APIs based on authentication.
- Support Admin role access.

---

## 3.2 Material Management

The system shall

- Create materials.
- Update materials.
- Delete materials.
- View material details.
- Search materials.
- Store specifications.
- Store storage rules.
- Track reorder levels.
- Track minimum stock.
- Maintain reserved stock.

---

## 3.3 Supplier Management

The system shall

- Create suppliers.
- Update suppliers.
- Delete suppliers.
- Display supplier information.
- Associate suppliers with materials.

---

## 3.4 Warehouse Management

The system shall

- Create warehouses.
- Update warehouse details.
- Delete warehouses.
- Maintain warehouse capacity.
- Assign warehouse managers.

---

## 3.5 Purchase Request Module

The system shall

- Create purchase requests.
- Assign priorities.
- Specify urgency.
- Track approval status.
- Link requests with projects.

---

## 3.6 Purchase Order Module

The system shall

- Generate purchase orders.
- Calculate total amount.
- Track supplier information.
- Maintain delivery status.

---

## 3.7 Goods Receiving Module

The system shall

- Record incoming goods.
- Generate GRN records.
- Record received quantities.
- Track batches.

---

## 3.8 Quality Inspection Module

The system shall

- Record inspection results.
- Accept materials.
- Reject defective materials.
- Store defect descriptions.

---

## 3.9 Inventory Module

The system shall

- Monitor inventory.
- Calculate stock levels.
- Track reserved inventory.
- Maintain stock valuation.

---

## 3.10 Stock Transfer Module

The system shall

- Transfer materials between warehouses.
- Track transfer status.
- Update inventory automatically.

---

## 3.11 Scrap Management Module

The system shall

- Record scrap quantity.
- Store disposal information.
- Estimate scrap value.

---

## 3.12 Material Return Module

The system shall

- Process returns.
- Maintain return status.
- Associate returns with suppliers.

---

## 3.13 Dashboard Module

The dashboard shall display

- Total Materials
- Total Suppliers
- Total Warehouses
- Purchase Requests
- Purchase Orders
- Stock Alerts
- AI Recommendations
- Inventory Statistics