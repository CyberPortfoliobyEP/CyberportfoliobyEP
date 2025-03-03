# Lab 16 - Sentinel: Creating Rules

## Table of Contents
1. [Introduction](#1-introduction)
2. [Implementation](#2-implementation)
   - [Configuring Fusion Rules in Microsoft Sentinel](#21-configuring-fusion-rules-in-microsoft-sentinel)
   - [Creating a Microsoft Incident Creation Rule](#22-creating-a-microsoft-incident-creation-rule)
   - [Installing an Analytics Rule from Content Hub](#23-installing-an-analytics-rule-from-content-hub)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

## 1. Introduction

Microsoft Sentinel provides a variety of **analytics rules** to detect and respond to threats in real time. These rules automate **incident detection, alert correlation, and response actions**.

This lab covers:
- **Fusion Rules**: Machine-learning-driven detection of **multi-stage attacks**.
- **Incident Creation Rules**: Custom rules for **Microsoft Defender integration**.
- **Content Hub Rules**: Prebuilt analytics rules based on **MITRE ATT&CK techniques**.

> **Screenshot: Sentinel Fusion Rule**  
> ![Fusion Rule](https://i.imgur.com/IQCTDB8.png)

## 2. Implementation

### 2.1 Configuring Fusion Rules in Microsoft Sentinel

#### **What are Fusion Rules?**
Fusion Rules use **AI and machine learning** to **correlate alerts** from multiple Microsoft security products (Defender, Entra ID, etc.), detecting **multi-stage attacks** that span different environments.

#### **Steps to Configure Fusion Rules**
1. Navigate to **Microsoft Sentinel** → **Analytics**.
2. Locate the **"Advanced Multistage Attack Detection"** Fusion Rule.
3. Click **Edit** to view its settings.

#### **Key Configuration Options**
- **Enable or Disable Products**:  
  - Example: **Disable Microsoft Defender for IoT** if no IoT devices are used.
- **Adjust Alert Sensitivity**:  
  - Options: **Low, Medium, High** (default: **High**).
- **Configure Automated Response**:  
  - Example: Assign **SOC Level 2** for high-severity incidents.

#### **Creating an Automation Rule**
1. Navigate to **Automated Response** within the Fusion Rule.
2. Click **Create New Automation Rule**.
3. Configure the rule:
   - **Name**: `Assign SOC 2`
   - **Trigger**: When incident is created.
   - **Condition**: Security severity **equals High**.
   - **Action**: Assign **SOC Level 2 Analyst** as owner.
   - **Order**: `1` (highest priority).

> **Screenshot: Custom Automation Rule**  
> ![Custom Rule](https://i.imgur.com/w17a6gK.png)

> **Microsoft Documentation:**  
> [Configure Fusion Rules in Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/configure-fusion-rules)

---

### 2.2 Creating a Microsoft Incident Creation Rule

#### **What is a Microsoft Incident Creation Rule?**
This rule **automates incident generation** based on security alerts from **Microsoft Defender services**.

#### **Steps to Create the Rule**
1. Navigate to **Sentinel → Analytics**.
2. Click **Create** → **Microsoft Incident Creation Rule**.
3. Configure the rule:
   - **Name**: `Assignment`
   - **Microsoft Security Service**: `Defender for Cloud`
   - **Severity**: `Any`
4. Under **Automated Response**, apply the same **SOC 2 Assignment Rule** from the Fusion Rule.

#### **Key Differences from Fusion Rules**
| Feature | Fusion Rule | Incident Creation Rule |
|---------|------------|-----------------------|
| **Detection Method** | AI-based correlation | Single-source alerts |
| **Supported Sources** | Multiple Microsoft services | One Defender service per rule |
| **Customization** | Limited (Microsoft-managed) | Fully customizable |

> **Screenshot: Security Rule in Sentinel**  
> ![Security Rule](https://i.imgur.com/VgthxwP.png)

> **Microsoft Documentation:**  
> [Create Microsoft Incident Creation Rules](https://learn.microsoft.com/en-us/azure/sentinel/incidents)

---

### 2.3 Installing an Analytics Rule from Content Hub

#### **What is Sentinel Content Hub?**
Content Hub provides **prebuilt analytics rules** for **third-party and Microsoft security products**.

#### **Steps to Install an Analytics Rule**
1. Open **Sentinel** → **Content Hub**.
2. Apply **Filters**:
   - **Content Type**: Analytics Rule.
   - **Support**: Microsoft, Community (exclude Partner).
3. Select **"High Count of Failed Logons by a User"**.
4. Click **Install**.

> **Screenshot: Content Hub Filtered View**  
> ![AR Content Hub](https://i.imgur.com/l1RBgIj.png)

#### **Configuring the Installed Rule**
1. Navigate to **Sentinel** → **Analytics**.
2. Open **Rule Templates** → **Installed Rule**.
3. Adjust settings:
   - **MITRE ATT&CK Mapping**: `T1110 – Brute Force`.
   - **Rule Period**: `Last 1 hour`.
   - **Rule Frequency**: `Run query every 30 minutes`.

> **Screenshot: Review + Create Rule**  
> ![Review + Create](https://i.imgur.com/6LIMDYG.png)

> **Microsoft Documentation:**  
> [Microsoft Sentinel Content Hub](https://learn.microsoft.com/en-us/azure/sentinel/content-hub)

---

## 3. Impact of Deployment

### **Key Benefits of Sentinel Rules**
- **Fusion Rule**: Detects **multi-stage attacks** across services.
- **Incident Creation Rule**: Ensures **automated triaging** of Defender alerts.
- **Content Hub Rules**: Provides **ready-to-use analytics** aligned with **MITRE ATT&CK**.

> **Example Scenario:**  
> A brute-force attack is detected by the **High Count of Failed Logons Rule** → Fusion correlates it with **other suspicious activities** → **SOC 2 is alerted automatically**.

---

## 4. Conclusion

This lab demonstrated **how to configure and deploy analytics rules** in **Microsoft Sentinel**, covering:
- **Fusion Rule Configuration**.
- **Incident Creation Rule for Microsoft Defender**.
- **Installing & Customizing Prebuilt Rules from Content Hub**.

### **Next Steps**
- Implement **custom Kusto queries** for advanced threat hunting.
- Configure **Sentinel Playbooks** for automated remediation.
- Monitor **rule performance** using **Sentinel logs**.

---

## 5. References

- [Configure Fusion Rules in Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/configure-fusion-rules)
- [Create Microsoft Incident Creation Rules](https://learn.microsoft.com/en-us/azure/sentinel/incidents)
- [Microsoft Sentinel Content Hub](https://learn.microsoft.com/en-us/azure/sentinel/content-hub)