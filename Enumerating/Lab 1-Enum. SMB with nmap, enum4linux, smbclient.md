# Lab Report: SMB Enumeration on Windows Server

---

## Lab Details
- **Lab Name**: SMB Enumeration on Windows Server  
- **Lab Environment**: EC-Council iLabs  
- **Lab Goal**: Identify SMB shares, users, and permissions on a Windows Server system using enumeration tools.  
- **Resources Used**:
  - **Parrot Security OS** (attacker machine)  
  - **Windows Server 2022** (target machine, IP address: 10.10.1.22)  
  - **Tools**: nmap, enum4linux-ng, smbclient  

---

## Introduction  
The goal of this lab is to identify SMB shares and retrieve information about users and groups on a Windows Server. SMB (Server Message Block) is a network protocol commonly used for file sharing, which is often misconfigured.  

---

## 1. SMB Port Scan with Nmap

**Command:**  
nmap -p 139,445 --script smb-os-discovery,smb-enum-shares,smb-enum-users 10.10.1.22

**Description:**  
This scan targets SMB ports 139 and 445, using Nmap scripts to detect shares, users, and operating system information.

**Results:**  
- Discovered Users:  
  - Martin  
  - Sheila  
  - Guest  
  - Joshua  
- Operating System: Windows Server 2022 Standard  
- Share Access Errors: NT_STATUS_ACCESS_DENIED for ADMIN$, C$, IPC$  

---

## 2. User and Group Enumeration with enum4linux-ng

**Command:**  
enum4linux-ng -U -G 10.10.1.22

**Description:**  
This tool lists users (-U) and groups (-G) from an SMB server and provides additional configuration details.

**Results:**  
- Supported SMB Dialects:  
  - SMB 1.0  
  - SMB 2.02  
  - SMB 3.0 (preferred SMB 3.0)  
- SMB Signing Required: Yes  
- Discovered Users:  
  - Martin, Sheila, Guest, Joshua  
- Discovered Groups:  
  - DnsAdmins  
  - Domain Users  
  - Enterprise Read-Only Domain Controllers  

---

## 3 & 4. Share Enumeration and Content Browsing

**Commands:**  
1. Enumerate shares:  
smbclient -L //10.10.1.22 -U Guest

2. Browse share content:  
smbclient //10.10.1.22/SharedFolder -U Guest

**Description:**  
These commands enumerate available SMB shares and attempt to browse their content (if accessible).

**Results:**  
- Checked Shares: SharedFolder  
- Outcome: Access denied with guest account, password required  

---

## Summary

**Steps Performed:**  
1. Scanned SMB ports and enumerated shares, users, and groups.  
2. Tested access to SMB shares and attempted to browse content.  

**Findings:**  
- Insecure Configuration: User and group information can be retrieved without authentication.  
- Access to SMB shares is restricted, but further enumeration may reveal vulnerabilities.  

**Recommendations:**  
- Disable the guest account and revise SMB permissions.  
- Regularly review SMB configurations for vulnerabilities.  
- Enable additional security measures, such as enforcing SMB signing and restricting insecure SMB dialects.  