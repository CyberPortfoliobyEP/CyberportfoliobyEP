# Lab 16-Sentinel: Configuring Threat Intelligence TAXII

## Table of Contents
1. [Introduction](#1-introduction)
2. [Implementation](#2-implementation)
   - [Understanding STIX and TAXII](#21-understanding-stix-and-taxii)
   - [Deploying Microsoft Sentinel Threat Intelligence Connector](#22-deploying-microsoft-sentinel-threat-intelligence-connector)
   - [Integrating Open-Source TAXII Server (Pulsedive)](#23-integrating-open-source-taxii-server-pulsedive)
   - [Verifying TAXII Connection in Sentinel](#24-verifying-taxii-connection-in-sentinel)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

---

## 1. Introduction

Microsoft Sentinel integrates **Threat Intelligence feeds** via the **TAXII (Trusted Automated Exchange of Intelligence Information) protocol**, enabling organizations to collect **indicators of compromise (IOCs)** from external intelligence sources.

### **Key Components of Threat Intelligence**
- **STIX (Structured Threat Information Expression)**: A standardized language for threat intelligence sharing.
- **TAXII (Trusted Automated Exchange of Intelligence Information)**: The transport protocol that enables STIX-compatible data exchange.

> **Screenshot: STIX TAXII Topology**  
> ![STIX TAXII Topology](https://i.imgur.com/vuOyB1o.png)  
> *Source: oasis-open.github.io*

### **Project STIX & TAXII**
The **OASIS Cyber Threat Intelligence (CTI) framework** standardizes cyber threat data sharing.  
- STIX **structures threat intelligence** data.
- TAXII **enables secure transmission of STIX**.

For more details, refer to:  
[OASIS CTI Documentation](https://oasis-open.github.io/cti-documentation/)

---

## 2. Implementation

### 2.1 Understanding STIX and TAXII

The **STIX/TAXII framework** allows organizations to:
- **Consume Open-Source Threat Feeds**: Integrate intelligence feeds from sources like Pulsedive.
- **Collaborate with Threat Intelligence Communities**: Share cyber threat data globally.
- **Utilize Commercial Intelligence Feeds**: Access premium security threat databases.
- **Ingest Local Intelligence**: Use in-house investigations for proactive defense.

> **Microsoft Documentation:**  
> [Understanding Threat Intelligence in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/understand-threat-intelligence)

---

### 2.2 Deploying Microsoft Sentinel Threat Intelligence Connector

The **Threat Intelligence** connector in **Microsoft Sentinel** enables organizations to ingest threat indicators from external sources.

#### **Steps to Enable the Threat Intelligence Connector**
1. Open **Azure Portal** → **Sentinel**.
2. Navigate to **Content Hub**.
3. Search for **Threat Intelligence** and **Install the Connector**.

> **Screenshot: Sentinel TI Connector**  
> ![Sentinel TI Connector](https://i.imgur.com/mBoTfug.png)

### **Prerequisites for Sentinel Threat Intelligence Connector**
| Requirement | Description |
|------------|-------------|
| **Azure Subscription** | A valid **Microsoft Sentinel-enabled** Log Analytics workspace. |
| **Threat Intelligence Source** | A TAXII-compatible **feed provider** (e.g., Pulsedive). |
| **Permissions** | **Microsoft Sentinel Contributor** or **Global Administrator** required to configure. |

> **Microsoft Documentation:**  
> [Microsoft Sentinel Threat Intelligence](https://learn.microsoft.com/en-us/azure/sentinel/understand-threat-intelligence)

---

### 2.3 Integrating Open-Source TAXII Server (Pulsedive)

To utilize **free threat intelligence feeds**, a **TAXII server** is required.  
Pulsedive provides **TAXII 2.0 services** that are compatible with **Microsoft Sentinel**.

#### **Steps to Set Up Pulsedive TAXII Server**
1. Register an account at **[Pulsedive](https://pulsedive.com/)**.
2. Navigate to **Pulsedive API Pricing** and select the **Free Plan**.

> **Screenshot: Pulsedive Pricing**  
> ![Pulsedive Pricing](https://i.imgur.com/mTzIsqZ.png)

3. Go to **Pulsedive Quickstep** and copy the following required information:
   - **API Root URL**: `https://pulsedive.com/taxii2/api/`
   - **Username**: `taxii2`
   - **Password**: **Your private API key** (found in Pulsedive account settings).

> **Screenshot: Quickstep Pulsedive Configuration**  
> ![Quickstep Pulsedive](https://i.imgur.com/DlQEKxf.png)

#### **Configuring Sentinel Threat Intelligence TAXII Connector**
1. Open **Sentinel** → **Data Connectors**.
2. Select **Threat Intelligence - TAXII**.
3. Enter the following:
   - **Server Name**: `PulseFeed`
   - **API Root URL**: `https://pulsedive.com/taxii2/api/`
   - **Collection ID**: Retrieved from Pulsedive.
   - **Username**: `taxii2`
   - **Password**: **Your API Key**

4. Click **Add**.

> **Screenshot: TI Setup**  
> ![TI Setup](https://i.imgur.com/gZjFvTL.png)

---

### 2.4 Verifying TAXII Connection in Sentinel

After configuring the TAXII server, the connection should be verified in **Sentinel Logs**.

#### **Steps to Verify Threat Intelligence Feed**
1. Open **Sentinel** → **Logs**.
2. Run the following query to check for threat indicators:

   **Kusto Query:**  
   ThreatIntelligenceIndicator  
   | where TimeGenerated > ago(24h)  
   | project TimeGenerated, Description, Type  
   | order by TimeGenerated desc  

> **Screenshot: Verifying TAXII Connection**  
> ![Verifying TAXII Connection](https://i.imgur.com/AGFOJAN.png)

### **Analyzing Query Results**
- **TimeGenerated**: Confirms when threat intelligence data was ingested.
- **SourceSystem**: Displays **PulseFeed**, verifying integration with Pulsedive.
- **Threat Type**: Indicates **malicious domains, IPs, or hashes** detected.

> **Microsoft Documentation:**  
> [Microsoft Sentinel Threat Intelligence Queries](https://learn.microsoft.com/en-us/azure/sentinel/threat-intelligence-query)

---

## 3. Impact of Deployment

### **Security Benefits of Threat Intelligence in Sentinel**
- **Real-time Threat Detection**: Identifies malicious indicators from threat intelligence feeds.
- **Proactive Defense Against Cyber Threats**: Blocks known malicious actors before incidents occur.
- **Community-Driven Security Collaboration**: Integrates **open-source, commercial, and private intelligence** sources.
- **Automation & Response**: Correlates intelligence with **SOAR (Security Orchestration and Automated Response)** playbooks.

> **Example Scenario:**  
> If **PulseFeed** provides an indicator for a **malicious IP**, Sentinel can **automatically create an alert**, blocking traffic to that IP.

---

## 4. Conclusion

This lab demonstrated how to integrate **Threat Intelligence Feeds** with **Microsoft Sentinel**, covering:
- **Understanding STIX and TAXII protocols**.
- **Configuring the Microsoft Sentinel Threat Intelligence Connector**.
- **Setting up an open-source TAXII provider (Pulsedive)**.
- **Verifying the connection through Sentinel Logs**.

### **Next Steps**
- Enable **Automated Incident Response** using Sentinel Playbooks.
- Integrate **commercial threat intelligence feeds** for enriched data.
- Utilize **custom analytics rules** for deeper threat correlation.

---

## 5. References

- [OASIS CTI Documentation](https://oasis-open.github.io/cti-documentation/)
- [Microsoft Sentinel Threat Intelligence](https://learn.microsoft.com/en-us/azure/sentinel/understand-threat-intelligence)
- [Microsoft Sentinel Threat Intelligence Queries](https://learn.microsoft.com/en-us/azure/sentinel/threat-intelligence-query)
- [Pulsedive TAXII Integration](https://pulsedive.com/)