# 4. Non-Functional Requirements

## 4.1 Performance

The system shall provide high performance for inventory and procurement operations.

Requirements include:

- API response time should be less than 200 milliseconds for normal CRUD operations.
- Dashboard statistics should load within 2 seconds.
- Database queries should be optimized using SQLAlchemy ORM.
- Support at least 100 concurrent users.
- AI services should respond within 5–10 seconds depending on network conditions.

---

## 4.2 Security

The system shall provide secure authentication and authorization.

Security features include:

- JWT-based Authentication
- Password hashing using bcrypt
- Protected REST APIs
- Role-Based Access Control (RBAC)
- Secure HTTP communication
- Input validation using Pydantic
- SQL Injection prevention using SQLAlchemy ORM
- Environment variables for sensitive configuration

---

## 4.3 Reliability

The system shall ensure reliable operation.

- Automatic database transaction rollback on failures.
- AI chatbot falls back gracefully if Gemini API is unavailable.
- Docker containers automatically restart after failures.
- Exception handling for API endpoints.
- Validation for all user inputs.

---

## 4.4 Availability

The application shall be available whenever the backend server and database are running.

Availability features include:

- Dockerized deployment
- PostgreSQL persistent storage
- REST API health availability
- Swagger API documentation

---

## 4.5 Scalability

The system is designed to support future expansion.

Possible improvements include:

- Cloud deployment on AWS
- Multiple warehouse support
- Multiple organization support
- Increased concurrent users
- AI model upgrades

---

## 4.6 Maintainability

The application follows modular architecture.

Modules include:

- Routers
- Services
- Models
- Schemas
- Database Layer
- Authentication Layer
- AI Services

This structure simplifies maintenance and future enhancements.

---

## 4.7 Portability

The application can run on

- Windows
- Linux
- Docker
- AWS EC2
- AWS ECS

without major modifications.

---

# 5. AI Functional Requirements

Artificial Intelligence is integrated to improve procurement planning and inventory management.

---

## 5.1 Lead-Time Prediction

### Purpose

Estimate expected supplier delivery time.

### Input

- Supplier Name
- Material Name

### Output

- Estimated Lead Time
- Confidence Level

Example

Supplier:
BuildCo

Material:
Cement

Output:

Estimated Delivery:
8 Days

Confidence:
Medium

---

## 5.2 Supplier Recommendation

### Purpose

Recommend the best supplier.

### Input

Material Name

### Output

Recommended Supplier

Recommendation Reason

Example

Material:
Steel

Output

Recommended Supplier:
BuildCo

Reason

- Better delivery history
- Lower defect rate
- Higher fulfillment speed

---

## 5.3 Material Substitute Recommendation

### Purpose

Suggest alternative materials available in stock.

### Input

Required Material

### Output

List of substitute materials

Category similarity

Available quantity

Example

Input

Cement

Output

Steel

Laptop

(Example output based on current sample dataset.)

---

## 5.4 Wastage Analysis

### Purpose

Identify abnormal material wastage.

### Input

Inventory data

Consumption history

### Output

Risk Level

Low

Medium

High

Recommendations

---

## 5.5 AI Chatbot

### Purpose

Answer inventory-related questions using Google Gemini AI and inventory data.

### Supported Queries

Examples:

- Show all materials
- Which material has highest stock?
- Show low stock materials
- Who supplies laptops?
- Which materials need reorder?
- Show purchase requests

### Output

Natural language response generated using inventory data and Gemini AI.

---

# 6. Database Requirements

The application uses PostgreSQL as the primary relational database.

Database access is performed through SQLAlchemy ORM.

---

## Primary Tables

- Users
- Materials
- Suppliers
- Warehouses
- Purchase Requests
- Purchase Orders
- Goods Receiving
- Quality Inspections
- Stock Transfers
- Scrap Records
- Material Returns

---

## Relationships

Materials

↓

Purchase Requests

↓

Purchase Orders

↓

Goods Receiving

↓

Quality Inspection

↓

Inventory

Suppliers are linked with

- Materials
- Purchase Orders
- Material Returns

Warehouses manage

- Inventory
- Stock Transfers

---

## Database Features

- ACID Transactions
- Primary Keys
- Foreign Keys
- Auto Increment IDs
- Indexed Search
- Transaction Rollback
- SQLAlchemy ORM

---

# 7. External Interface Requirements

## 7.1 User Interface

Frontend technologies

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

Features

- Responsive Dashboard
- CRUD Forms
- Search
- Filters
- Statistics Cards
- Tables
- AI Dashboard

---

## 7.2 Software Interface

Backend

Python FastAPI

Database

PostgreSQL

Authentication

JWT

AI

Google Gemini API

---

## 7.3 API Interface

REST APIs

Example endpoints

POST /api/login

GET /api/materials

POST /api/materials

PUT /api/materials/{id}

DELETE /api/materials/{id}

GET /api/suppliers

GET /api/dashboard

GET /api/ai/predict-leadtime

GET /api/ai/recommend-supplier

GET /api/ai/suggest-substitutes

GET /api/ai/wastage-analysis

POST /api/chatbot

Swagger documentation is available at

```
/docs
```

---

# 8. System Requirements

## Software Requirements

Operating System

- Windows 10/11
- Linux

Programming Language

- Python 3.12

Framework

- FastAPI

Database

- PostgreSQL

ORM

- SQLAlchemy

Frontend

- HTML5
- CSS3
- Bootstrap
- JavaScript

Authentication

- JWT
- bcrypt

AI

- Google Gemini API
- Scikit-Learn

Containerization

- Docker
- Docker Compose

Documentation

- Swagger/OpenAPI

Version Control

- Git
- GitHub

---

## Hardware Requirements

Minimum

Processor

Intel Core i3

RAM

4 GB

Storage

20 GB

Recommended

Intel Core i5 or above

8 GB RAM

SSD Storage

Internet Connection for AI Features