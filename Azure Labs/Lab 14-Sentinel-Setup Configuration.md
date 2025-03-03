# Lab 14-Sentinel: Setup Configuration

## Table of Contents
1. [Introduction](#1-introduction)
2. [Implementation](#2-implementation)
   - [Understanding Microsoft Sentinel](#21-understanding-microsoft-sentinel)
   - [Setting Up Log Analytics Workspace](#22-setting-up-log-analytics-workspace)
   - [Deploying Microsoft Sentinel](#23-deploying-microsoft-sentinel)
   - [Roles and Permissions](#24-roles-and-permissions)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

---

## 1. Introduction

**Microsoft Sentinel** is a **cloud-native SIEM (Security Information and Event Management) and SOAR (Security Orchestration Automated Response) solution** that enables security monitoring, detection, and automated threat response.

### **Key Features of Microsoft Sentinel**
- **Cloud-native & AI-powered**: Integrates with over **300 security partners**.
- **Automated threat response** using **playbooks** and **Logic Apps**.
- **Centralized logging and monitoring** via **Log Analytics Workspace**.
- **Scalable pricing** based on **data ingestion (Pay-as-you-go model)**.

> **Screenshot: Microsoft Sentinel Topology**  
> ![Sentinel Topology](https://i.imgur.com/IRDzcOK.png)  
> *Source: azure.com*

### **Cost Considerations**
Microsoft Sentinel follows a **Pay-as-you-go model**, with pricing based on **ingested data per GB**.  
For example:
- **$4.30 per GB (West Europe region)**
- **100GB/day ingestion = $430/day**
- **Free trial includes 10GB/day for 30 days**

> **Microsoft Documentation:**  
> [Microsoft Sentinel Pricing](https://learn.microsoft.com/en-us/azure/sentinel/pricing)

---

## 2. Implementation

### 2.1 Understanding Microsoft Sentinel

Before deployment, it is important to understand the core Sentinel components:

| Component | Description |
|-----------|-------------|
| **Log Analytics Workspace** | Stores all ingested logs and security data. |
| **Connectors** | Integrate security data sources (e.g., Microsoft Defender, Syslog). |
| **Workbooks** | Dashboards for visualizing security events. |
| **Analytics Rules** | Define detection criteria for threats. |
| **Automation (SOAR)** | Playbooks using Logic Apps for automatic responses. |

> **Microsoft Documentation:**  
> [What is Microsoft Sentinel?](https://learn.microsoft.com/en-us/azure/sentinel/overview?tabs=azure-portal)

---

### 2.2 Setting Up Log Analytics Workspace

A **Log Analytics Workspace** is required for Sentinel to **store and analyze security data**.

#### **Steps to Create a Log Analytics Workspace**
1. Open **Azure Portal** → **All Services** → **Log Analytics Workspaces**.
2. Click **Create** and configure:
   - **Resource Group:** `Laboratorium`
   - **Workspace Name:** `Laboratorium-Logs`
   - **Region:** `West Europe`
   - **Pricing Tier:** `Pay-as-you-go`
3. Click **Review + Create** → **Create**.

> **Screenshot: Log Analytics Workspace**  
> ![Log Analytics Workspace](https://i.imgur.com/M7yiYyM.png)

### **Why is Log Analytics Important?**
- **Stores all Sentinel logs and detections.**
- **Enables advanced security analytics and correlation.**
- **Required for enabling Microsoft Sentinel.**

> **Microsoft Documentation:**  
> [Log Analytics Workspace Overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview)

---

### 2.3 Deploying Microsoft Sentinel

Once the **Log Analytics Workspace** is created, Sentinel can be deployed.

#### **Steps to Enable Microsoft Sentinel**
1. Open **Azure Portal** → **Search for Sentinel**.
2. Click **Create** and **Select an existing Log Analytics Workspace** (`Laboratorium-Logs`).
3. Click **Add Microsoft Sentinel** to complete the setup.

> **Screenshot: Sentinel Deployment**  
> ![Sentinel Ready](https://i.imgur.com/ZfPsvOm.png)

### **Free Trial & Data Ingestion**
- Microsoft Sentinel provides a **30-day free trial**.
- Includes **10GB/day free ingestion**.
- **Beyond 10GB/day, standard billing applies**.

> **Microsoft Documentation:**  
> [Sentinel Prerequisites](https://learn.microsoft.com/en-us/azure/sentinel/prerequisites)

---

### 2.4 Roles and Permissions

Microsoft Sentinel includes several **built-in roles** that define access levels.

| Role | Permissions |
|-----------|-------------|
| **Microsoft Sentinel Reader** | View incidents, data, and dashboards (no modifications). |
| **Microsoft Sentinel Responder** | Manage incidents but cannot edit rules. |
| **Microsoft Sentinel Contributor** | Edit analytics rules, workbooks, and data connectors. |
| **Microsoft Sentinel Playbook Operator** | Run playbooks for automated response (SOAR). |
| **Microsoft Sentinel Automation Contributor** | Allows Sentinel to add playbooks to automation rules. |

> **Screenshot: Sentinel Roles and Permissions**  
> ![Roles, Permissions and Actions](https://i.imgur.com/eTOAnQ4.png)

### **Playbooks and Automated Response**
- **Sentinel playbooks** use **Azure Logic Apps** for automation.
- Assign **Sentinel Playbook Operator** to enable **SOAR actions**.
- Use **Logic App Contributor** role for **editing and managing playbooks**.

> **Microsoft Documentation:**  
> [Microsoft Sentinel Roles and Permissions](https://learn.microsoft.com/en-us/azure/sentinel/roles)

### **Admin Considerations**
- **Global Administrators & Owners** automatically inherit full Sentinel access.
- **Role assignments should follow the principle of least privilege.**

> **Note:** Since the user is a **Global Admin and Owner**, additional **role assignments are not required**.

---

## 3. Impact of Deployment

### **Security Benefits of Microsoft Sentinel**
- **Centralized Threat Monitoring**: Aggregates logs from multiple sources.
- **AI-Powered Detection**: Uses machine learning to detect security anomalies.
- **Automated Response**: Playbooks enable instant remediation of threats.
- **Scalable & Cost-Effective**: Flexible pricing based on data ingestion.

> **Example Scenario:**  
> If an attacker attempts to access **Azure resources**, Sentinel can **detect the anomaly**, trigger a **SOAR playbook**, and **block access automatically**.

---

## 4. Conclusion

This lab covered the **setup and configuration** of **Microsoft Sentinel** in Azure, including:
- **Creating a Log Analytics Workspace** (`Laboratorium-Logs`).
- **Deploying Sentinel and linking it to the workspace**.
- **Understanding Sentinel roles, permissions, and automation.**

### **Next Steps**
- Configure **data connectors** for integration with **Microsoft Defender & Syslog**.
- Define **custom analytics rules** to detect threats.
- Implement **playbooks for automated response**.

---

## 5. References

- [Microsoft Sentinel Overview](https://learn.microsoft.com/en-us/azure/sentinel/overview?tabs=azure-portal)
- [Microsoft Sentinel Prerequisites](https://learn.microsoft.com/en-us/azure/sentinel/prerequisites)
- [Log Analytics Workspace Overview](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview)
- [Microsoft Sentinel Roles and Permissions](https://learn.microsoft.com/en-us/azure/sentinel/roles)
- [Microsoft Sentinel Pricing](https://learn.microsoft.com/en-us/azure/sentinel/pricing)
- [Microsoft Sentinel Playbooks and Automation](https://learn.microsoft.com/en-us/azure/sentinel/playbooks)