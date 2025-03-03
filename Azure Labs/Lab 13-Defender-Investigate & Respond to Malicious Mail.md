# Lab 13 - Defender: Investigate & Respond to Malicious Mail

## Table of Contents
1. [Introduction](#1-introduction)
2. [Implementation](#2-implementation)
   - [Sending a Fake Email with Malicious Attachment](#21-sending-a-fake-email-with-malicious-attachment)
   - [Analyzing Email Headers in Microsoft Defender](#22-analyzing-email-headers-in-microsoft-defender)
   - [Taking Action Against the Malicious Email](#23-taking-action-against-the-malicious-email)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

## 1. Introduction

Microsoft Defender for Office 365 provides built-in tools for **email security and threat investigation**. This lab demonstrates how to send a **simulated phishing email** with a **malicious link and attachment**, analyze the email headers using **Microsoft Defender**, and manually respond to the identified threat.

> **Screenshot: Received Malicious Email**  
> ![Received](https://i.imgur.com/yN5a3ej.png)

## 2. Implementation

### 2.1 Sending a Fake Email with Malicious Attachment

To simulate an **email-based attack**, a **fake tracking link** and an **email attachment** were used.

#### **Steps to Generate a Fake Link & Send a Malicious Email**
1. A **fake tracking link** was generated using **Protoolio.com/links**.
2. The **anonymous email service** **5ymail.com** was used to send a phishing email.
3. The **malicious link** and a **random attachment** were embedded in the email.

**Outcome**: The email was delivered to the **Junk Folder**, following Microsoft Defender's **default security policies**.

> **Screenshot: Email Received in Junk Folder**  
> ![Received](https://i.imgur.com/yN5a3ej.png)

### 2.2 Analyzing Email Headers in Microsoft Defender

To investigate the **email authenticity and security checks**, the **Message Header Analyzer** in **Microsoft Defender** was used.

#### **Steps to Analyze Email Headers**
1. Navigate to **Microsoft Defender Portal** → **Threat Explorer**.
2. Open the received **email entity**.
3. Click on **Message Header Analyzer**.

**Key Observations:**  
The sender domain **5ymail.com** was **marked as legitimate**, and the authentication results confirmed:
-Received-SPF Pass (protection.outlook.com: domain of 5ymail.de designates 20.82.148.229 as permitted sender)
-Authentication-Results spf=pass (sender IP is 20.82.148.229) smtp.mailfrom=5ymail.de;
-DKIM=pass (signature was verified) header.d=5ymail.de;
-DMARC=pass action=none header.from=5ymail.de;
-Compauth=pass reason=100.
> **Screenshot: Email Header Analysis**  
> ![Analyzer](https://i.imgur.com/CFFW7oV.png)

### **Why is This Important?**
- Even though the email was technically **valid** (SPF/DKIM/DMARC passed), it was **malicious**.
- **Threat actors** can use **legitimate domains** for **social engineering attacks**.

> **Microsoft Documentation:**  
> [Microsoft Defender for Office 365 - Email Authentication](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication)

### 2.3 Taking Action Against the Malicious Email

After identifying the email as **potentially malicious**, **remediation actions** were taken.

#### **Steps to Respond to the Email Threat**
1. Navigate to **Microsoft Defender Portal** → **Threat Explorer**.
2. Open the email **entity view**.
3. Click on **Take Action**.
4. Select:
   - **"Move or Delete from Junk Box"**: Manually remove the email.
   - **"Initiate Automated Investigation"**: Identify related threats and remediation options.

> **Screenshot: Defender Action Options**  
> ![Action](https://i.imgur.com/AoPNhQL.png)

#### **Verifying the Actions in the Action Center**
After performing the actions, the **Action Center** confirmed:
- The email was **successfully moved** to the **Junk Folder**.
- **Manual deletion** was also possible using **"Take Action"**.

> **Screenshot: Action Center Confirmation**  
> ![Action Center](https://i.imgur.com/VR65HwS.png)

## 3. Impact of Deployment

### **Security Benefits of Email Threat Investigation**
- **Identifies advanced phishing techniques** even when SPF/DKIM/DMARC pass.
- **Empowers security teams** with manual and automated remediation options.
- **Enhances email security posture** by detecting and responding to threats in real time.

> **Example Scenario:**  
> If a malicious email bypasses **Defenders automated filtering**, manual review and **proactive investigation** can **prevent user compromise**.

## 4. Conclusion

This lab demonstrated how to **investigate and respond to a phishing email** using **Microsoft Defender for Office 365**.  
- A **fake phishing email** was sent using **5ymail.com**.  
- **Microsoft Defender Threat Explorer** was used to analyze **email headers**.  
- **Remediation actions** were taken, including **deleting the email** and **initiating an automated investigation**.

### **Next Steps**
- Enable **Defender Attack Simulation** to train users on phishing threats.
- Implement **custom email filtering rules** for enhanced detection.
- Monitor **Defender Explorer Logs** for **real-time threat intelligence**.

## 5. References

- [Microsoft Defender for Office 365 - Threat Explorer](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/threat-explorer)
- [Microsoft Defender for Office 365 - Email Authentication](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/email-authentication)
- [Microsoft Defender - Action Center](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/action-center)
