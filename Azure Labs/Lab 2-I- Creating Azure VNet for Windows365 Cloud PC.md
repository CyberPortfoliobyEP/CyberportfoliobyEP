# Lab Report: Creating Azure VNet for Windows365 Cloud PC

## Table of Contents
1. [Introduction](#1-introduction)
2. [Visualization of Azure Connection with Windows 365 Cloud PC](#2-visualization-of-azure-connection-with-windows-365-cloud-pc)
3. [Creating a Virtual Network (VNet) in Azure](#3-creating-a-virtual-network-vnet-in-azure)
4. [Permissions Required for Windows 365 to Support Azure Networking](#4-permissions-required-for-windows-365-to-support-azure-networking)
5. [Creating an Azure Network Connection in Windows 365](#5-creating-an-azure-network-connection-in-windows-365)
6. [Summary and Conclusion](#6-summary-and-conclusion)

---

## 1. Introduction

This lab report documents the process of establishing Azure network connections with Windows 365 Cloud PC. The goal is to enable secure and efficient communication between Windows 365 Cloud PCs and Azure Virtual Networks (VNets). This setup is essential for organizations that require their cloud PCs to interact with resources hosted in Azure, such as virtual machines, web applications, or on-premises networks via VPN or ExpressRoute.

The lab covers the following key steps:
- Visualization of Azure network connections and the role of VNets.
- Creation of a VNet in Azure.
- Assignment of necessary permissions for Windows 365 to interact with Azure resources.
- Creation of an Azure Network Connection (ANC) in Windows 365.

**Note:** The Azure Network Connection process can take up to an hour to complete, depending on the complexity of the setup and the resources involved.

---

## 2. Visualization of Azure Connection with Windows 365 Cloud PC

This section provides an overview of how Windows 365 Cloud PCs interact with Azure Virtual Networks (VNets) and the benefits of using VNets over Microsoft Hosted Networks.

![VNets-Functionality](https://i.imgur.com/iTtIry4.png)

### Key Concepts:
- **Microsoft Hosted Network:** By default, Windows 365 Cloud PCs use a Microsoft Hosted Network, which allows them to join Entra ID and be managed via Intune. However, this setup does not allow direct interaction with Azure VNets or on-premises networks.
- **Azure Virtual Network (VNet):** A VNet enables secure communication between Azure resources, such as virtual machines, and can be connected to on-premises networks via VPN or ExpressRoute. VNets also support advanced features like Network Security Groups (NSGs) and subnetting.

### Comparison: Microsoft Hosted Network vs. Azure VNet

| **Feature**                     | **Microsoft Hosted Network**                  | **Azure Virtual Network (VNet)**              |
|----------------------------------|-----------------------------------------------|-----------------------------------------------|
| **Direct Azure Resource Access** | ❌ Not supported                              | ✅ Fully supported                            |
| **On-Premises Connectivity**     | ❌ Not supported                              | ✅ Supported via VPN or ExpressRoute          |
| **Subnetting**                   | ❌ Not supported                              | ✅ Supports multiple subnets                  |
| **Network Security Groups (NSGs)** | ❌ Not supported                              | ✅ Supports NSGs for traffic filtering        |
| **Use Case**                     | Basic cloud PC setup with no Azure integration | Advanced setups requiring Azure resource access |

### Why Use Azure VNet with Windows 365?
- **Enhanced Security:** VNets allow for granular control over network traffic using NSGs.
- **Resource Integration:** Cloud PCs can interact with Azure resources like virtual machines and web applications.
- **On-Premises Connectivity:** VNets can be connected to on-premises networks, enabling hybrid cloud scenarios.

[Screenshot: Diagram showing Azure VNet connectivity with Windows 365 Cloud PC]

---

## 3. Creating a Virtual Network (VNet) in Azure

This section describes the steps to create a VNet in Azure, which is a prerequisite for establishing an Azure Network Connection with Windows 365.

### Steps to Create a VNet:
1. **Access the Azure Portal:**
   - Navigate to [portal.azure.com](https://portal.azure.com) and log in with your credentials.

2. **Create a Resource Group:**
   - All Azure resources must be contained within a resource group. In this lab, the resource group was named **"Laboratorium"**.
   - Go to **Resource Groups** → **Create** and enter the name **"Laboratorium"**. Select the region **West Europe**.

3. **Create the VNet:**
   - Navigate to **Virtual Networks** → **Create**.
   - The VNet was named **"VNet1"** and associated with the **"Laboratorium"** resource group.
   - The IP address space was set to **10.1.0.0/16**.

4. **Add Subnets:**
   - A subnet named **"Subnet1"** was created with the IP range **10.1.1.0/24**.
   - Optionally, a second subnet named **"Subnet2"** was created with the IP range **10.1.2.0/24**.
   - Subnets within the same VNet can communicate with each other automatically.

5. **Review and Create:**
   - The settings were validated and the VNet was created by clicking **Create**.

![Screenshot: VNet configuration in Azure Portal](https://i.imgur.com/FLS1V6C.png)
![Screenshot: VNet configuration in Azure Portal 2](https://i.imgur.com/gSrTyvT.png)
---

## 4. Permissions Required for Windows 365 to Support Azure Networking

To enable Windows 365 Cloud PCs to interact with Azure resources, specific permissions must be assigned to the Windows 365 service.

Note: See also in the link https://learn.microsoft.com/en-us/windows-365/enterprise/customer-permissions the requirements guidelines.
![Requirements VNet](https://i.imgur.com/2ETgIKQ.png)

### Required Permissions:
1. **Reader Permission on Azure Subscription:**
   - Assign the **Reader** role to the Windows 365 service at the subscription level.
   - This allows Windows 365 to read Azure resources.

2. **Windows 365 Network Interface Contributor Role:**
   - Assign this role to the **"Laboratorium"** resource group.
   - This role allows Windows 365 to manage network interfaces within the resource group.


3. **Windows 365 Network User Role:**
   - Assign this role to the **"VNet1"** virtual network.
   - This role allows Windows 365 to use the VNet for network connections.


### Steps to Assign Permissions:
1. **Reader Permission:**
   - Navigate to **Subscriptions** → **Access Control (IAM)** → **Add Role Assignment**.
   - Select **Reader** and assign it to the Windows 365 service.
![Role assignment "Reader"](https://i.imgur.com/G3pUdVB.png)

2. **Network Interface Contributor Role:**
   - Navigate to **Resource Groups** → **Laboratorium"** → **Access Control (IAM)** → **Add Role Assignment**.
   - Select **Windows 365 Network Interface Contributor** and assign it to the Windows 365 service.
[Role assignment "NEtwork Contributer"](https://i.imgur.com/S6a3FAp.png)

3. **Network User Role:**
   - Navigate to **Virtual Networks** → **VNet1"** → **Access Control (IAM)** → **Add Role Assignment**.
   - Select **Windows 365 Network User** and assign it to the Windows 365 service.
![Role assignment "Network User"](https://i.imgur.com/AWxQqKM.png)

---

## 5. Creating an Azure Network Connection in Windows 365

This section describes the process of creating an Azure Network Connection (ANC) in Windows 365, which allows Cloud PCs to connect to the Azure VNet.

### Steps to Create an ANC:
1. **Access the Intune Admin Center:**
   - Navigate to [intune.microsoft.com](https://intune.microsoft.com/) and log in with your global administrator account.

2. **Create the ANC:**
   - Go to **Devices** → **Windows 365** → **Azure Network Connection** → **Create**.
   - Select **Microsoft Entra Join** as the join type.
   - The connection was named **"VNet1-Connection"**.
   - The subscription, resource group (**"Laboratorium"**), and VNet (**"VNet1"**) were selected.
   - **"Subnet1"** was chosen as the target subnet.

3. **Review and Create:**
   - The settings were validated and the ANC was created by clicking **Create**.
   - The ANC creation process can take up to an hour to complete.

![Screenshot: ANC creation in Intune Admin Center](https://i.imgur.com/8aqdHGu.png)

Successful created VNet overview:
![VNet creation](https://i.imgur.com/iWg7kkW.png)

Steps that has been taken from Azure to create the VNet:
![Steps for creation of VNet](https://i.imgur.com/GDwczNP.png)

---

## 6. Summary and Conclusion

This lab successfully demonstrated the process of establishing Azure network connections with Windows 365 Cloud PCs. By creating a VNet, assigning the necessary permissions, and setting up an Azure Network Connection, organizations can enable secure and efficient communication between their Cloud PCs and Azure resources.

### Key Takeaways:
- **Azure VNets** provide enhanced security and resource integration compared to Microsoft Hosted Networks.
- **Permissions** must be carefully assigned to allow Windows 365 to interact with Azure resources.
- **Azure Network Connections** enable Cloud PCs to access Azure VNets and on-premises networks.

### Suggestions for Improvement:
- **Monitoring:** Set up Azure Monitor to track network performance and detect issues proactively.
- **User Training:** Provide training for IT staff on managing Azure VNets and Windows 365 connections.
- **Backup and Recovery:** Implement backup and disaster recovery plans for Azure resources.

---

### Relevant Links:
- [Azure Virtual Network Documentation](https://learn.microsoft.com/en-us/azure/virtual-network/)
- [Windows 365 Documentation](https://learn.microsoft.com/en-us/windows-365/enterprise/)
- [Intune Admin Center](https://intune.microsoft.com/)
- [Customer Permissions Needed for Windows 365 Operations](https://learn.microsoft.com/en-us/windows-365/enterprise/customer-permissions)

---
