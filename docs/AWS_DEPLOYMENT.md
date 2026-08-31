# AWS Cloud Deployment & Architecture Guide

This document outlines the production cloud deployment setup for the **AI Material Management System** on Amazon Web Services (AWS) using **AWS App Runner / Elastic Container Service (ECS)**, **Amazon RDS (PostgreSQL)**, and **AWS S3 / CloudFront**.

---

## 🏗️ Architecture Overview

```
+-------------------------------------------------------------------+
|                        AWS Cloud Platform                         |
|                                                                   |
|  +------------------------+        +---------------------------+  |
|  |  AWS CloudFront / S3   | <----> |   AWS App Runner / ECS    |  |
|  |  (Frontend UI Hosting)  |        | (FastAPI Docker Backend)  |  |
|  +------------------------+        +---------------------------+  |
|                                                  |                |
|                                                  v                |
|                                    +---------------------------+  |
|                                    |  AWS RDS (PostgreSQL 15)  |  |
|                                    |  (Managed Database)       |  |
|                                    +---------------------------+  |
+-------------------------------------------------------------------+
```

---

## 🚀 Step-by-Step Deployment Instructions

### 1. Provision Amazon RDS (PostgreSQL Database)
- **Engine**: PostgreSQL 15.x
- **Instance Type**: `db.t3.micro` (Free Tier Eligible)
- **Database Name**: `ai_material_management`
- **Master Username**: `postgres`
- **Security Group**: Allow Inbound TCP on Port `5432` from App Runner / ECS security group.

### 2. Build & Push Docker Image to Amazon ECR
```bash
# Authenticate Docker to ECR registry
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com

# Build the FastAPI container image
docker build -t ai-material-backend ./backend

# Tag and push image
docker tag ai-material-backend:latest <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/ai-material-backend:latest
docker push <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/ai-material-backend:latest
```

### 3. Deploy Backend Container on AWS App Runner
- Navigate to **AWS App Runner** console.
- Choose **Container Image Repository** -> Select `ai-material-backend:latest` from ECR.
- Configure Environment Variables:
  - `DATABASE_URL` = `postgresql://postgres:YOUR_PASSWORD@your-rds-endpoint.amazonaws.com:5432/ai_material_management`
  - `SECRET_KEY` = `production-jwt-secret-key-32-chars`
  - `ALGORITHM` = `HS256`
- Set Port to `8000`.

### 4. Deploy Frontend Static Web App
- Upload all files from `/frontend` to **AWS S3** bucket (e.g. `ai-material-frontend-bucket`).
- Enable **Static Website Hosting**.
- Attach **Amazon CloudFront CDN** distribution for HTTPS SSL encryption and low latency.
- Update `API_BASE` in `frontend/js/app.js` to point to the live App Runner URL:
  ```js
  const API_BASE = "https://<app-runner-id>.us-east-1.awsapprunner.com/api";
  ```

---

## 🌍 Production Live URL Formats

- **Frontend Application URL**: `https://d123456789.cloudfront.net` (or `http://ai-material-frontend.s3-website-us-east-1.amazonaws.com`)
- **Backend Swagger API Docs**: `https://<app-runner-id>.us-east-1.awsapprunner.com/docs`
- **Health Check Endpoint**: `https://<app-runner-id>.us-east-1.awsapprunner.com/api/dashboard`
