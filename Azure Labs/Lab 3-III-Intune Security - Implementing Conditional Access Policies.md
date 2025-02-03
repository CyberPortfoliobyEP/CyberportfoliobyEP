# Lab 3-III-Intune Security - Implementing Conditional Access Policies

## Table of Contents
1. [Introduction](#1-introduction)
2. [Creating a Conditional Access Policy](#2-creating-a-conditional-access-policy)
   - [Users and External Identities](#21-users-and-external-identities)
   - [Conditions: User Risk](#22-conditions-user-risk)
   - [Network Settings](#23-network-settings)
   - [Grant Controls](#24-grant-controls)
   - [Session Controls](#25-session-controls)
   - [Enable Policy Options](#26-enable-policy-options)
3. [Impact of Deployment](#3-impact-of-deployment)
4. [Conclusion](#4-conclusion)
5. [References](#5-references)

# 1. Introduction

Conditional Access is a critical component of Microsoft Entra ID that interprets signals, enforces policies, and determines if a user is granted access to resources. It helps organizations secure access by applying policies based on specific conditions such as user identity, device health, and location.

![Conditional Access Overview](https://i.imgur.com/7W58nzQ.png)

Conditional Access policies can be applied to both internal and external users, enhancing security while maintaining flexibility.

> **Note:** Conditional Access requires the disabling of **Security Defaults** to prevent conflicts with custom policies.

# 2. Creating a Conditional Access Policy

## 2.1 Users and External Identities

![Screenshot: Create Conditional Access policy](https://i.imgur.com/oh8xQrb.png)

When creating a policy, the **Users** section allows targeting:
- **All users** or specific groups.
- **Guest or External Users** for B2B collaboration.

### Example:
Applying a policy that enforces **Multi-Factor Authentication (MFA)** for all **external users** accessing sensitive resources.

![Conditional Access for external identities](https://i.imgur.com/adpV81s.png)

> **Note:** External access flows involve cross-tenant settings, influencing MFA requirements and trust relationships.

## 2.2 Conditions: User Risk

![Screenshot: Conditional Access – User Risk](https://i.imgur.com/ZcfwOJk.png)

The **User Risk** condition leverages AI-driven risk assessments to detect:
- **Anomalous sign-in behaviors** (e.g., impossible travel, unfamiliar locations).
- **Compromised credentials** detected from threat intelligence feeds.

In this policy:
- **High** and **Medium** risk levels are selected.
- **Low** risk users are excluded from the policy.

> **Note:** As shown in the screenshot, selecting risk levels tailors the policy to users with elevated risk profiles.

## 2.3 Network Settings

Network conditions help secure access based on:
- **Trusted IPs:** Allowing access only from known networks.
- **Named Locations:** Defining geographic regions.
- **New Network Protection:** Helps mitigate threats like **DDoS attacks**.

> **Note:** Network-based Conditional Access enhancements were introduced in [2021](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/locations), providing advanced protection against network-based threats.

## 2.4 Grant Controls

![Grant – Control Access Enforcement](https://i.imgur.com/6H9KPsL.png)

The **Grant** section defines the access control behavior:
- **Grant Access** with additional conditions (e.g., require MFA).
- **Block Access** for high-risk scenarios.

### Example:
Enforcing **MFA** for accessing financial data:
- Select **“Grant Access”**.
- Enable **“Require Multi-Factor Authentication”**.

> **Note:** Combining multiple conditions strengthens security without compromising user productivity.

## 2.5 Session Controls

Session controls manage access post-authentication:
- **Sign-in frequency:** Requires re-authentication after set intervals.
- **Persistent browser sessions:** Controls whether users remain signed in.

> **Note:** Session controls help mitigate risks from compromised sessions.

## 2.6 Enable Policy Options

When finalizing the policy, choose from:
- **Report-only:** Simulates policy effects without enforcement.
- **On:** Actively enforces the policy.
- **Off:** Disables the policy.

> **Note:** Enabling policies requires disabling **Security Defaults** to avoid conflicts. If **Security Defaults** are active, you’ll encounter an error prompting you to disable them before proceeding.

# 3. Impact of Deployment

Implementing Conditional Access policies results in:
- **Stronger Security:** Protects against identity-based attacks.
- **Adaptive Access Control:** Dynamic responses to real-time risks.
- **Compliance:** Supports regulatory requirements for secure access.

> **Note:** Regularly review policy reports to optimize security configurations.

# 4. Conclusion

This lab demonstrated the creation of Conditional Access policies to secure organizational resources. Key takeaways:
- Applying policies to **external users** enhances collaboration security.
- **User Risk** conditions leverage AI for dynamic risk assessment.
- **Grant and Session Controls** fine-tune access enforcement.

# 5. References

- [Secure Access with Conditional Access](https://learn.microsoft.com/en-us/entra/architecture/7-secure-access-conditional-access)
- [Conditional Access for External Users](https://learn.microsoft.com/en-us/entra/external-id/authentication-conditional-access#conditional-access-for-external-users)
- [Named Locations in Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/locations)