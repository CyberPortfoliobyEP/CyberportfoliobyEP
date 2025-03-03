# Lab 12-Defender: Creating Phishing Policy

## Table of Contents
1. [Introduction](#1-introduction)
2. [Implementation](#2-implementation)
   - [Microsoft Defender for Office 365 Overview](#21-microsoft-defender-for-office-365-overview)
   - [Preset Security Policies](#22-preset-security-policies)
   - [Creating a Custom Anti-Phishing Policy](#23-creating-a-custom-anti-phishing-policy)
   - [Configuring Spoof Intelligence](#24-configuring-spoof-intelligence)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

---

## 1. Introduction

**Microsoft Defender for Office 365** provides **anti-phishing protection** through preset and custom policies. These policies detect **impersonation attempts, domain spoofing, and email-based threats**.

### **Key Features of Defender for Office 365**
- **Protects against phishing, malware, and spam attacks**.
- **Utilizes AI-driven threat detection**.
- **Provides preset security policies for standard and strict configurations**.
- **Enables advanced anti-phishing measures, including impersonation protection and spoof intelligence**.

> **Screenshot: Microsoft Defender for Office 365 Overview**  
> ![General Defender 365](https://i.imgur.com/iz8BkgF.png)

---

## 2. Implementation

### 2.1 Microsoft Defender for Office 365 Overview

Microsoft Defender for Office 365 includes various **policies and rules** to enhance email security. These policies can be accessed via:

1. **Microsoft Defender Portal**:  
   Navigate to **Email & Collaboration → Policies & Rules → Threat Policies**.
2. **Types of Threat Policies**:
   - **Preset Security Policies** (Standard and Strict)
   - **Anti-Phishing Policies**
   - **Anti-Spam and Anti-Malware Policies**
   - **Safe Links and Safe Attachments**

> **Microsoft Documentation**:  
> [Step-by-Step Guide for Defender for Office 365 Security Policies](https://learn.microsoft.com/en-us/defender-office-365/step-by-step-guides/ensuring-you-always-have-the-optimal-security-controls-with-preset-security-policies)

---

### 2.2 Preset Security Policies

Microsoft provides **preset security policies** with predefined settings for threat protection.

#### **Configuration Steps**
1. Navigate to **Defender Portal → Policies & Rules → Threat Policies → Preset Security Policies**.
2. Select between:
   - **Standard Protection**: Balanced protection with fewer false positives.
   - **Strict Protection**: More aggressive filtering with higher detection rates.
3. Apply policies to **all recipients** or **specific groups**.
4. Use the **Configuration Analyzer** to verify adherence to Microsoft's best practices.

> **Screenshot: Preset Security Baseline**  
> ![Baseline 365](https://i.imgur.com/6JS5HTS.png)

> **Microsoft Documentation**:  
> [Preset Security Policies in Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/step-by-step-guides/ensuring-you-always-have-the-optimal-security-controls-with-preset-security-policies)

---

### 2.3 Creating a Custom Anti-Phishing Policy

In addition to **preset policies**, Microsoft Defender allows for **custom anti-phishing policies**.

#### **Steps to Create a Custom Anti-Phishing Policy**
1. Navigate to **Defender Portal → Policies & Rules → Threat Policies → Anti-Phishing**.
2. By default, Microsoft includes a **built-in policy**:  
   - **Office 365 Anti-Phishing Default (Default)**
   - This policy primarily protects against **impersonation attacks**.
3. To modify the default policy:
   - Select **Edit Protection Settings**.
   - Enable **User Impersonation Protection**.

> **Screenshot: Default Anti-Phishing Policy**  
> ![Phishing Default Policy](https://i.imgur.com/fSOxOEr.png)

#### **Creating a New Custom Policy**
1. Click **Create a Policy**.
2. Assign a **Policy Name** (e.g., `Standard Directory`).
3. Select **Target Users or Groups**.
4. Configure protection settings:
   - **Impersonation Protection**: Detects attempts to impersonate internal users or domains.
   - **Mailbox Intelligence**: Uses AI to analyze email patterns.
   - **Custom Allow/Block Lists**: Specify domains or senders to be blocked or trusted.

> **Microsoft Documentation**:  
> [Impersonation Settings in Anti-Phishing Policies](https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-policies-about#impersonation-settings-in-anti-phishing-policies-in-microsoft-defender-for-office-365)

---

### 2.4 Configuring Spoof Intelligence

**Spoof intelligence** detects and blocks emails sent from **forged domains** attempting to impersonate legitimate senders.

#### **Steps to Enable Spoof Intelligence**
1. Navigate to **Defender Portal → Policies & Rules → Threat Policies → Anti-Phishing**.
2. Select the created **Anti-Phishing Policy**.
3. Enable **Spoof Intelligence**:
   - Detects **third-party senders using an organization's domain**.
   - Blocks suspicious emails flagged as **spoofed**.
4. Configure **Actions**:
   - Move detected spoofed messages to the **Junk Email Folder**.

> **Microsoft Documentation**:  
> [Spoof Intelligence in Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/anti-spoofing-spoof-intelligence)

> **Screenshot: Review & Create Policy**  
> ![Review](https://i.imgur.com/IUOd3Hh.png)

---

## 3. Impact of Deployment

### **Security Benefits of Anti-Phishing Policies**
- **Reduces impersonation attacks** by identifying similar domains.
- **Protects internal and external users** from email-based threats.
- **Enhances security with AI-driven detection** for **spoofed domains and malicious emails**.
- **Minimizes false positives** through **customized allow/block lists**.

> **Example Scenario:**  
> If an external sender attempts to use a **similar-looking domain** (e.g., `contos0.com` instead of `contoso.com`), the **anti-phishing policy** detects the similarity and **blocks the email**.

Organizations that enable **spoof intelligence and impersonation protection** significantly **reduce successful phishing attempts**.

---

## 4. Conclusion

This lab demonstrated how **Microsoft Defender for Office 365** enhances email security through **custom anti-phishing policies**. The key components covered were:
- **Preset security baselines** (Standard & Strict Protection).
- **Creating a custom anti-phishing policy** with granular settings.
- **Enabling spoof intelligence** to detect domain impersonation.

### **Next Steps**
- Regularly review and update **allow/block lists** to improve detection accuracy.
- Monitor **Defender’s Threat Explorer** for real-time phishing attempts.
- Integrate **Safe Links and Safe Attachments** for additional security layers.

---

## 5. References

- [Microsoft Defender for Office 365 - Anti-Phishing Policies](https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-policies-about)
- [Microsoft Defender for Office 365 - Spoof Intelligence](https://learn.microsoft.com/en-us/defender-office-365/anti-spoofing-spoof-intelligence)
- [Step-by-Step Guide to Microsoft 365 Security Policies](https://learn.microsoft.com/en-us/defender-office-365/step-by-step-guides/ensuring-you-always-have-the-optimal-security-controls-with-preset-security-policies)