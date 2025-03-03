# Lab 19 - Sentinel: Connecting New deployed VM to Log analytics for Monitoring

## Table of Contents
1. [Introduction](#1-introduction)
2. [Implementation](#2-implementation)
   - [Verifying VM Connection to Log Analytics](#21-verifying-vm-connection-to-log-analytics)
   - [Installing and Configuring the Windows Security Events Connector](#22-installing-and-configuring-the-windows-security-events-connector)
   - [Verifying the Connection in Microsoft Sentinel](#23-verifying-the-connection-in-microsoft-sentinel)
   - [Generating Security Events for Analysis](#24-generating-security-events-for-analysis)
   - [Querying Logs in Sentinel](#25-querying-logs-in-sentinel)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

## 1. Introduction

In this lab, **Microsoft Sentinel** is used to **monitor and analyze security events from a connected virtual machine (VM)**.  
The main objectives are:
- **Verifying the VM's connection to Log Analytics**.
- **Installing the Windows Security Events data connector**.
- **Ensuring security events are ingested into Sentinel**.
- **Performing log analysis using Kusto Query Language (KQL)**.

> **Screenshot: VM not connected to Log Analytics**  
> ![VM not connected](https://i.imgur.com/f6fqHdi.png)

## 2. Implementation

### 2.1 Verifying VM Connection to Log Analytics

The **Log Analytics Workspace (LAW)** is used in Sentinel to store and analyze security logs.  
To verify if the VM is connected:

1. Navigate to **Azure Portal** → **Log Analytics Workspaces**.
2. Open the workspace **"Laboratorium Logs"**.
3. Click on **Virtual Machines**.
4. The VM **"FFM-EPL1"** appeared as **"Not Connected"**, confirming that it is not yet sending event logs.

> **Note:** A VM must be connected to Log Analytics for Sentinel to process security data.

---

### 2.2 Installing and Configuring the Windows Security Events Connector

To collect **Windows security logs** from the VM, the **Windows Security Events via AMA** connector is required.

#### **Steps to Install and Configure the Connector**
1. Open **Microsoft Sentinel** → **Content Hub**.
2. Install the **"Windows Security Events via AMA"** data connector.
3. Navigate to **Sentinel** → **Data Connectors**.
4. Open **Windows Security Events via AMA**.

#### **Prerequisites to Configure the Connector**
- **Workspace Data Sources Permissions:** Requires **read and write** access.
- **Enable Data Collection Rule (DCR):** A wizard will guide the setup.

> **Screenshot: Data Collection Rule Setup**  
> ![Data Collection Rule](https://i.imgur.com/N3UeS75.png)

#### **Linux Systems**
- For **Linux systems**, use **Common Event Format (CEF) via AMA**.
- Additional configuration is required using **Azure Arc**.

---

### 2.3 Verifying the Connection in Microsoft Sentinel

After installing the connector, the VM must be linked to Log Analytics.

#### **Steps to Connect the VM**
1. Navigate to **Sentinel** → **Workspace Data Sources**.
2. Select **Virtual Machines**.
3. Click on **FFM-EPL1** → **Connect**.
4. After **1 minute**, the VM showed **"Connected"**.

> **Screenshot: Successful Connection**  
> ![Connection Success](https://i.imgur.com/XUASLyf.png)

---

### 2.4 Generating Security Events for Analysis

To verify that the VM is **sending security events**, a **brute-force attack simulation** was conducted.

#### **Steps to Generate Failed Logins**
1. Attempted multiple **failed logins** via **Remote Desktop (RDP)**.
2. Used **incorrect passwords** to trigger security events.

> **Screenshot: Brute Force Login Attempts**  
> ![Brute Forcing](https://i.imgur.com/ZrEqdji.png)

---

### 2.5 Querying Logs in Sentinel

After generating security events, **Kusto Query Language (KQL)** was used to analyze logs.

#### **Query to Detect Failed Logins**
**Kusto**  
SecurityEvent  
| where EventID == 4625  

#### **Understanding the Query**
- **Event ID 4625**: Represents **failed login attempts**.
- **Source:** Microsoft Security Audit logs.

> **Microsoft Documentation:**  
> [Event ID 4625 - An Account Failed to Log On](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4625)

#### **Results in Sentinel**
The query **successfully returned results**, confirming:
- **VM is connected to Sentinel**.
- **Windows Security Event logs are ingested properly**.
- **Failed login attempts were detected**.

> **Screenshot: Query Results in Sentinel**  
> ![Sentinel Results](https://i.imgur.com/SD4K95F.png)

---

## 3. Impact of Deployment

### **Security Benefits of Log Ingestion in Sentinel**
- **Monitors failed login attempts, brute-force attacks, and unauthorized access**.
- **Provides real-time security insights** for proactive threat hunting.
- **Enhances SOC efficiency** by centralizing security events.

> **Example Scenario:**  
> If repeated **Event ID 4625** logins are detected, Sentinel can trigger:
- **Automated alerts** to SOC analysts.
- **Playbooks for automated response** (e.g., block IP, notify admins).

---

## 4. Conclusion

This lab demonstrated how to **connect a virtual machine (VM) to Microsoft Sentinel** and **analyze security logs**, covering:
- **Verifying the VM connection to Log Analytics**.
- **Installing and configuring Windows Security Events via AMA**.
- **Generating security events through brute-force attempts**.
- **Querying security logs using KQL**.

### **Next Steps**
- Configure **custom Sentinel detection rules** based on security logs.
- Integrate **Azure Logic Apps** for automated threat response.
- Enable **real-time incident alerts** for suspicious activities.

---

## 5. References

- [Windows Security Events via AMA in Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/data-connectors/windows-security-events-via-ama)
- [Event ID 4625 - An Account Failed to Log On](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4625)