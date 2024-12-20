# Lab: Enumeration with Metasploit

---

## **Lab Details**

- **Attacker Machine:** Parrot Security OS  
- **Target Machine:** Windows Server 2022 with Active Directory  
- **Network Address:** 10.10.1.22  
- **Tools:** Metasploit Framework  
- **Protocols:** SMB, HTTP, SNMP  

---

## **Objective of the Lab**

The objective of this lab is to enumerate a target server using various scanners and modules in the Metasploit Framework. The aim is to identify user accounts, services, and network resources.

---

## **Steps**

### **1. Enumerating SMB User Accounts**

Command:  
use auxiliary/scanner/smb/smb_enumusers  
set RHOSTS 10.10.1.22  
run  

**Expected Outcome:**  
This module attempts to list user accounts available on the SMB service running on the target server. 
 
![Results](https://i.imgur.com/6Vh8U4E.png)

**Results Found:**  
- Users: `Guest`, `Martin`, `Sheila`, `Joshua`  
- Domain: `CEH`  

**Interpretation:**  
The identified usernames can be utilized for potential brute-force or pass-the-hash attacks.  

---

### **2. Retrieving HTTP Version and Server Details**

Command:  
use auxiliary/scanner/http/http_version  
set RHOSTS 10.10.1.22  
run  

**Expected Outcome:**  
This module identifies the HTTP version and additional details about the web server.  

![Results](https://i.imgur.com/y1nG5B6.png)

**Results Found:**  
- Server: Microsoft IIS/10.0  
- Framework: ASP.NET  

**Interpretation:**  
The identified server software may contain vulnerabilities that can be exploited, such as directory traversal or remote code execution (RCE).  

---

### **3. SNMP Enumeration**

Command:  
use auxiliary/scanner/snmp/snmp_enum  
set RHOSTS 10.10.1.22  
run  

**Expected Outcome:**  
The module retrieves SNMP information, including users, network adapters, and system details.  

![Results](https://i.imgur.com/P5LmJQo.png)

![Results](https://i.imgur.com/moxmZeS.png)

![Results](https://i.imgur.com/LIvtber.png)

**Results Found (Key Points):**  
- Users: `Administrator`, `krbtgt`, `SQL_srv`, `DC-Admin`  
- Network Adapters: Hyper-V Network Adapter, WAN Miniport  
- System Details: Windows Server 2022, Intel64 Hardware  

**Interpretation:**  
The retrieved information can be used to target specific user accounts or services effectively.  

---

## Summary

### Steps Taken:
- SMB enumeration using the `smb_enumusers` module.
- HTTP header analysis using the `http_version` module.
- SNMP enumeration using the `snmp_enum` module.

### Findings:
- **SMB Enumeration:**
  - Users identified: `Guest`, `Martin`, `Sheila`, `Joshua`.
  - Domain: `CEH`.

- **HTTP Analysis:**
  - Server: Microsoft IIS/10.0.
  - Framework: ASP.NET.

- **SNMP Enumeration:**
  - Users: `Administrator`, `krbtgt`, `SQL_srv`, `DC-Admin`.
  - Network adapters identified: Hyper-V Network Adapter, WAN Miniport.
  - System details: Windows Server 2022 with Intel64 Hardware.

### Recommendations:
- Perform a detailed analysis of identified SMB accounts for potential weaknesses (e.g., password spraying).
- Investigate the IIS server for misconfigurations or vulnerabilities, focusing on ASP.NET components.
- Further analyze SNMP outputs to target specific accounts or services for further exploitation.
- Apply patches and ensure secure configurations for all identified services.
---