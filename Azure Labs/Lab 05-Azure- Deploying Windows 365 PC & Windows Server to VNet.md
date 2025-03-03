# Lab Report: Deploying Windows 365 PC & Windows Server to VNet

## Table of Contents
1. [Introduction](#introduction)
2. [Provisioning an Entra ID Joined Azure Network Connected Windows 365 PC](#provisioning-an-entra-id-joined-azure-network-connected-windows-365-pc)
3. [Adding a Windows Server to the VNet for Testing](#adding-a-windows-server-to-the-vnet-for-testing)
4. [Verifying Connection Between Windows 365 PC and Windows 2022 Server](#verifying-connection-between-windows-365-pc-and-windows-2022-server)
5. [Summary and Conclusion](#summary-and-conclusion)

---

## 1. Introduction

This lab report documents the process of deploying a Windows 365 Cloud PC and a Windows Server to an Azure Virtual Network (VNet). The goal is to establish a secure and efficient connection between the Windows 365 Cloud PC and the Windows Server within the same VNet. This setup is essential for organizations that require their cloud PCs to interact with resources hosted in Azure, such as virtual machines, web applications, or on-premises networks via VPN or ExpressRoute.

The lab covers the following key steps:

- Provisioning a Windows 365 Cloud PC connected to an Azure VNet.
- Adding a Windows Server to the VNet for testing purposes.
- Verifying the connection between the Windows 365 Cloud PC and the Windows Server.

> **Note:** The Azure Network Connection process can take up to an hour to complete, depending on the complexity of the setup and the resources involved.

![Vizualization](https://i.imgur.com/Z55GuHV.png)

---

## 2. Provisioning an Entra ID Joined Azure Network Connected Windows 365 PC

This section describes the process of provisioning a Windows 365 Cloud PC that is connected to an Azure VNet. The existing provisioning policy from Lab 1 was deleted, and a new policy was created to ensure a clean setup.

### Steps to Provision a Windows 365 Cloud PC:

#### Delete Existing Provisioning Policy:
- The existing provisioning policy from Lab 1 was deleted to avoid conflicts and ensure a clean setup.
- The security group associated with the policy was removed before deletion.

#### Create a New Provisioning Policy:
- I have created a new policy with the following configurations (see screenshot):

![Screenshot: New provisioning policy configuration in Intune Admin Cente](https://i.imgur.com/7CFJICy.png)

#### Provisioning Process:
- The provisioning process was initiated, and it took approximately **one hour** for the Windows 365 Cloud PC to be fully provisioned.

> **Note:** Changes to an existing provisioning policy only apply to new resources, such as newly created Cloud PCs. Existing Cloud PCs will not be affected by changes to the provisioning policy. If a new VNet is added to an existing provisioning policy, it will not apply to already provisioned Cloud PCs. To apply the changes, the existing Cloud PCs must be deprovisioned and reprovisioned.


---

## 3. Adding a Windows Server to the VNet for Testing

This section describes the process of adding a Windows Server to the VNet for testing purposes. The server was configured with an auto-shutdown feature to minimize costs.

### Steps to Add a Windows Server to the VNet:

#### Create a Virtual Machine:
- The VM Windows 2022 Server was created won the easiest way and cheapest way for sure. You can also configure option like Backup configuration, Load Balancer and so on but this was not relevant for my lab, the VM  Windows 2022 Server was named `**Server1**` (see screenshot):
![Screenshot: Virtual machine configuration in Azure Portal](https://i.imgur.com/RdGGbfr.png)

#### Configure Networking:
- The virtual machine was connected to **VNet1** and **Subnet1**.
- A public IP address was automatically assigned to the VM.

> **Note:** Azure has his own DHCP Server that assigns automatically IP-Adresses to Resources

#### Enable Auto-Shutdown:
- The auto-shutdown feature was enabled to minimize costs. The shutdown time was set to **8:00 PM (UTC+1)**.

#### Connect to the Windows Server:
1. Once the VM was created, the RDP file was downloaded and used to connect to the Windows Server. In my Mac Unix environment I had to download the "Windows APP" to be able to connect with the RDP file.

> **Note:** I disabled the Firewall in the VM to avoid connection issues during testing.

![Screenshot: Virtual machine configuration in Azure Portal](https://i.imgur.com/Z9e8osf.png)

**Connecting VM via Windows APP on MAC-Host:**  

![Connection VM](https://i.imgur.com/AvaRkUr.png)

---

## 4. Verifying Connection Between Windows 365 PC and Windows 2022 Server

This section describes the process of verifying the connection between the Windows 365 Cloud PC and the Windows Server within the same VNet.

### Steps to Verify the Connection:

#### Check IP Addresses:
- The Windows Server had the IP address **10.1.1.6**.
- The Windows 365 Cloud PC had the IP address **10.1.1.4**.

#### Ping Test:
- A **ping test** was performed from the Windows 365 Cloud PC to the Windows Server.
- The ping test was successful, confirming that the two devices were able to communicate within the VNet.

> **Note:** A ping test is a network diagnostic tool used to test the connectivity between two devices. It sends ICMP (Internet Control Message Protocol) echo request packets to the target device and waits for a response. The results of the ping test show the round-trip time (RTT) for each packet, indicating the latency between the devices.

![Screenshot: Successful ping test from Windows 365 Cloud PC to Windows Server](https://i.imgur.com/22djD89.png)

---

## 5. Summary and Conclusion

This lab successfully demonstrated the process of deploying a Windows 365 Cloud PC and a Windows Server to an Azure VNet. The connection between the two devices was verified, confirming that they can communicate securely within the same VNet.

### Key Takeaways:
- **Azure VNets** provide enhanced security and resource integration compared to Microsoft Hosted Networks.
- **Auto-Shutdown Feature**: The auto-shutdown feature on the Windows Server helped minimize costs.
- **Ping Test**: The ping test confirmed that the Windows 365 Cloud PC and the Windows Server were able to communicate within the VNet.

### Suggestions for Improvement:
- **Monitoring**: Set up Azure Monitor to track network performance and detect issues proactively.
- **User Training**: Provide training for IT staff on managing Azure VNets and Windows 365 connections.
- **Backup and Recovery**: Implement backup and disaster recovery plans for Azure resources.

---

## Relevant Links:
- [Azure Virtual Network Documentation](https://learn.microsoft.com/en-us/azure/virtual-network/)
- [Windows 365 Documentation](https://learn.microsoft.com/en-us/windows-365/)
- [Intune Admin Center](https://endpoint.microsoft.com/)
- [Customer Permissions Needed for Windows 365 Operations](https://learn.microsoft.com/en-us/windows-365/enterprise/customer-permissions)
