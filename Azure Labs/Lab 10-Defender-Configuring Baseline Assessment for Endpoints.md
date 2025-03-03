# Lab 10-Defender-Configuring Baseline Assessment for Endpoints

## Table of Contents
1. [Introduction](#1-introduction)
2. [Implementation](#2-implementation)
   - [Creating a Device Group](#21-creating-a-device-group)
   - [Configuring Security Baseline Assessment](#22-configuring-security-baseline-assessment)
   - [Applying Group Policy Settings](#23-applying-group-policy-settings)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

---

## 1. Introduction

Microsoft Defender for Endpoint includes a **Security Baseline Assessment** feature that evaluates devices for compliance with security policies. This lab focuses on creating a **Device Group** and configuring a **Baseline Assessment Policy** using **CIS and STIG benchmarks**.

### **Prerequisites**
- A **Microsoft Defender for Endpoint Plan 2** license is required to use **Security Baseline Assessment**.
- **Global Administrator** or **Security Administrator** permissions are necessary.
- The configuration is performed via the **Defender Portal**: [security.microsoft.com](https://security.microsoft.com).

---

## 2. Implementation

### 2.1 Creating a Device Group

A **Device Group** is needed to apply security policies to a defined set of endpoints.

#### **Steps to create a Device Group**
1. Open the **[Microsoft Defender Portal](https://security.microsoft.com)**.
2. Navigate to **Settings → Endpoints → Device Groups**.
3. Select **Add Device Group**.
4. Name the group **FFM**.
5. Under **Conditions**, select `"Starts with 'FFM'"` (ensuring only devices with the prefix `FFM` are included).
6. Set the **Automation Level** to `Full – remediate threats automatically`.

> **Note:** The device may take **up to 10 minutes** to appear in the group.

> **Screenshot: Device Group Creation**  
> ![Device Group Creation](https://i.imgur.com/ksRv9xX.png)

---

### 2.2 Configuring Security Baseline Assessment

The **Security Baseline Assessment** evaluates devices based on predefined security standards.

#### **Steps to create a Baseline Assessment Profile**
1. Open **Defender Portal** → **Vulnerability Management → Baseline Assessment**.
2. Click **Create Profile**.
3. Name the profile **FFM Baseline Assessment**.
4. Under **Software Selection**, choose **Windows 11** (matching the VM used in this lab).
5. Under **Benchmark Selection**, choose either **CIS** or **STIG**.

| Benchmark  | Description |
|------------|-------------|
| **CIS**   | Center for Internet Security, widely used corporate security standard. |
| **STIG**  | U.S. Department of Defense security framework, stricter than CIS. |

6. Select **Compliance Level**: `Level 1 - Corporate Environment General Use`.

> **Screenshot: Review + Create Profile**  
> ![Review + Create Profile](https://i.imgur.com/a5XsqsR.png)

### **Licensing Requirements**
- This feature requires either:  
  - **Microsoft Defender for Endpoint Plan 2**, or  
  - **Microsoft Defender Vulnerability Management**.  
- Refer to the official documentation:  
  - [Baseline Assessment Prerequisites](https://learn.microsoft.com/en-us/defender-vulnerability-management/tvm-prerequisites?view=o365-worldwide)

---

### 2.3 Applying Group Policy Settings

Once the **Baseline Assessment Profile** is created, the system will check compliance.

#### **Verifying compliance in Defender Portal**
1. Open the **Defender Portal**.
2. Navigate to **Baseline Assessment Overview**.
3. Select **FFM Baseline Assessment**.

> **Screenshot: Baseline Assessment Overview**  
> ![Baseline Assessment Overview](https://i.imgur.com/Xm6WJFW.png)

The following settings were flagged as **non-compliant**:
1. **(L1) Ensure 'Turn off Microsoft Defender AntiVirus' is set to 'Disabled'**.
2. **(L1) Ensure 'Configure detection for potentially unwanted applications' is set to 'Enabled: Block'**.

To manually remediate these settings, **Group Policy** must be used.

#### **Manually modifying Group Policy Settings**
1. Open the **Group Policy Editor** using the following command:

   **Bash:**  
   Win + R → gpedit.msc

2. Navigate to the following path:
   
   **Path:**  
   Computer Configuration → Administrative Templates → Windows Components → Microsoft Defender Antivirus

3. Locate the policy **‘Turn off Microsoft Defender AntiVirus’** and change its value to **Disabled**.
4. Force an update with the following command:

   **Bash:**  
   gpupdate /force

> **Screenshot: Group Policy Setting Change**  
> ![Disable Policy 1](https://i.imgur.com/pAab9Un.png)

---

### **Intune Enrollment Limitation**
If the device is already **Intune enrolled**, policy synchronization from Defender may be **unavailable**.

> **Screenshot: Policy Sync Unavailable**  
> ![Policy Sync Unavailable](https://i.imgur.com/orGX3w9.png)

For further details, refer to:  
[Microsoft Intune - MDE Security Integration](https://learn.microsoft.com/en-us/mem/intune/protect/mde-security-integration).

---

## 3. Impact of Deployment

The **Security Baseline Assessment** provides:
- **Visibility into compliance status** across devices.
- **Prevention of misconfigurations** that could introduce vulnerabilities.
- **Insights into security gaps** that need remediation.

> **Example:**  
> Enforcing `"Turn off Microsoft Defender AntiVirus = Disabled"` prevents unauthorized deactivation of antivirus protection, ensuring **continuous malware protection**.

If organizations enforce **STIG** instead of **CIS**, the security standard is **higher**, but usability may be impacted.

---

## 4. Conclusion

This lab demonstrated the configuration of **Microsoft Defender for Endpoint** to perform a **Security Baseline Assessment**. The key elements covered were:
- Creating a **Device Group**.
- Applying a **Security Baseline Policy**.
- Manual remediation via **Group Policy**.

### **Next Steps**
- Automate policy application using **Intune Configuration Profiles**.
- Implement **automated remediation** instead of manual GPO adjustments.
- Monitor compliance via **Defender Advanced Hunting**.

---

## 5. References

- [Microsoft Defender Vulnerability Management - Prerequisites](https://learn.microsoft.com/en-us/defender-vulnerability-management/tvm-prerequisites?view=o365-worldwide)
- [Microsoft Intune - MDE Security Integration](https://learn.microsoft.com/en-us/mem/intune/protect/mde-security-integration)
- [Microsoft Defender for Endpoint - Security Baselines](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/security-baselines?view=o365-worldwide)