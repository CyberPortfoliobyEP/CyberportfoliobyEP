# Lab 3-II-Intune Security - Implementing Compliance Policies

## Table of Contents
1. [Introduction](#1-introduction)
2. [Creating a Compliance Policy](#2-creating-a-compliance-policy)
   - [Compliance Settings Overview](#21-compliance-settings-overview)
   - [Password Management and Security Settings](#22-password-management-and-security-settings)
   - [Comparison: Configuration vs. Compliance Settings](#23-comparison-configuration-vs-compliance-settings)
   - [Actions for Noncompliance](#24-actions-for-noncompliance)
   - [Review + Create](#25-review--create)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

# 1. Introduction

This lab focuses on implementing **Compliance Policies** in Microsoft Intune for Windows 365 devices. Compliance policies are essential for ensuring that devices adhere to organizational security requirements.

Key aspects covered:
- Configuring compliance settings, especially **password management**.
- Defining **actions for noncompliance**.
- Comparing **configuration** and **compliance** settings.
- Synchronizing compliance policies with devices.

# 2. Creating a Compliance Policy

The process starts in the **Intune Admin Center** under **Devices > Compliance Policies**. Here, a new compliance policy is created to enforce security requirements.

## 2.1 Compliance Settings Overview

![Screenshot: Compliance – System Security](https://i.imgur.com/7helGnr.png)

Compliance settings include:
- **Device Health:** Ensures the device meets health criteria.
- **Device Properties:** Validates OS versions and configurations.
- **System Security:** Enforces security measures like passwords, encryption, and firewall settings.
- **Microsoft Defender for Endpoint:** Integrates compliance checks with Defender.

> **Note:** Compliance settings help maintain device integrity and security, marking devices as noncompliant if criteria are not met.

## 2.2 Password Management and Security Settings

The screenshot above highlights critical password settings:
- **Minimum Password Length:** Enforces a baseline for password strength.
- **Password Complexity:** Requires alphanumeric characters for stronger passwords.
- **Maximum Inactivity Time:** Locks devices after inactivity to prevent unauthorized access.

### Why This Matters:
- **Security:** Strong passwords reduce the risk of unauthorized access.
- **Compliance:** Ensures devices meet regulatory and organizational standards.
- **Risk Mitigation:** Reduces vulnerability to brute-force attacks.

> **Note:** Regularly reviewing and updating password policies is recommended to adapt to evolving security threats.

## 2.3 Comparison: Configuration vs. Compliance Settings

| **Aspect**                  | **Configuration Settings**                       | **Compliance Settings**                          |
|-----------------------------|-------------------------------------------------|------------------------------------------------|
| **Purpose**                 | Defines device behavior and settings.          | Ensures devices meet security requirements.     |
| **Enforcement**             | Applies settings directly to devices.           | Monitors settings; flags noncompliance.         |
| **Focus**                   | Device configuration (e.g., Wi-Fi, VPN).        | Security compliance (e.g., passwords, encryption). |
| **Response to Issues**      | Settings may fail to apply if unsupported.      | Devices marked noncompliant if requirements not met. |

> **Note:** Compliance settings do not configure devices but verify if the configurations meet defined standards.

## 2.4 Actions for Noncompliance

![Screenshot: Actions for Noncompliance](https://i.imgur.com/ecyY7Tv.png)

When a device is marked as noncompliant, several actions can be triggered:
- **Mark Device as Noncompliant:** Default action for policy violations.
- **Send Email to User:** Notifies the user about noncompliance with a custom **notification template**.
- **Retire Device:** Removes corporate data and access.

### Creating a Notification Template:
- Go to **Intune Admin Center > Notifications**.
- Create a new template specifying the message content.
- Assign the template to the compliance policy.

> **Note:** Clear communication via notifications helps users correct compliance issues promptly.

## 2.5 Review + Create

![Screenshot: Compliance Policy Review + Create](https://i.imgur.com/on1ND5D.png)

After reviewing the policy settings:
- Verify the **targeted groups**.
- Confirm the **compliance criteria**.
- Click **Create** to deploy the policy.

The policy applies to Windows 10/11 devices and enforces the configured compliance settings.

> **Note:** The policy may take up to **1 hour** to apply. Use the **Sync** option on the device to expedite compliance checks.

# 3. Impact of Deployment

Deploying a compliance policy results in:
- **Enhanced Device Security:** Ensures devices meet baseline security requirements.
- **Regulatory Compliance:** Helps organizations adhere to industry regulations.
- **Proactive Risk Management:** Identifies and addresses noncompliant devices.

> **Note:** Regular monitoring of compliance reports is essential to maintain security posture.

# 4. Conclusion

This lab demonstrated the creation and deployment of compliance policies in Microsoft Intune. Key takeaways include:
- The importance of **password management** in compliance.
- Defining effective **actions for noncompliance**.
- Understanding the difference between **configuration** and **compliance** settings.
- The role of **device synchronization** in maintaining compliance.

# 5. References

- [Microsoft Intune Compliance Policies](https://learn.microsoft.com/en-us/mem/intune/protect/protect-devices)
- [Device Configuration vs. Compliance](https://learn.microsoft.com/en-us/mem/intune/configuration/device-profile-create)
- [Conditional Access with Compliance Policies](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview)
