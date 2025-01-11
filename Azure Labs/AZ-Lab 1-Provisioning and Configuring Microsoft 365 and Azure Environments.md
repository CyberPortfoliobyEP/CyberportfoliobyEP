# AZ-Lab 1 Report: Provisioning and Configuring Microsoft 365 and Azure Environments

---
> **_This lab was created and executed on the CYBRARY platform (www.cybrary.com), a leading online training provider for cybersecurity professionals. The platform's virtual labs and cloud-based environments are designed to simulate real-world scenarios. The configuration of this lab, including the location in Washington and the specific use of a Microsoft 365 trial account, follows CYBRARY's guidelines to ensure compatibility with their global infrastructure. As such, decisions like the deployment location and the creation of user accounts (e.g., Dan Park) were guided by these instructional frameworks._**
>
> 
## 1. Lab Details
- **Lab Name**: Provision a Microsoft 365 Trial Account and Device Management in Azure
- **Environment**:  
  - Virtual Machines: Win11, W10-Admin With Office, W10 With Office  
  - Services: Microsoft Azure Portal, Microsoft 365 Admin Center, Microsoft Entra ID, Microsoft Endpoint Manager  
- **Tools Used**:  
  - Microsoft Edge browser  
  - Microsoft Azure  
  - Microsoft 365 Admin Center  
  - Microsoft Intune  
- **Objectives**:  
  - Provision a Microsoft 365 E5 trial subscription.  
  - Deploy and configure a Microsoft Entra tenant.  
  - Configure Intune auto-enrollment for devices.  
  - Add organizational information and create new users.  
  - Verify device registration and configuration profile assignment.  

---

## 2. Introduction
This lab focuses on setting up a foundational Microsoft 365 and Azure environment for future device and identity management. The activities include creating a Microsoft 365 trial subscription, deploying a Microsoft Entra tenant, and configuring device management settings via Microsoft Intune. The goal is to ensure a secure and organized platform for device enrollment and management.

---

## 3. Techniques and Results

### 3.1 Provisioning a Microsoft 365 Trial Account
1. **Creating a Microsoft Entra Tenant**:
   - Signed into the Win11 virtual machine using the credentials `Admin` and `Passw0rd!`.  
   - Opened Microsoft Edge and accessed the Azure Portal (`https://portal.azure.com`).  
   - Logged in using `User1-47281568@cloudslice.onmicrosoft.com` and the provided password.  
   - Created a new Microsoft Entra tenant with the following details:
     - **Organization Name**: Hexelo47281568  
     - **Initial Domain Name**: hexelo47281568.onmicrosoft.com  
     - **Location**: United States  

![img](https://i.imgur.com/xIWoMDX.png)

2. **Adding Organization Information**:
   - Navigated to the Microsoft 365 Admin Center (`https://admin.microsoft.com`).  
   - Signed in as `admin@hexelo47281568.onmicrosoft.com` using the recorded password.  
   - Added organization details as follows:
     - **Name**: Hexelo47281568  
     - **Address**: 1 Microsoft Way, Redmond, WA, 98052, United States  

![img](https://i.imgur.com/JmrUXAl.png)

3. **Recording Credentials**:
   - Saved the following credentials for future labs:
     - **Global Administrator User Principal Name**: `admin@hexelo47281568.onmicrosoft.com`  
     - **Global Administrator Password**: Variable `<Password>`  
     - **Domain**: hexelo47281568.onmicrosoft.com  

---

### 3.2 Creating and Managing Users in Microsoft Entra ID
1. **User Creation**:
   - Accessed the Azure Portal and navigated to **Microsoft Entra ID > Users > New User**.  
   - Created a new user with the following details:
     - **User Principal Name**: `DanP@hexelo47281568.onmicrosoft.com`  
     - **Display Name**: Dan Park  
     - **Password**: Auto-generated `<Password>`  

2. **Assigning Group Membership**:
   - Created a new security group named **Mobile Users**.  
   - Added the user `DanP@hexelo47281568.onmicrosoft.com` to the **Mobile Users** group.  

3. **Verification**:
   - Verified that Dan Park appeared as a member of the **Mobile Users** group.  

---

### 3.3 Configuring Intune Auto-Enrollment
1. **Enable Auto-Enrollment**:
   - Accessed Microsoft Entra ID > **Device Settings**.  
   - Enabled **MDM Enrollment** for Microsoft Intune.  

2. **Verification**:
   - Opened Microsoft Endpoint Manager Admin Center (`https://endpoint.microsoft.com`) to confirm the setting.

**Result**: Successfully configured Intune auto-enrollment for all users.

---

### 3.4 Adding Devices and Configuring Profiles
1. **Joining a Device to Microsoft Entra ID**:
   - Switched to the virtual machine **W10 With Office** and logged in as `Admin`.  
   - Navigated to **Settings > Accounts > Access work or school** and added the account `DanP@hexelo47281568.onmicrosoft.com` with `<Password>`.  

2. **Creating and Applying Configuration Profiles**:
   - Created a new configuration profile using the **Device Restrictions** template in Microsoft Endpoint Manager.  
   - Enabled **Real-time monitoring** for Microsoft Defender Antivirus.  
   - Assigned the configuration profile to the **Mobile Users** group.  

3. **Verification**:
   - Verified that the device registered under Dan Park synchronized and received the assigned configuration profile.

---

## 4. Summary

### Steps Taken:
- Provisioned a Microsoft 365 trial account and deployed a Microsoft Entra tenant.  
- Created a new user (`Dan Park`) and assigned group membership.  
- Enabled Intune auto-enrollment for devices.  
- Joined a virtual machine to Microsoft Entra ID and applied configuration profiles.  

### Findings and Insights:
- Microsoft Entra ID simplifies identity and access management for cloud-based services.  
- Intune auto-enrollment ensures seamless device management with minimal user intervention.  
- Configuration profiles provide granular control over security settings.

### Recommendations:
1. Regularly audit user accounts and group memberships to maintain security.  
2. Verify device enrollment status periodically to ensure compliance.  
3. Test configuration profiles on a limited group of devices before rolling out organization-wide.  

---
