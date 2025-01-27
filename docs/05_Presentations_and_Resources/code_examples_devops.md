# **Overview: Code Examples for DevOps Practices**

---

### **Table of Contents**

- [**1. Introduction**](#1-introduction)
- [**2. Version Control**](#2-version-control)
- [**3. Continuous Integration (CI)**](#3-continuous-integration-ci)
- [**4. Infrastructure as Code (IaC)**](#4-infrastructure-as-code-iac)
- [**5. Containerization and Orchestration**](#5-containerization-and-orchestration)
- [**6. Monitoring and Alerts**](#6-monitoring-and-alerts)

---

## **1. Introduction**

This document provides code examples for implementing various DevOps practices. These examples demonstrate the use of common tools and frameworks, helping you get started with version control, CI/CD pipelines, infrastructure automation, container orchestration, and monitoring systems.

> **Note:** Modify these examples to suit your specific project requirements.

---

## **2. Version Control**

Version control ensures code changes are tracked, enabling collaboration among teams.

### **2.1 Git Commands**

```bash
# Initialize a Git repository
git init

# Clone a repository
git clone https://github.com/example/repo.git

# Add changes to staging
git add .

# Commit changes
git commit -m "Initial commit"

# Push changes to remote repository
git push origin main

# Create a new branch
git branch feature-branch

# Switch to a branch
git checkout feature-branch

# Merge a branch into main
git merge feature-branch
```

> **Tip:** Use descriptive commit messages to make your version history easier to understand.

---

## **3. Continuous Integration (CI)**

CI automates testing and building of code whenever changes are made.

### **3.1 GitHub Actions Workflow Example**

```yaml
name: CI Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'

      - run: npm install
      - run: npm test
      - run: npm run build
```

### **3.2 Jenkins Pipeline Example**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'npm run deploy'
            }
        }
    }
}
```

---

## **4. Infrastructure as Code (IaC)**

IaC allows infrastructure to be managed using code, ensuring consistency and repeatability.

### **4.1 Terraform Script for Azure**

```hcl
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_virtual_network" "example" {
  name                = "example-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
}
```

### **4.2 Ansible Playbook Example**

```yaml
- hosts: web_servers
  become: yes
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present

    - name: Start Nginx
      service:
        name: nginx
        state: started
```

---

## **5. Containerization and Orchestration**

### **5.1 Dockerfile Example**

```dockerfile
# Use Node.js as base image
FROM node:14

# Set working directory
WORKDIR /app

# Copy application files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy remaining application files
COPY . .

# Expose application port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
```

### **5.2 Kubernetes Deployment YAML**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: example-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: example
  template:
    metadata:
      labels:
        app: example
    spec:
      containers:
      - name: example-container
        image: example-image:v1
        ports:
        - containerPort: 80
```

---

## **6. Monitoring and Alerts**

### **6.1 Prometheus Alert Rule**

```yaml
groups:
  - name: example-alerts
    rules:
      - alert: HighCPUUsage
        expr: node_cpu_seconds_total > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage detected"
          description: "CPU usage is above 80% for the past 5 minutes."
```

### **6.2 Grafana Dashboard JSON**

```json
{
  "dashboard": {
    "title": "Example Dashboard",
    "panels": [
      {
        "type": "graph",
        "title": "CPU Usage",
        "targets": [
          {
            "expr": "node_cpu_seconds_total",
            "legendFormat": "{{cpu}}"
          }
        ]
      }
    ]
  }
}
```

---
### Next step:
- [guide_setting_up_redis](guide_setting_up_redis.md)