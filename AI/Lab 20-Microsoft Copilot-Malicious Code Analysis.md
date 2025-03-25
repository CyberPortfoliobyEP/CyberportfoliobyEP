# Lab 20-Copilot: Malicious Code Analysis

## Table of Contents
1. [Introduction](#1-introduction)
2. [Implementation](#2-implementation)
   - [Understanding Microsoft Security Copilot](#21-understanding-microsoft-security-copilot)
   - [Deploying Microsoft Security Copilot](#22-deploying-microsoft-security-copilot)
   - [Performing Suspicious Script Analysis](#23-performing-suspicious-script-analysis)
   - [Managing Plugins and File Analysis](#24-managing-plugins-and-file-analysis)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

## 1. Introduction

Microsoft **Security Copilot** is an **AI-powered security solution** that assists in **incident response, security investigations, and malicious code analysis**.  
It integrates **Microsoft Defender XDR, Sentinel, Intune, and third-party security tools** to enhance **SOC operations**.

### **Key Benefits of Security Copilot**
- **Automated threat analysis** using **generative AI**.
- **Reverse engineering of malware and suspicious scripts**.
- **Integration with Microsoft and non-Microsoft security tools**.
- **Guided remediation steps for security teams**.

> **Cost Consideration**  
> - Security Copilot costs **$4 per hour**.  
> - Running it continuously for **one month costs approx. $3,000**.  
> - Recommended for **on-demand usage** to **avoid unnecessary expenses**.

> **Screenshot: Copilot Diagram**  
> ![Copilot Diagram](https://i.imgur.com/GNLcnoL.png)

> **Microsoft Documentation:**  
> [Microsoft Security Copilot Overview](https://www.microsoft.com/de-de/security/business/ai-machine-learning/microsoft-security-copilot)

---

## 2. Implementation

### 2.1 Understanding Microsoft Security Copilot

Security Copilot enables security professionals to:
- **Summarize incidents and perform impact assessments**.
- **Reverse engineer suspicious scripts and malware**.
- **Automate responses to security threats**.
- **Utilize natural language prompts for threat hunting**.

Copilot assists in:
- **Incident prioritization** (e.g., detecting **phishing, ransomware, privilege escalation**).
- **Threat intelligence correlation** with **Microsoft Defender & Sentinel**.
- **Malware code analysis** for **quick identification of obfuscation techniques**.

---

### 2.2 Deploying Microsoft Security Copilot

#### **Steps to Deploy Copilot**
1. Open **Azure Portal**.
2. Search for **"Copilot for Security"**.
3. Click **Create** and configure:
   - **Resource Group**: `CopilotforSecurity`
   - **Security Compute Units (SCUs)**:  
     - **1 SCU**: For occasional security queries.  
     - **5 SCUs**: For **parallel** incident response.  
     - **10+ SCUs**: For **automated threat detection**.
4. Click **Review + Create** → **Deploy**.

> **Screenshot: Copilot Deployment**  
> ![Review+Create Copilot](https://i.imgur.com/xA2Dd6r.png)

#### **Completing the Setup**
1. Once deployed (**~1 min processing time**), go to:  
   **[Security Copilot Setup](https://securitycopilot.microsoft.com/tour/admin)**
2. Default **RBAC roles**:
   - **Global Admin** & **Security Admin** = **Owners** (can manage plugins, access control, and prompts).
   - **Security Analysts** = Limited **read access**.
3. Click **Finish Setup**.

---

### 2.3 Performing Suspicious Script Analysis

Security Copilot assists in **malware reverse engineering** using **predefined prompt books**.

#### **Steps to Analyze a Malicious Script**
1. Navigate to **Microsoft Security Copilot**.
2. Search for **"Suspicious Script Analysis"** in **Prompt Books**.
3. Copy & Paste a **malicious script** from **[ANY.RUN](https://any.run/cybersecurity-blog/malicious-scripts/)**.
4. Click **Submit**.

```Python
import base64  
encoded = "d2Vic2l0ZQ=="  
decoded = base64.b64decode(encoded)  
exec(decoded)  
```
**Outcome**:  
- Copilot detects **obfuscation**:  
  `"Decodes the string 'website' and executes it via base64 obfuscation."`
- Matches **ANY.RUN** results in **5 seconds**.

> **Screenshot: Script Analysis Prompt**  
> ![Prompt 2](https://i.imgur.com/sBw39Bc.png)

#### **Why is This Important?**
- **Identifies encoded or obfuscated payloads**.
- **Reverse engineers potential malware behavior**.
- **Speeds up forensic investigation in SOC workflows**.

> **Microsoft Documentation:**  
> [Microsoft Security Copilot Prompt Books](https://learn.microsoft.com/en-us/microsoft-365/security/security-copilot)

---

### 2.4 Managing Plugins and File Analysis

Security Copilot supports **plugins** to integrate with:
- **Microsoft Defender XDR, Sentinel, Intune**.
- **Third-party tools** (e.g., **Splunk, Palo Alto**).

#### **Managing Plugins**
1. Open **Security Copilot** → Click **"Sources"**.
2. Toggle **Microsoft & Non-Microsoft Plugins** on/off.
3. Assign **RBAC permissions** for each plugin.

> **Screenshot: Plugin Management**  
> ![Plugins Copilot](https://i.imgur.com/w6t8BYs.png)

#### **File Analysis in Copilot**
- Allows **direct cloud uploads** for:
  - **Obfuscated scripts**.
  - **Malware detection (Steganography, Rootkits)**.

#### **Steps to Upload a File**
1. Click **"File Analysis"**.
2. Upload **suspicious code files**.
3. Security Copilot **scans & provides results**.

> **Screenshot: Copilot File Upload**  
> ![Copilot File Upload](https://i.imgur.com/M5IZKPl.png)

---

## 3. Impact of Deployment

### **Security Benefits of Security Copilot**
- **Accelerated threat analysis** using AI-powered **incident summarization**.
- **Automated detection of malware & obfuscated scripts**.
- **Guided remediation & response workflows**.
- **Seamless integration with Microsoft Defender & Sentinel**.
- **Cost-effective investigation** (on-demand usage reduces unnecessary charges).

> **Example Scenario:**  
> - A **ransomware attack** is detected in **Microsoft Defender**.  
> - Security Copilot **summarizes the attack** and provides **remediation steps**.  
> - The **SOC team follows AI-generated recommendations** for **containment**.

---

## 4. Conclusion

This lab demonstrated **how to use Microsoft Security Copilot for malware analysis**, covering:
- **Deploying and configuring Security Copilot**.
- **Performing reverse engineering of suspicious scripts**.
- **Managing plugins and integrating third-party security tools**.

### **Next Steps**
- Configure **custom security playbooks** for Copilot automation.
- Explore **threat-hunting workflows** using **predefined prompt books**.
- Utilize **Kusto queries** to refine malware investigation.

---

## 5. References

- [Microsoft Security Copilot Overview](https://www.microsoft.com/de-de/security/business/ai-machine-learning/microsoft-security-copilot)
- [Microsoft Security Copilot Prompt Books](https://learn.microsoft.com/en-us/microsoft-365/security/security-copilot)
- [ANY.RUN Malware Sandbox](https://any.run/cybersecurity-blog/malicious-scripts/)
- [Microsoft Sentinel & Security Copilot Integration](https://learn.microsoft.com/en-us/microsoft-365/security/security-copilot)