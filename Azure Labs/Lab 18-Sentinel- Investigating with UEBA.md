# Lab 18 - Sentinel: Investigating with UEBA

## Table of Contents
1. [Introduction](#1-introduction)
2. [Implementation](#2-implementation)
   - [Enabling UEBA in Microsoft Sentinel](#21-enabling-ueba-in-microsoft-sentinel)
   - [Investigating User Activities with UEBA](#22-investigating-user-activities-with-ueba)
   - [Analyzing Anomalies and Suspicious Behaviors](#23-analyzing-anomalies-and-suspicious-behaviors)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

## 1. Introduction

**User and Entity Behavior Analytics (UEBA)** in **Microsoft Sentinel** enables security teams to detect **anomalies, suspicious activities, and potential threats** by analyzing behavioral patterns across users and entities.

### **Key Benefits of UEBA**
- **Detects anomalous user behaviors** based on historical data.
- **Identifies compromised accounts** by correlating security events.
- **Improves security investigation efficiency** by centralizing behavioral insights.
- **Supports advanced threat detection** with machine learning-driven analytics.

> **Example Scenario:**  
> *A user logs in from two geographically distant locations (Germany and the USA) within 10 minutes. UEBA flags this as an "impossible travel" anomaly, triggering a security alert.*

> **Screenshot: UEBA Architecture**  
> ![UEBA Image](https://i.imgur.com/7Um5c6I.png)  
> *Source: Microsoft*

> **Microsoft Documentation:**  
> [Microsoft Sentinel UEBA Overview](https://learn.microsoft.com/en-us/azure/sentinel/identify-threats-with-entity-behavior-analytics)

---

## 2. Implementation

### 2.1 Enabling UEBA in Microsoft Sentinel

UEBA is **license-free** and can be enabled by **Global Administrators or Security Administrators**.

#### **Steps to Enable UEBA**
1. Open **Microsoft Sentinel** in **Azure Portal**.
2. Navigate to **Entity Behavior → Entity Behavior Settings**.
3. Click **Enable UEBA**.
4. Select the desired **data sources**:
   - **Microsoft Entra ID** (formerly Azure AD)
   - **Audit Logs**
   - **Security Events**
   - **Sign-in Logs**
5. Click **Apply** to start synchronization.

> **Screenshot: Enabling UEBA**  
> ![Enabling UEBA](https://i.imgur.com/uB1SyfK.png)

### **Key Considerations**
- **Permissions Required**:  
  - Only **Global Administrators** or **Security Administrators** can enable UEBA.
- **Granular Data Selection**:  
  - Organizations can choose specific **log sources** for UEBA insights.
- **Sync Process**:  
  - Once enabled, the system **synchronizes** the selected logs and starts **behavioral analysis**.

---

### 2.2 Investigating User Activities with UEBA

Once UEBA is enabled, administrators can **search for specific users** and analyze their activities.

#### **Steps to Investigate a User**
1. Open **Microsoft Sentinel**.
2. Navigate to **Entity Behavior**.
3. Search for a specific **user** (e.g., `admin@company.com`).
4. View **detailed behavioral insights**.

#### **Example: Reviewing User Timeline**
- The **timeline** provides a structured view of user activities.
- In this example, UEBA detected **no anomalies** but logged:
  - A **SharePoint document** was shared externally.
  - A **new sign-in event** from an unusual location.
  - Interaction with **sensitive resources**.

> **Screenshot: Detailed User Behavior Analysis**  
> ![Detailed Behavior](https://i.imgur.com/uPTPAVy.png)

### **How Security Teams Use This Data**
- **Monitor high-risk users** for potential insider threats.
- **Identify patterns in user activity** that may indicate compromise.
- **Validate security events** by correlating with behavioral insights.

---

### 2.3 Analyzing Anomalies and Suspicious Behaviors

UEBA provides **real-time detection** of unusual activities.

#### **Example: Impossible Travel Detection**
- A user logs in from **New York at 9:00 AM**.
- The same user logs in from **Germany at 9:10 AM**.
- UEBA **flags this activity** as an **impossible travel anomaly**.

#### **Scoring System**
UEBA assigns **risk scores (0-10)** to anomalies:
- **0-3**: Low Risk – Likely normal user activity.
- **4-7**: Medium Risk – Requires manual verification.
- **8-10**: High Risk – Immediate security action required.

#### **Correlation with MITRE ATT&CK Framework**
- UEBA correlates detected anomalies with **MITRE ATT&CK tactics**.
- Example:  
  - **T1078**: "Valid Accounts" → Detects compromised user credentials.
  - **T1133**: "External Remote Services" → Flags unusual external access.

> **Microsoft Documentation:**  
> [UEBA Threat Detection Use Cases](https://learn.microsoft.com/en-us/azure/sentinel/identify-threats-with-entity-behavior-analytics)

---

## 3. Impact of Deployment

### **Security Benefits of UEBA**
- **Proactive Threat Detection**: Detects **behavioral anomalies** before a security breach occurs.
- **Enhanced Investigation Capabilities**: Provides **detailed user activity logs** for forensic analysis.
- **Automated Anomaly Scoring**: Assigns **risk scores** to prioritize security incidents.
- **Integration with Microsoft Defender**: Correlates **Defender alerts** with behavioral insights.

> **Example Scenario:**  
> A **dormant admin account** suddenly logs in after 150 days and accesses **sensitive SharePoint files**.  
> UEBA **detects the anomaly**, assigns a **high-risk score**, and triggers a **security alert**.

---

## 4. Conclusion

This lab demonstrated how to **enable and use UEBA in Microsoft Sentinel**, covering:
- **Configuration and activation of UEBA settings**.
- **Investigating user activities and security insights**.
- **Detecting anomalies and assigning risk scores**.

### **Next Steps**
- Configure **custom UEBA alerts** for high-risk activities.
- Integrate UEBA with **Sentinel Playbooks** for automated remediation.
- Use **Kusto queries** to enhance UEBA data analysis.

---

## 5. References

- [Microsoft Sentinel UEBA Overview](https://learn.microsoft.com/en-us/azure/sentinel/identify-threats-with-entity-behavior-analytics)
- [UEBA Threat Detection Use Cases](https://learn.microsoft.com/en-us/azure/sentinel/identify-threats-with-entity-behavior-analytics)
- [Microsoft Defender & UEBA Integration](https://learn.microsoft.com/en-us/azure/sentinel/threat-intelligence-integration)