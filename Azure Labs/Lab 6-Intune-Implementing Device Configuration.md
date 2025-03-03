
# Lab 3 - Intune Security: Implementing Device Configuration

## Table of Contents
1. [Introduction](#1-introduction)
2. [Creating a Template for Device Restriction](#2-creating-a-template-for-device-restriction)
   - [Configuration Settings Overview](#21-configuration-settings-overview)
   - [Group Assignment](#22-group-assignment)
   - [Applicability Rules](#23-applicability-rules)
   - [Review + Create – Device Restrictions](#24-review--create--device-restrictions)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

# 1. Introduction

This lab demonstrates the process of creating and deploying **Device Configuration Profiles** in Microsoft Intune to manage settings on a **Windows 365 Cloud PC**. The goal is to control specific device behaviors, enhance security, and ensure compliance with organizational policies.

Key aspects covered:

- Creating a Device Restriction Template.
- Assigning configuration profiles to user groups.
- Applying **Applicability Rules** for granular control.
- Configuring settings like **Malicious Site Access**.

# 2. Creating a Template for Device Restriction

The process begins in the **Intune Admin Center** under the **Windows Devices** section. Here, a new configuration profile is created to enforce specific device restrictions.

## 2.1 Configuration Settings Overview

![Screenshot: Configuration Settings Overview](https://i.imgur.com/sx3zr3N.png)

- **Platform:** Windows 10 and later.
- **Profile Type:** Templates → Device Restrictions.

Settings configured:

- **Malicious Site Access:** Enabled to block access to known malicious websites.

> **Note:** Enabling this setting helps mitigate risks associated with phishing attacks and harmful websites.

## 2.2 Group Assignment

![Screenshot: Group Assignment](https://i.imgur.com/KdKEOGH.png)

Assignments are critical in determining which devices receive the policy:

- **Included Group:** Specifies users/devices that should receive the policy.
- **Excluded Group:** Specifies users/devices that should be exempt from the policy.

> **Note:** **Excluded Groups** take priority over **Included Groups**. If a user is in both, the exclusion will override the inclusion.

## 2.3 Applicability Rules

![Screenshot: Applicability Rules](https://i.imgur.com/Oe5zaZ0.png)

**Applicability Rules** define additional criteria for policy application:

- **OS Edition Rule:** Ensures the policy applies only to specific Windows editions.
- **Version Rule:** Targets devices with certain OS versions.

> **Note:** Applicability Rules provide granular control, allowing for precise targeting of configurations.

## 2.4 Review + Create – Device Restrictions

![Screenshot: Review + Create – Device Restrictions](https://i.imgur.com/Uwwiegi.png)

After reviewing the configuration settings, the policy is created and deployed.

Deployment Notes:

- The policy may take up to **1 hour** to apply to the Windows 365 Cloud PC.
- To expedite the process, manually trigger a **sync** on the device.

> **Note:** Always verify policy application by syncing the target device after deployment.

# 3. Impact of Deployment

Deploying the Device Configuration Profile results in:

- **Enhanced Security:** Blocking malicious sites reduces the risk of cyber threats.
- **Policy Compliance:** Ensures devices adhere to organizational security standards.
- **Conflict Resolution:** In case of conflicts with Group Policy Objects (GPOs), **GPOs take precedence** over Intune policies.

> **Note:** Understanding the conflict hierarchy between Intune and GPOs is crucial for effective policy management.

# 4. Conclusion

This lab demonstrated how to create and deploy device configuration profiles using Microsoft Intune. Key takeaways include:

- The importance of **Applicability Rules** for targeted deployments.
- The role of **Included/Excluded Groups** in policy assignments.
- Methods to verify policy application, such as device syncing.

# 5. References

- [Microsoft Intune Documentation](https://learn.microsoft.com/en-us/mem/intune/)
- [Device Configuration Profiles in Intune](https://learn.microsoft.com/en-us/mem/intune/configuration/device-profile-create)
- [Understanding Intune and Group Policy Conflicts](https://learn.microsoft.com/en-us/mem/intune/configuration/gpo-intune-policy-conflict)
