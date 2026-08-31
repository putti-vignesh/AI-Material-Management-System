# 9. Use Case Descriptions

## 9.1 User Login

### Actor
Administrator

### Description
The administrator logs into the system using a username and password.

### Precondition
The user account must exist.

### Main Flow

1. User enters username and password.
2. System validates credentials.
3. JWT access token is generated.
4. User is redirected to the dashboard.

### Postcondition

User is authenticated and authorized to access protected APIs.

---

## 9.2 Material Management

### Actor

Store Manager

### Description

Manage inventory materials.

### Main Flow

1. Add new material.
2. Update material information.
3. Delete obsolete material.
4. Search material.
5. View inventory.

---

## 9.3 Purchase Request

### Actor

Department Head

### Main Flow

1. Select required material.
2. Enter quantity.
3. Select priority.
4. Submit purchase request.
5. Procurement team reviews request.

---

## 9.4 Purchase Order

### Actor

Procurement Officer

### Main Flow

1. Review purchase request.
2. Select supplier.
3. Generate purchase order.
4. Send PO to supplier.

---

## 9.5 Goods Receiving (GRN)

### Actor

Warehouse Staff

### Main Flow

1. Receive material.
2. Enter batch information.
3. Record received quantity.
4. Generate GRN.
5. Update inventory.

---

## 9.6 Quality Inspection

### Actor

Quality Inspector

### Main Flow

1. Inspect received material.
2. Accept quantity.
3. Reject damaged quantity.
4. Record inspection remarks.

---

## 9.7 Stock Transfer

### Actor

Store Manager

### Main Flow

1. Select source warehouse.
2. Select destination warehouse.
3. Select material.
4. Enter transfer quantity.
5. Confirm transfer.

---

## 9.8 AI Procurement Assistant

### Actor

Procurement Officer

### Main Flow

1. Open AI Dashboard.
2. Enter supplier/material.
3. Request AI prediction.
4. View supplier recommendation.
5. View lead-time prediction.
6. View substitute materials.
7. View wastage analysis.

---

## 9.9 AI Chatbot

### Actor

Any Authenticated User

### Main Flow

1. Enter natural language query.
2. System retrieves inventory information.
3. Google Gemini processes the prompt.
4. Chatbot returns a natural language answer.

---

# 10. Assumptions

The following assumptions were made during system development.

- PostgreSQL database is available.
- Internet connection is available for AI features.
- Docker Engine is installed.
- Users access the application using modern web browsers.
- Google Gemini API key is configured.
- All users have valid login credentials.
- Warehouse inventory data is maintained correctly.
- Authorized users follow organization inventory policies.

---

# 11. Constraints

The following limitations apply.

- AI chatbot requires internet connectivity.
- Gemini API usage depends on available quota.
- The application currently supports a single organization.
- Mobile application is not implemented.
- Multi-tenant architecture is not supported.
- Role hierarchy is limited to implemented user roles.
- AI recommendations depend on available inventory data.

---

# 12. Testing Requirements

The project has been tested using the following methods.

## Unit Testing

- Authentication
- CRUD Operations
- AI Services
- Database Models

---

## API Testing

Verified using Swagger OpenAPI.

Tested APIs include

- Login
- Dashboard
- Materials
- Suppliers
- Warehouses
- Purchase Requests
- Purchase Orders
- Goods Receiving
- Quality Inspection
- Stock Transfers
- Scrap Management
- Material Returns
- AI APIs

---

## Database Testing

Verified

- Insert
- Update
- Delete
- Foreign Key Relationships
- Data Retrieval

---

## Authentication Testing

Verified

- JWT Token Generation
- Protected APIs
- Unauthorized Access
- Role Validation

---

## AI Testing

Verified

- Lead Time Prediction
- Supplier Recommendation
- Material Substitute Suggestion
- Wastage Analysis
- AI Chatbot using Google Gemini

---

## Docker Testing

Verified

- Docker Image Build
- Docker Compose
- Backend Container
- PostgreSQL Container
- Container Communication

---

# 13. Deployment Requirements

## Local Deployment

Components

- FastAPI Backend
- PostgreSQL Database
- HTML/CSS/JavaScript Frontend

Containerization

- Docker
- Docker Compose

---

## Cloud Deployment (Future)

Recommended Platform

AWS

Possible Services

- Amazon EC2
- Amazon ECS
- Amazon RDS PostgreSQL
- Amazon S3
- CloudWatch
- GitHub Actions CI/CD

---

# 14. Future Enhancements

The following features can be added in future releases.

- Mobile Application
- Progressive Web App (PWA)
- Email Notifications
- SMS Alerts
- OCR-based Invoice Processing
- Automatic Purchase Order Approval
- Multi-level Approval Workflow
- Predictive Material Demand Forecasting using Machine Learning
- Real-time IoT Inventory Monitoring
- Barcode and QR Code Integration
- RFID Inventory Tracking
- Multi-Organization (Multi-Tenant) Support
- Advanced Analytics Dashboard
- AI Report Generation
- Voice-enabled AI Assistant
- Vendor Performance Analytics
- Cloud-native Kubernetes Deployment

---

# 15. References

1. FastAPI Documentation
   https://fastapi.tiangolo.com/

2. PostgreSQL Documentation
   https://www.postgresql.org/docs/

3. SQLAlchemy Documentation
   https://docs.sqlalchemy.org/

4. Docker Documentation
   https://docs.docker.com/

5. Google Gemini API Documentation
   https://ai.google.dev/

6. Bootstrap Documentation
   https://getbootstrap.com/

7. JWT Documentation
   https://jwt.io/

8. Python Documentation
   https://docs.python.org/

---

# 16. Conclusion

The AI-Enabled Material Management System provides a complete solution for inventory control, procurement management, warehouse operations, quality inspections, and AI-assisted decision making.

The project combines a responsive web interface, FastAPI backend, PostgreSQL database, JWT authentication, Docker containerization, and Google Gemini AI to deliver an intelligent and scalable material management platform.

The implemented modules automate inventory tracking, supplier management, purchase workflows, stock monitoring, warehouse management, and AI-powered procurement recommendations. The architecture is modular, maintainable, and suitable for future deployment on cloud platforms such as AWS.

This project demonstrates the practical integration of Artificial Intelligence with modern full-stack software engineering practices and provides a strong foundation for enterprise-level inventory management systems.