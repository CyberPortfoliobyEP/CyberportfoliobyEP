# Lab 15 - Sentinel: Configuring Data Sources

## Table of Contents
1. [Introduction](#1-introduction)
2. [Implementation](#2-implementation)
   - [Understanding Microsoft Sentinel Data Collection](#21-understanding-microsoft-sentinel-data-collection)
   - [Deploying Microsoft Sentinel Training Lab](#22-deploying-microsoft-sentinel-training-lab)
   - [Installing Entra ID via Content Hub](#23-installing-entra-id-via-content-hub)
   - [Configuring Microsoft Defender XDR and Defender for Cloud](#24-configuring-microsoft-defender-xdr-and-defender-for-cloud)
   - [Setting Up Common Event Format (CEF) and Syslog](#25-setting-up-common-event-format-cef-and-syslog)
   - [Configuring Windows Security Events](#26-configuring-windows-security-events)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

---

## 1. Introduction

Microsoft Sentinel allows organizations to **collect security data at cloud scale** from various sources, including Microsoft services, third-party security solutions, and on-premises environments.

### **Key Benefits of Sentinel Data Collection**
- **Unified security monitoring** across cloud and on-premises resources.
- **Normalization of log formats** to enhance threat detection.
- **Integration with Microsoft Defender and other security solutions.**

> **Screenshot: Sentinel Data Sources**  
> ![Sentinel data sources](https://i.imgur.com/LRmaVkb.png)

---

## 2. Implementation

### 2.1 Understanding Microsoft Sentinel Data Collection

**Data connectors** are used to ingest logs from multiple sources into **Microsoft Sentinel**.

| Data Source | Purpose |
|------------|---------|
| **Azure Services (Defender, Entra ID, Activity Logs)** | Provides security logs from Azure services. |
| **Third-Party Security Tools (Cisco, Palo Alto, AWS, etc.)** | Connects external security solutions. |
| **Syslog & Common Event Format (CEF)** | Collects logs from Linux/Unix and network appliances. |
| **Windows Security Events** | Captures security logs from Windows machines. |

> **Microsoft Documentation:**  
> [Understanding Sentinel Data Connectors](https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources)

---

### 2.2 Deploying Microsoft Sentinel Training Lab

Microsoft provides a **training lab** that includes **pre-recorded security data** for testing Sentinel features.

#### **Steps to Deploy the Training Lab**
1. Open **Azure Portal** → **Content Hub**.
2. Search for **Microsoft Sentinel Training Lab** in **Marketplace**.
3. Click **Install** and associate it with:
   - **Resource Group**: `Laboratorium`
   - **Log Analytics Workspace**: `Laboratorium Logs`
4. Click **Review + Create**.

> **Screenshot: Review + Create Sentinel Training Lab**  
> ![Review + Create Sentinel Training Lab](https://i.imgur.com/xHB2FzO.png)

### **Benefits of the Training Lab**
- Provides **hands-on experience** with **Microsoft Sentinel features**.
- Includes **pre-ingested threat intelligence data** (no additional cost).
- Facilitates **learning security use cases** in Sentinel.

> **Microsoft Documentation:**  
> [Microsoft Sentinel Training Lab](https://github.com/Azure/Azure-Sentinel/tree/master/Solutions/Training/Azure-Sentinel-Training-Lab)

---

### 2.3 Installing Entra ID via Content Hub

**Entra ID (formerly Azure Active Directory)** enables the ingestion of **sign-in logs and identity protection alerts**.

#### **Steps to Install Entra ID in Sentinel**
1. Navigate to **Azure Portal** → **Content Hub**.
2. Search for **Entra ID** and click **Install**.
3. Connect to **Laboratorium Logs** workspace.

> **Screenshot: Sentinel Content Hub**  
> ![Sentinel Content Hub](https://i.imgur.com/WT4LmEQ.png)

### **Why Integrate Entra ID?**
- Provides visibility into **sign-in attempts and identity-based threats**.
- Enables **user-based analytics for security monitoring**.
- Integrates with **Conditional Access policies**.

---

### 2.4 Configuring Microsoft Defender XDR and Defender for Cloud

Microsoft Defender XDR and Defender for Cloud provide **threat intelligence and security alerts**.

#### **Steps to Enable Microsoft Defender XDR & Defender for Cloud**
1. Open **Azure Portal** → **Defender for Cloud**.
2. Navigate to **Security Alerts**.
3. Click **Generate Sample Alerts** to create test events.
4. Go to **Sentinel Content Hub**.
5. Search for **Microsoft Defender XDR** and **Defender for Cloud**.
6. Click **Install** to connect them to Sentinel.

> **Screenshot: Sample Alerts**  
> ![Sample Alerts](https://i.imgur.com/5F9A1Ai.png)

### **Differences Between Defender XDR & Defender for Cloud**
| Feature | Microsoft Defender XDR | Microsoft Defender for Cloud |
|---------|-----------------|--------------------|
| **Scope** | Endpoint, Office 365, Cloud Apps, Entra ID | Multi-cloud security posture management |
| **Threat Intelligence** | Advanced AI-based detection | Monitors misconfigurations in workloads |
| **Integration** | Security alerts & incidents | Risk-based recommendations |

> **Microsoft Documentation:**  
> [Microsoft Defender XDR Overview](https://learn.microsoft.com/en-us/microsoft-365/security/defender-xdr?view=o365-worldwide)

---

### 2.5 Setting Up Common Event Format (CEF) and Syslog

**CEF and Syslog** allow ingestion of security logs from **Linux-based systems and network appliances**.

#### **Steps to Install CEF & Syslog**
1. Open **Azure Portal** → **Content Hub**.
2. Search for **Syslog** and **Common Event Format**.
3. Click **Install**.

> **Screenshot: Syslog and CEF**  
> ![Syslog and CEF](https://i.imgur.com/yyrnESZ.png)

### **How Syslog & CEF Work**
- **Syslog**: Standardized log format for Linux/Unix systems.
- **CEF (Common Event Format)**: A normalized log format used in security devices.
- **Azure Monitor Agent (AMA)** is now required for Syslog ingestion.

> **Screenshot: Event Transfer Microsoft/Linux**  
> ![Event Transfer Microsoft/Linux](https://i.imgur.com/OCmMazq.png)

> **Microsoft Documentation:**  
> [Best Practices for CEF Collection](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/best-practices-for-common-event-format-cef-collection-in-azure-sentinel/969990)

---

### 2.6 Configuring Windows Security Events

Microsoft Sentinel can ingest **Windows Security Events** using the **AMA (Azure Monitor Agent)**.

#### **Steps to Enable Windows Security Event Collection**
1. Open **Azure Portal** → **Content Hub**.
2. Search for **Windows Security Events** and click **Install**.

> **Screenshot: Windows Security Events**  
> ![Windows Security Events](https://i.imgur.com/nTTUBrc.png)

### **Why Collect Windows Security Events?**
- Enables detection of **failed login attempts, privilege escalations, and malware execution**.
- **Correlates security logs with Sentinel analytics rules**.

> **Screenshot: Windows Security Event Topology**  
> ![WSE Topology](https://i.imgur.com/27QJa1V.png)

#### **Creating a Data Connection Rule**
1. Navigate to **Sentinel Workspace** → **Data Connectors**.
2. Select **Windows Security Events via AMA**.
3. Click **Create Data Connection Rule**.
4. Set:
   - **Rule Name:** `FFM-EPL1-Rule`
   - **Resource Group:** `Laboratorium`
   - **Event Collection:** `All Security Events`
5. Click **Review + Create**.

> **Screenshot: Review + Create Connector**  
> ![Review + Create Connector](https://i.imgur.com/UVMgmtI.png)

---

## 3. Impact of Deployment

### **Security Benefits of Data Collection**
- **Enhanced security visibility** across multiple data sources.
- **Automated detection of threats** using Sentinel analytics rules.
- **Improved forensic investigations** with enriched event logs.

---

## 4. Conclusion

This lab demonstrated the **integration of various data sources in Microsoft Sentinel**, including:
- **Azure services (Entra ID, Defender, Security Logs)**
- **Third-party sources (Syslog, CEF)**
- **Windows Security Events**

### **Next Steps**
- Configure **custom analytics rules** for threat detection.
- Implement **automated playbooks** to respond to alerts.

---

## 5. References

- [Microsoft Sentinel Data Connectors](https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources)
- [Microsoft Defender XDR Overview](https://learn.microsoft.com/en-us/microsoft-365/security/defender-xdr?view=o365-worldwide)
- [Best Practices for CEF Collection](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/best-practices-for-common-event-format-cef-collection-in-azure-sentinel/969990)