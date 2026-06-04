# AWS Cost Optimization Platform

A full-stack cloud cost optimization platform that analyzes AWS resources, identifies cost-saving opportunities, and generates actionable recommendations through an interactive dashboard.

## Features

* AWS Cost Explorer Integration
* EC2 Resource Discovery
* CloudWatch CPU Utilization Analysis
* EBS Volume Analysis
* S3 Bucket Discovery
* Cost Optimization Recommendations
* AI-Powered Recommendation Support
* PDF Report Generation
* Interactive React Dashboard
* Docker Containerization
* GitHub Actions CI/CD Pipeline

---

## Architecture

```text
React Dashboard
       │
       ▼
FastAPI Backend
       │
       ▼
AWS Services
├── Cost Explorer
├── EC2
├── CloudWatch
├── EBS
└── S3
```

---

## Tech Stack

### Frontend

* React.js
* Axios
* Recharts
* Tailwind CSS

### Backend

* FastAPI
* Python
* Boto3
* ReportLab

### AWS Services

* AWS Cost Explorer
* Amazon EC2
* Amazon S3
* Amazon EBS
* Amazon CloudWatch

### DevOps

* Docker
* GitHub Actions
* Git

---

## Dashboard Features

### Cost Monitoring

* Monthly AWS cost tracking
* Resource utilization insights

### Resource Discovery

* EC2 instance inventory
* S3 bucket inventory
* Unattached EBS volume detection

### Optimization Recommendations

* Idle EC2 detection
* Storage optimization recommendations
* Potential monthly savings estimation

### Reporting

* Executive PDF report generation
* Optimization summary dashboard

---

## API Endpoints

| Endpoint           | Description                  |
| ------------------ | ---------------------------- |
| `/`                | Health Check                 |
| `/cost`            | AWS Cost Explorer Data       |
| `/ec2`             | EC2 Inventory                |
| `/ebs`             | EBS Volume Analysis          |
| `/s3`              | S3 Bucket Discovery          |
| `/recommendations` | Optimization Recommendations |
| `/report`          | Executive Report             |
| `/report/pdf`      | Download PDF Report          |

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/sayandeeydey06/aws-cost-optimization-platform
cd aws-cost-optimization-platform
```

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## Docker Setup

```bash
docker compose up --build
```

Frontend:

```text
http://localhost:5173
```

Backend:

```text
http://localhost:8000/docs
```

---

## CI/CD

GitHub Actions pipeline automatically:

* Builds Backend
* Builds Frontend
* Validates Docker Configuration
* Performs Continuous Integration Checks

Workflow File:

```text
.github/workflows/ci.yml
```

---

## Screenshots

### Dashboard

screenshots/dashboard.png

### Recommendations

screenshots/recommendation.png

### CI/CD PIPELINE

screenshots/githubAction.png

### PDF Report

screenshots/pdf-report.png

---

## Future Improvements

* Multi-Region AWS Scanning
* AWS Lambda Integration
* FinOps Analytics
* Advanced Cost Forecasting
* AI-Powered Optimization Insights
* CloudFront Deployment
* ECS/Fargate Deployment

---

## Resume Highlights

* Developed a full-stack AWS Cost Optimization Platform using React, FastAPI, and AWS APIs.
* Built automated cloud resource analysis and recommendation engine.
* Implemented Docker containerization and GitHub Actions CI/CD pipelines.
* Generated executive PDF reports and real-time dashboard analytics.
* Integrated AWS Cost Explorer, CloudWatch, EC2, S3, and EBS services.

---

## Author

Sayandeep Dey

Cloud Developer | AWS | DevOps | Full Stack Development
