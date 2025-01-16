# **Lab 1: Setup Architecture – Microsoft Azure Platform, Azure Security Features, Subscription, Virtual Machines in UTM**

---

## **General Scenario**

The purpose of this lab is to create an architecture that supports both **attack** and **defense operations**, allowing practical testing of security measures and simulation of threat scenarios. The infrastructure consists of the following components:

1. **Administrator:** Responsible for conducting and managing security operations. The admin configures policies, implements security measures, and analyzes incidents.
2. **Attacker:** Simulated in a Parrot VM, executing attack scenarios such as malware delivery or DDoS attacks.
3. **Victim:** An endpoint user in a Windows VM, used to test security measures and act as the target of attacks.

This architecture is designed to facilitate hands-on testing and demonstrate security features in Microsoft Azure and UTM. The following diagram illustrates the setup:

![Setup Architecture](Setup.png)

---

## **Lab Details**

### **Licenses Used and Their Purpose**

1. **Enterprise Mobility + Security E5 (EMS E5):**
   - **Why EMS E5?**
     - This license provides the advanced security features required for the labs:
       - **Microsoft Defender for Endpoint Plan 2:** For threat detection and automated responses (Lab 1, 2, 6).
       - **Azure Sentinel:** Log and incident management for attack detection and incident response (Lab 6, 7).
       - **Microsoft Purview:** For data classification and governance (Lab 3, 4).
       - **Data Loss Prevention (DLP):** To prevent data leakage (Lab 3).
     - **Key Features Included:**
       - Azure AD Premium P2 for identity protection and conditional access.
       - Microsoft Defender Suite for enhanced endpoint protection.
       - Automated threat remediation.

2. **Microsoft Intune Suite:**
   - **Why Intune Suite?**
     - Essential for device and policy management of the Windows VM (victim machine).
     - Enables enforcement of policies such as device compliance and conditional access (Lab 2, 3, 6).
     - **Key Features Included:**
       - Device management (Endpoint Privilege Management).
       - Policy configuration and monitoring.

3. **Microsoft 365 Business Standard:**
   - **Why Business Standard?**
     - This license provides **Exchange Online**, necessary for email functionality in **Lab 5: Phishing Simulation**.
     - **Key Features Included:**
       - Exchange Online for mailbox and email functionality.
       - Web-based Office applications (e.g., Word, Excel, PowerPoint).
       - OneDrive storage for cloud-based scenarios.

![Architecture](https://i.imgur.com/IfvPzDt.png)
---

## **Steps**

### **Step 1: Registration and Setup in Microsoft Azure**

The Azure portal was used to register and set up the platform for security operations. Two users were created:

1. **Administrator:** Responsible for managing security features and policies.
2. **Markus Ruehl:** An endpoint user assigned specific licenses for the victim machine.

In the **Microsoft 365 Admin Center**, the following actions were performed:
- Licenses **EMS E5**, **Intune Suite**, and **Microsoft 365 Business Standard** were purchased and assigned as follows:
  - **Admin User:** EMS E5 and Intune Suite.
  - **Markus Ruehl:** EMS E5, Intune Suite, and Business Standard.

![img](https://i.imgur.com/rHADmIh.png)

![img](https://i.imgur.com/vlan9Wg.png)

---

### **Step 2: Setting Up the UTM Environment**

The UTM application was installed on a macOS system to facilitate the virtualization of machines. Two virtual machines were created:

1. **Windows 11 (Victim Machine):**
   - A QEMU ARM64-based image was used.
   - Configuration included 16 GB of storage and 4 GB of RAM.
   - The machine was started, and Markus Ruehl logged in to verify license assignments.

2. **Parrot Security OS (Attacker Machine):**
   - A Parrot OS image file was implemented.
   - The machine was configured for attack simulations.

![UTM](https://i.imgur.com/FldL8Fk.png)
---

### **Step 3: License Assignment Verification**

The following verifications were conducted:
1. Markus Ruehl logged into the Windows VM using his Azure credentials.
2. License details were checked in the Microsoft 365 Admin Center.
3. Markus Ruehl successfully logged into Outlook ([Outlook Web App](https://outlook.office365.com)), demonstrating that the Exchange Online mailbox was active. He was able to send and receive emails.

- **Result:** The mailbox was successfully activated. The following screenshot confirms the successful login:

![Outlook Login Successful](https://i.imgur.com/gwwL92j.png)

---

## **Summary**

The architecture is fully set up and ready for lab execution. Key accomplishments include:
- Acquisition and assignment of EMS E5, Intune Suite, and Microsoft 365 Business Standard licenses.
- Configuration of virtual machines in UTM.
- Verification of user login and email functionality on the Windows VM.
- The architecture is prepared for the execution of planned labs (1–7), covering attack and defense scenarios, as well as compliance and governance.

---

Let me know if additional steps or modifications are needed! 😊