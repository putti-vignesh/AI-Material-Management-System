# System Architecture Document
## Project 28: AI-Enabled Material Management System

---

## 1. High-Level Architecture Overview

The system follows a modern decoupled 3-tier architecture with an intelligent AI Micro-service Layer.

```
+------------------------------------------------------------------------------------------------+
|                                    PRESENTATION TIER                                           |
|------------------------------------------------------------------------------------------------|
| HTML5 | CSS3 | Bootstrap 5 | JavaScript | Chart.js | FontAwesome | Responsive Dashboard       |
| Login | Dashboard | Materials | Suppliers | Warehouses | Reports | AI Intelligence Suite      |
+------------------------------------------------------------------------------------------------+
                                             |
                                             |
                                   REST / JSON APIs (HTTP)
                                             |
                                             ▼
+------------------------------------------------------------------------------------------------+
|                                   APPLICATION TIER                                             |
|                                      FastAPI Backend                                           |
|------------------------------------------------------------------------------------------------|
| Authentication (JWT) | RBAC | Pydantic Validation | Swagger/OpenAPI | CRUD REST APIs          |
|-----------------------------------------------------------------------------------------------|
| Routers                                                                          Services      |
|-----------------------------------------------------------------------------------------------|
| Auth                 Materials                 Suppliers                     AI Assistant       |
| Warehouses           Purchase Requests         Purchase Orders               Forecast Engine     |
| Goods Receiving      Quality Inspection        Inventory                     Chatbot            |
| Stock Transfers      Material Returns          Scrap Management              Reports            |
+------------------------------------------------------------------------------------------------+
                     |                                               |
                     | SQLAlchemy ORM                                | AI Service Calls
                     ▼                                               ▼

+---------------------------------------------+     +--------------------------------------------+
|             PERSISTENCE TIER                |     |              AI ENGINE                      |
|---------------------------------------------|     |--------------------------------------------|
| PostgreSQL Database                         |     | Google Gemini LLM                          |
| SQLAlchemy ORM                              |     | Natural Language Chatbot                   |
| Materials                                   |     | Supplier Recommendation                    |
| Suppliers                                   |     | Lead Time Prediction                       |
| Warehouses                                  |     | Material Substitute Suggestion             |
| Purchase Requests                           |     | Wastage & Scrap Analysis                   |
| Purchase Orders                             |     | Inventory Query Assistant                  |
| Goods Receiving (GRN)                       |     +--------------------------------------------+
| Quality Inspection                          |
| Inventory Transactions                      |
| Material Returns                            |
| Scrap Management                            |
| Users                                       |
| Reports                                     |
+---------------------------------------------+

                                             |
                                             ▼

+------------------------------------------------------------------------------------------------+
|                                   DEPLOYMENT LAYER                                             |
|------------------------------------------------------------------------------------------------|
|  Backend : Docker Container (FastAPI)                                                          |
|  Database: Docker Container (PostgreSQL)                                                       |
|  Frontend: Static HTML/CSS/JS running in Browser (Live Server/localhost)                       |
|  Docker Compose manages Backend + PostgreSQL                                                   |
|  Deployment: AWS EC2 / ECS                                                                     |
+------------------------------------------------------------------------------------------------+

---

## 2. Component Breakdown

### 2.1 Frontend Presentation Tier
- Static HTML5 pages with modular JavaScript controllers.
- Asynchronous API communication via standardized `apiRequest()` helper with automated JWT bearer token attachment.
- Dynamic data rendering with HTML table DOM generation and Chart.js bar charts.

### 2.2 Backend Application Tier
- **FastAPI Framework**: Provides asynchronous web routing, automatic request/response serialization, and interactive Swagger documentation at `/docs`.
- **Authentication Engine**: Password hashing via `bcrypt` and JWT token issuance/verification via `PyJWT`.
- **Validation Layer**: Pydantic v2 data structure validation enforcing type safety and business logic constraints.

### 2.3 AI Intelligence Services
- **Scikit-Learn Forecast Model**: Performs linear regression on past consumption trends to predict future stock depletion timelines.
- **Supplier Recommendation & Lead-Time Predictor**: Scores suppliers based on historical fulfillment reliability and predicts delivery times in days.
- **Substitute Material Suggestion Engine**: Queries categories for in-stock alternatives during low-stock scenarios.
- **Google Gemini LLM Integration**: Formulates natural language answers to user queries regarding stock levels and procurement guidelines.

### 2.4 Persistence Tier
- **SQLAlchemy ORM**: Handles relational object mapping, session pooling, and transaction handling.
- **Relational Storage**: MySQL / PostgreSQL database supporting ACID transactions.
