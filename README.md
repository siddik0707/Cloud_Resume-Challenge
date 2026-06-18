# Cloud Resume Challenge

A fully serverless cloud resume website built on AWS as part of the Cloud Resume Challenge. This project demonstrates cloud infrastructure, serverless computing, API development, CI/CD automation, and frontend-backend integration using AWS services.

---

## 🌐 Live Website

**Live Demo:** https://d1ljkbb2nvzl2b.cloudfront.net/

> Note: The live website is hosted using AWS Free Tier eligible services. If the website becomes unavailable in the future, screenshots and architecture diagrams are provided below.

---

## 📖 Project Overview

This project hosts a personal resume website using AWS serverless services. It includes a real-time visitor counter powered by API Gateway, Lambda, and DynamoDB.

The primary objective of this project was to gain hands-on experience with:

* AWS Cloud Services
* Serverless Architecture
* IAM and Security
* API Development
* Infrastructure Troubleshooting
* CI/CD Automation
* Cloud Monitoring
* Frontend and Backend Integration

---

## 🏗️ Architecture

![Architecture Diagram](screenshots/architecture-diagram.png)

The architecture consists of:

1. Users access the resume website through Amazon CloudFront.
2. CloudFront serves static content stored in Amazon S3.
3. JavaScript on the webpage sends requests to API Gateway.
4. API Gateway invokes an AWS Lambda function.
5. Lambda updates and retrieves visitor count data from DynamoDB.
6. CloudWatch stores Lambda execution logs for monitoring and troubleshooting.

---

## 🚀 AWS Services Used

### Amazon S3

* Hosts the static resume website
* Stores website assets (HTML, CSS, JavaScript)

### Amazon CloudFront

* Global Content Delivery Network (CDN)
* Improves website performance through caching
* Provides HTTPS access

### Amazon API Gateway

* Exposes REST API endpoints
* Integrates frontend and backend services

### AWS Lambda

* Serverless compute service
* Processes visitor counter requests

### Amazon DynamoDB

* NoSQL database
* Stores visitor count data

### AWS IAM

* Manages roles and permissions
* Secures service interactions

### Amazon CloudWatch

* Stores Lambda logs
* Assists with monitoring and debugging

---

## ✨ Features

* Fully serverless architecture
* Static website hosting
* Global content delivery with CloudFront
* Real-time visitor counter
* REST API implementation
* DynamoDB integration
* Lambda backend processing
* CloudWatch monitoring
* CI/CD deployment pipeline using GitHub Actions

---

## 🔄 Visitor Counter Workflow

1. User opens the website.
2. JavaScript sends a request to API Gateway.
3. API Gateway invokes Lambda.
4. Lambda updates the visitor count in DynamoDB.
5. DynamoDB returns the updated value.
6. Lambda returns the response.
7. JavaScript updates the visitor count displayed on the webpage.

---

## ⚙️ CI/CD Pipeline

This project uses GitHub Actions for automated deployments.

### Deployment Workflow

```text
Developer Pushes Code
          ↓
GitHub Actions Workflow
          ↓
Authenticate with AWS
          ↓
Upload Website Files to S3
          ↓
Create CloudFront Invalidation
          ↓
Updated Website Available
```

### GitHub Actions Used

* actions/checkout
* aws-actions/configure-aws-credentials

### Benefits

* Automated deployments
* Faster updates
* Reduced manual work
* Consistent deployment process

---

## 🛠️ Skills Demonstrated

* AWS Cloud Architecture
* Serverless Computing
* REST API Development
* IAM and Security Management
* DynamoDB Integration
* Lambda Development
* CloudFront CDN Configuration
* S3 Static Website Hosting
* CloudWatch Monitoring
* Troubleshooting and Debugging
* CI/CD with GitHub Actions
* Infrastructure Documentation

---

## 📁 Repository Structure

```text
cloud-resume-challenge/
│
├── website/
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── screenshots/
│
├── .github/
│   └── workflows/
│
├── lambda.py
│
└── README.md
```

---

## 🔍 Challenges Faced

### IAM Permission Errors

Encountered:

```text
AccessDeniedException
```

Resolution:

* Updated Lambda execution role permissions
* Added required DynamoDB permissions

---

### DynamoDB Data Retrieval

Issues encountered:

* Partition key formatting
* Item retrieval failures
* JSON serialization errors

Resolution:

* Corrected table schema usage
* Implemented Decimal serialization handling

---

### API Gateway CORS Issues

Encountered browser errors:

```text
No 'Access-Control-Allow-Origin' header
```

Resolution:

* Enabled CORS in API Gateway
* Added OPTIONS method
* Returned required CORS headers

---

### CloudFront Caching

Updated website content was not immediately visible.

Resolution:

```text
/*
```

CloudFront invalidations were used to refresh cached content.

---

## 💻 Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### AWS Services

* Amazon S3
* Amazon CloudFront
* Amazon API Gateway
* AWS Lambda
* Amazon DynamoDB
* AWS IAM
* Amazon CloudWatch

### DevOps

* Git
* GitHub
* GitHub Actions

---

## 📸 Screenshots

### Resume Website

![Resume Screenshot](screenshots/resume.png)

### Architecture Diagram

![Architecture Diagram](screenshots/architecture-diagram.png)

### API Gateway

![API Gateway](screenshots/api-gateway.png)

### Lambda Function

![Lambda](screenshots/lambda.png)

### DynamoDB Table

![DynamoDB](screenshots/dynamodb.png)

### CloudFront Distribution

![CloudFront](screenshots/cloudfront.png)

---

## 🔮 Future Improvements

* Infrastructure as Code using Terraform
* Custom Domain with Route 53
* SSL Certificate Management with ACM
* Automated Infrastructure Provisioning
* Multi-Environment Deployment (Dev/Prod)
* Monitoring Dashboards and Alerts

---

## 👤 Author

**Siddik Mulla**

GitHub: https://github.com/siddik0707

LinkedIn: https://www.linkedin.com/in/siddik-mulla-b9a692255/

---

## 📜 Acknowledgements

This project was built as part of the Cloud Resume Challenge, a hands-on project designed to develop practical cloud engineering skills through real-world implementation.
