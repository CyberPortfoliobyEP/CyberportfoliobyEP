# Lab 11-Defender-Utilizing Phishing Campaign Simulation

## Table of Contents
1. [Introduction](#1-introduction)
2. [Implementation](#2-implementation)
   - [Prerequisites and Role Requirements](#21-prerequisites-and-role-requirements)
   - [Launching a Phishing Simulation](#22-launching-a-phishing-simulation)
   - [User Experience and Reporting](#23-user-experience-and-reporting)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

---

## 1. Introduction

**Microsoft Defender for Office 365** includes an **Attack Simulation Training** feature that allows administrators to launch simulated phishing attacks to test user awareness and preparedness. This lab focuses on configuring and launching a **phishing campaign simulation** using the **Credential Harvesting** technique.

### **Simulation Overview**
Attack simulations in Microsoft Defender provide organizations with a way to assess employee susceptibility to phishing attempts. When a user interacts with a phishing email, they may be redirected to an educational landing page.

> **Screenshot: Example of a Phishing Simulation Result**  
> ![Simulation Example](https://i.imgur.com/bDbrpMk.png)

---

## 2. Implementation

### 2.1 Prerequisites and Role Requirements

The **Attack Simulation Training** feature requires specific licenses and permissions.

#### **Required Licenses**
- **Microsoft Defender for Office 365 Plan 2**, or
- **Microsoft 365 E5 (which includes Defender for Office 365 Plan 2)**  

For additional licensing details, refer to:  
[Attack Simulation Training Licensing Requirements](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started)

#### **Required Permissions**
At least one of the following roles is required to create and manage simulations:
- **Global Administrator**
- **Security Administrator**
- **Attack Simulation Administrator** (can create and manage simulations)
- **Attack Payload Author** (can create attack payloads)
- **Security Operator and Security Reader** (view-only access)

> **Note:** Microsoft recommends assigning roles with the **least required permissions** to adhere to the **principle of least privilege**.

#### **Microsoft Purview Audit Requirement**
Attack Simulation Training requires **Microsoft Purview Auditing to be enabled** for full reporting capabilities.  
Refer to: [Enable Microsoft Purview Audit Logging](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable?view=o365-worldwide&tabs=microsoft-purview-portal)

---

### 2.2 Launching a Phishing Simulation

A **phishing simulation campaign** follows a structured workflow within Microsoft Defender.

#### **Step 1: Selecting a Simulation Technique**
1. Navigate to **Microsoft Defender Portal** → **Email & Collaboration** → **Attack Simulation Training**.
2. Click **Launch Simulation**.
3. Select the **Credential Harvesting** technique.

> **Description of Credential Harvesting**  
> A **credential harvesting attack** typically involves a phishing email containing a **malicious URL** that directs the user to a fake login page designed to steal credentials.

> **Screenshot: Credential Harvesting Simulation Technique**  
> ![Overview Functionality](https://i.imgur.com/6ftTY9u.png)

#### **Step 2: Configuring the Simulation**
1. Name the simulation **"Campaign 1"**.
2. Select a predefined email **template**:
   - In this example, the **"Password Reset"** template is used.
3. Customize the attack:
   - Adjust the **email content**.
   - Modify the **target URL**.
   - Define the **recipients** and the **frequency** of emails.

> **Note:** The simulation can be sent to **all users**, **specific groups**, or a **custom list of email addresses**.

> **Screenshot: Review & Create Simulation**  
> ![Review + Create](https://i.imgur.com/ujAzT1J.png)

---

### 2.3 User Experience and Reporting

#### **Step 3: Phishing Email and User Interaction**
1. The **targeted user** receives an email appearing to be from Microsoft.
2. The email contains a **suspicious link** leading to a fake login page (`www.windocyte.com`).
3. If the user clicks the link:
   - The admin is notified.
   - The user may be redirected to an **educational training page**.

> **Screenshot: Example Phishing Warning Page**  
> ![Simulation Example](https://i.imgur.com/bDbrpMk.png)

#### **Step 4: Attack Simulation Training & Reporting**
- After failing the phishing test, the user is prompted to complete **awareness training**.
- The admin can review reports within **Defender Portal** under **Simulation Reports**.

> **Important Note:** Microsoft **does not allow admins to target themselves**, meaning a **separate user account** is required for complete testing.

> **Microsoft Requirement:**  
> "In order for Attack Simulation Training to have reporting capabilities, auditing must be enabled."  
> Refer to: [Microsoft Purview Audit Logging](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable?view=o365-worldwide&tabs=microsoft-purview-portal)

---

## 3. Impact of Deployment

**Key Security Benefits of Phishing Simulations:**
- **Improves user awareness** by exposing employees to realistic phishing scenarios.
- **Reduces security risks** by identifying vulnerable users.
- **Automates training** for users who fail the test.
- **Provides compliance tracking** by logging user interactions and training progress.

> **Example Scenario:**  
> If a user clicks on a simulated phishing email and enters their credentials, Microsoft Defender records the event, and the user is automatically assigned **mandatory security training**.

Organizations that implement regular phishing simulations see a **significant reduction in successful phishing attacks**.

---

## 4. Conclusion

This lab demonstrated how **Microsoft Defender for Office 365** can be used to conduct **phishing simulation campaigns**. The following key elements were covered:
- **Prerequisites and permissions** for launching a simulation.
- **Configuring and launching a phishing campaign** using **Credential Harvesting**.
- **Monitoring and analyzing phishing campaign results**.

### **Next Steps**
- Customize phishing templates to **mimic real-world threats**.
- Implement **automated remediation policies** for repeated offenders.
- Use **Defender Advanced Hunting** to analyze user responses and improve training effectiveness.

---

## 5. References

- [Microsoft Defender Attack Simulation Training](https://learn.microsoft.com/en-us/defender-office-365/attack-simulation-training-get-started)
- [Microsoft Purview Audit Logging](https://learn.microsoft.com/en-us/purview/audit-log-enable-disable?view=o365-worldwide&tabs=microsoft-purview-portal)
- [Microsoft Defender for Office 365 Security Features](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security?view=o365-worldwide)