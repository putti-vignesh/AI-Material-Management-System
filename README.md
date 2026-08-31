# AI Material Management System

## Overview
A full-stack capstone project for AI-assisted material management, procurement planning, inventory tracking, and reporting.

## Tech Stack
- Frontend: HTML5, CSS3, Bootstrap 5, JavaScript, Chart.js
- Backend: Python 3.12+, FastAPI, SQLAlchemy, Pydantic, Uvicorn
- Database: MySQL / SQLite fallback
- Authentication: JWT + bcrypt`
- AI: Gemini API + scikit-learn forecasting

## Project Structure
- backend/app: FastAPI application and API routers
- frontend: dashboard and management pages
- database/schema.sql: SQL schema

## Run Locally
1. Install Python dependencies:
   - pip install -r backend/requirements.txt
2. Start the backend:
   - cd backend
   - uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
3. Open frontend pages directly in the browser or use a simple static server.

## Default Login
- Username: admin
- Password: admin123

## API Endpoints
- /api/login
- /api/materials
- /api/suppliers
- /api/warehouses
- /api/purchase-requests
- /api/inventory
- /api/reports
- /api/chatbot
- /api/forecast
