# Lab Report: Setting Up a Microsoft Azure Account and Provisioning a Windows 365 Cloud PC

## Table of Contents
1. [Creation of a Microsoft Azure Account and Subscription](#1-creation-of-a-microsoft-azure-account-and-subscription)
2. [Comparison Between Azure Virtual Desktop, Windows 365, and Microsoft Business Premium](#2-comparison-between-azure-virtual-desktop-windows-365-and-microsoft-business-premium)
3. [Purchase and Assignment of the Microsoft 365 E5 License](#3-purchase-and-assignment-of-the-microsoft-365-e5-license)
4. [Group and Policy Creation in Intune](#4-group-and-policy-creation-in-intune)
5. [Provisioning a Windows 365 Cloud PC](#5-provisioning-a-windows-365-cloud-pc)
6. [Analysis of Provisioning Issues and Troubleshooting](#6-analysis-of-provisioning-issues-and-troubleshooting)
7. [Summary and Conclusion](#7-summary-and-conclusion)

---

## 1. Creation of a Microsoft Azure Account and Subscription

This section describes the basic setup of a Microsoft Azure account. An active account with a valid subscription is an essential prerequisite for all further steps, such as the provisioning of cloud services and licensing.

### Steps to Create an Azure Account and Activate a Subscription:
1. **Registration of the Azure Account:**
   - Access the registration page of Microsoft Azure at [azure.microsoft.com](https://azure.microsoft.com/en-us/free/).
   - Enter personal details such as name, email address, and phone number.
   - Select a global administrator role for the created account.

2. **Provision of a Payment Method:**
   - A valid credit card was provided to verify identity and enable future billing.
   - Note: Without a payment method, paid services such as Intune or Windows 365 cannot be used.

3. **Activation of the Subscription:**
   - Initially, a free trial version was activated. After the trial period, the subscription was switched to the "Pay-as-you-go" model.
   - The active subscription ensures that all necessary Azure services, such as Intune and Windows 365, can be used.

This subscription is the top-level instance on which all other products, such as licenses and services, will run. In my case, it is **"Azure Subscription 1"**.

![img](https://i.imgur.com/sqZQcsV.png)

---

## 2. Comparison Between Azure Virtual Desktop, Windows 365, and Microsoft Business Premium

This section describes the decision-making process when choosing between Azure Virtual Desktop (AVD), Windows 365, and Microsoft Business Premium. The goal is to highlight the differences and advantages of each solution and explain why Windows 365 and the Microsoft 365 E5 license better met the requirements.

### Comparison of Platforms and Licenses:
#### Azure Virtual Desktop (AVD)
- **Flexibility:** AVD offers a highly customizable environment, but it requires deeper technical expertise.
- **Cost Model:** Billing is based on actual usage (e.g., computing power, storage), which can lead to variable costs.
- **Network Configuration:** Requires the setup of Azure Virtual Networks (VNets) to provision desktops.
- **Target Audience:** Suitable for companies with experienced IT teams and complex requirements.

#### Windows 365
- **Easy Provisioning:** No VNet configuration required, ideal for quick deployment.
- **Cost Model:** Fixed monthly billing per user, ideal for predictable budgets.
- **Zero-Trust Security:** Central management via Microsoft Intune and multi-factor authentication.
- **Target Audience:** Companies looking for a straightforward and secure cloud desktop solution.

Here is a comparison animation between Microsoft 365 and Azure Virtual Desktop Solution:
![img](https://i.imgur.com/ZZg2ove.png)
![img](https://i.imgur.com/HJoXr8y.png)

#### Microsoft Business Premium
- **Cost-Effective:** Suitable for small businesses with less complex requirements.
- **Limited Features:** Does not include advanced security features like Entra ID P2 and Defender for Endpoint.
- **Target Audience:** Small to medium-sized businesses without the need for advanced security solutions.

### Decision Against Microsoft Business Premium
The decision was deliberately not in favor of Microsoft Business Premium because the following requirements were not met:
- **Lack of Zero-Trust Support:** Entra ID P2 is necessary for security policies.
- **Limited Security Features:** Microsoft Defender for Endpoint is not included.

### Table: Comparison of Options
| **Feature**                      | **Azure Virtual Desktop (AVD)** | **Windows 365 (Microsoft 365 E5)** | **Microsoft Business Premium** |
|-----------------------------------|--------------------------------|------------------------------------|---------------------------------|
| **Easy Provisioning**             | ❌ High effort                 | ✅ Intuitive                       | ✅ Intuitive                    |
| **Cost Model**                    | Variable                       | Fixed                              | Fixed                          |
| **Zero-Trust Support**            | ✅ Optional                    | ✅ Fully supported                 | ❌ Not included                 |
| **Entra ID P2**                   | ❌ Optional                    | ✅ Included                        | ❌ Not included                 |
| **Intune Integration**            | ✅ Optional                    | ✅ Fully supported                 | ✅ Limited                      |

---

## 3. Purchase and Assignment of the Microsoft 365 E5 License and Windows 365 Cloud PC License

This section describes the purchase and assignment of the Microsoft 365 E5 license and the Windows 365 Cloud PC license. Both licenses are necessary because the Microsoft 365 E5 license provides security and management features, while the Cloud PC license enables the actual use of a Windows 365 PC.

### Steps for Purchase and Assignment:
1. **Microsoft 365 E5 License:**
   - Access the Microsoft 365 Admin Center at [admin.microsoft.com](https://admin.microsoft.com/).
   - The E5 license was selected due to its advanced security features, such as Entra ID P2 and Microsoft Defender.

2. **Windows 365 Cloud PC License:**
   - Purchase of the "Windows 365 Enterprise 2 vCPU, 8 GB, 128 GB" license.
   - This license is **required** for users in the target group to provision a Cloud PC.
![img](https://i.imgur.com/tmWBHDH.png)

3. **Assignment:**
   - Both licenses were assigned to the global administrator account **popal.e@popaleoutlook.onmicrosoft.com**.
     
![img](https://i.imgur.com/BLRBkMB.png)

P.S.:
I also purchased a Microsoft Intune Suite license for additional lab scenarios. The granular differences between Microsoft 365 E5 and the Intune Suite are as follows:
- **Remote Help:** Secure remote support for user devices, ideal for BYOD scenarios.
- **Endpoint Privilege Management (EPM):** Temporary admin rights for users without security risks.
- **Automated Third-Party App Management:** Patch updates for apps like Adobe or Chrome.
- **Advanced Compliance:** Automatic resolution of policy violations on devices.
- **Advanced Endpoint Analytics:** Proactive error detection and prevention (e.g., crashes).
- **Microsoft Tunnel:** Secure app connections and access, especially for mobile employees.
- **More Security and Efficiency:** Improved management and protection of BYOD and corporate devices.

For smaller companies in non-risk-prone infrastructures, a Microsoft 365 E5 license is sufficient.

---

## 4. Group and Policy Creation in Intune

After purchasing and assigning the licenses, a security group was created to simplify the provisioning of Cloud PCs.
In Azure, there are two options for group types: Security and Microsoft 365. The granular difference lies in the security mechanisms available in Security Groups.
Here is a brief table comparing the differences:
### Table: Comparison of Security Groups and Microsoft 365 Groups

| **Feature**                     | **Security Group**                             | **Microsoft 365 Group**                    |
|----------------------------------|-----------------------------------------------|--------------------------------------------|
| **Primary Purpose**              | Access control and security management        | Collaboration and communication            |
| **Usage for Permissions**        | ✅ Access to resources and role management    | ❌ Not suitable for permissions            |
| **Device Support**               | ✅ Can include users and devices              | ❌ Supports only users                     |
| **Dynamic Membership**           | ✅ Supports automatic rules                   | ❌ No dynamic rules                        |
| **Intune Integration**           | ✅ Fully integrated                           | ❌ Not suitable for policies               |
| **Integration with Conditional Access** | ✅ Can be used for MFA and security policies | ❌ Not supported                           |
| **Role-Based Access Control (RBAC)** | ✅ Direct role assignment possible            | ❌ Not suitable for RBAC                   |
| **Collaboration Features**       | ❌ No collaboration resources included        | ✅ Includes mailbox, Planner, and Teams    |
| **Mail Functionality**           | ❌ Not included                               | ✅ Integrated mailbox and calendar         |
| **Typical Use Cases**            | Security groups, access control, device management | Teams channels, email, project management |

### Steps for Creation:
1. **Creating a Security Group:**
   - Navigate to **Groups → Create New Group** at [intune.microsoft.com](https://intune.microsoft.com/).
   - Group type: **Security Group**.
   - Name: "Windows365-EntraID".

2. **Assignment of the Security Group:**
   - The global administrator **popal.e@popaleoutlook.onmicrosoft.com** was added as a member.

![img](https://i.imgur.com/o24lCAX.png)
---

## 5. Provisioning a Windows 365 Cloud PC

The provisioning of a Windows 365 Cloud PC is a central step in providing a virtual workspace. This section describes how a provisioning policy was created and why certain decisions, such as the selection of a standard image, were made.

### Steps for Provisioning a Windows 365 Cloud PC:
1. **Access to the Intune Admin Center:**
   - Access [intune.microsoft.com](https://intune.microsoft.com/) and log in with the global administrator account.

2. **Creating the Provisioning Policy:**
   - **License type:** Enterprise – since the licensing is based on Enterprise and supports extensive features such as security policies and management.
   - **Join type:** Entra ID Join, as no hybrid environment was used, and the user was created directly in Entra ID.
   - **Region:** Automatic – recommended for faster provisioning.
   - **Naming schema:** **EPL-%USERNAME:5%-%RAND:5%**, where:
     - **EPL** stands for the initials.
     - **%USERNAME:5%** takes the first 5 characters of the username.
     - **%RAND:5%** generates a random 5-digit value for unique identification.

3. **Assignment:**
   - The security group "Windows365-EntraID" was assigned to the provisioning policy.

4. **Selection of the Image:**
   - **Image type:** From the Microsoft Gallery, the image "Windows 11 Enterprise + Microsoft 365 Apps" was selected.
   - **Reasons for the selection:**
     - Pre-installed Microsoft 365 Apps.
     - Up-to-date and secure version.
     - Reduced effort compared to custom images.

5. **Option for Custom Images:**
   - Alternatively, custom images could be uploaded to meet specific requirements. Further details: [Microsoft Custom Images](https://learn.microsoft.com/de-de/mem/autopilot/custom-images).

6. **Device Configuration:**
   - Language and region: **German**.

7. **Group Assignment:**
   - The previously created security group "Windows365-EntraID" was assigned to the provisioning policy.

![img](https://i.imgur.com/i0bN1S8.png)
---

## 6. Analysis of Provisioning Issues and Troubleshooting

During the provisioning of the Windows 365 Cloud PC, issues arose that required adjustments to the settings. This section describes the errors encountered and their solutions.

### Description of Errors:
1. **Problem:**  
   The "Mobile Device Management Authority" setting was set to "None" by default.  
   **Impact:**  
   The provisioning of the Cloud PC failed multiple times, even though all other configurations were correct.

2. **Analysis:**  
   A review of the dashboard revealed that the default Intune configuration needed to be changed. A report from September 2024 confirmed the issue.

### Solution:
- Activation of the Mobile Device Management Authority according to [Microsoft Documentation](https://learn.microsoft.com/en-us/mem/intune/fundamentals/mdm-authority-set).
- Adjustment of the configuration in the Intune Admin Center.

![img](https://i.imgur.com/iSUwsGU.png)

![img](https://i.imgur.com/pSCWDqs.png)

![img](https://i.imgur.com/AnkIlNj.png)

Verification that the Cloud PC has been provisioned and is usable: Simply go to the URL https://windows365.microsoft.com/ and you can see that the provisioned Cloud PC is ready for use.

![img](https://i.imgur.com/KMTzxbe.png)

---

## 7. Summary and Conclusion

This report documents the setup of a Microsoft Azure account, the selection of appropriate licenses, and the provisioning of a Windows 365 Cloud PC. The focus was on choosing a secure, cost-effective, and easy-to-manage solution.

### Conclusion:
- **Windows 365** proved to be the optimal solution for provisioning secure Cloud PCs.
- **Microsoft 365 E5** provided the necessary security and management features.
- The challenges during provisioning were successfully resolved, creating a reliable and scalable setup.

### Suggestions for Improvement:
- **Monitoring and Alerts:** Consider setting up monitoring and alerting systems in Azure to proactively detect and resolve issues with Cloud PCs.
- **User Training:** Provide training for end-users to ensure they can effectively use the Cloud PC environment.
- **Backup and Disaster Recovery:** Implement backup and disaster recovery plans for Cloud PCs to ensure business continuity in case of failures.

---

### Relevant Links:
- [Azure Virtual Desktop vs. Windows 365](https://learn.microsoft.com/de-de/azure/virtual-desktop/)
- [Microsoft 365 E5 License Overview](https://www.microsoft.com/en-us/microsoft-365/compare-microsoft-365-enterprise-plans)
- [Windows 365 Documentation](https://learn.microsoft.com/en-us/windows-365/enterprise/)
- [Intune Custom Images](https://learn.microsoft.com/en-us/mem/autopilot/custom-images)