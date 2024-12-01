# Lab Report: Operating System Detection (OS Discovery) with Nmap

## Lab Details

- **Lab Name**: Perform OS Discovery
- **Lab Environment**: EC-Council iLabs
- **Lab Goal**: Identifying the operating system on a target system to assess potential vulnerabilities and possible exploits.
- **Resources Used**:
  - Parrot Security OS (Attacker Machine)
  - Windows Server 2022 (Target Machine)
  - Tool: Nmap with Nmap Script Engine (NSE)

---

## Introduction

Operating system detection (OS Discovery) is a central step in penetration testing. It allows for the identification of the operating system of a target system and provides valuable information such as the NetBIOS name, domain name, and running services. In this lab, OS detection is performed using Nmap and the Nmap Script Engine (NSE).

---

## Procedure and Results

### 1. Aggressive Scan with Nmap

- **Command**:  
  `nmap -A 10.10.1.22`
  
- **Description**:  
  This command performs an aggressive scan to identify the operating system, open ports, services, and versions. It enables the quick compilation of host information for further analysis.

- **Results**:  
  - **Operating System**: Windows Server 2022  
  - **Open Ports**: 53, 80, 88, 135, 139, 389, 445, 464, 593, 1433, 3389, etc.  
  - **NetBIOS Name**: WIN-SERVER  
  - **Additional Details**: Service versions, IIS version, and other host information.

      ![Results](https://i.imgur.com/KbxT04s.png)
    
      ![Results](https://i.imgur.com/R4RBrBm.png)

---

### 2. Operating System Detection with `-O`

- **Command**:  
  `nmap -O 10.10.1.22`
  
- **Description**:  
  This command uses the TCP/IP implementation for OS detection. It leverages the differences in the TCP/IP stack configuration of various operating systems.

- **Results**:  
  - **OS Fingerprint**: Windows Server 2022  
  - **Reliability**: 96%

---

### 3. Using the NSE Script `smb-os-discovery`

- **Command**:  
  `nmap --script smb-os-discovery.nse 10.10.1.22`
  
- **Description**:  
  This command performs OS detection over the SMB protocol (Ports 445 and 139). It uses the open SMB ports identified in the previous scan to retrieve operating system information. This is particularly useful for obtaining detailed information such as NetBIOS names, domains, and workgroups.

- **Results**:  
  - **Operating System**: Windows Server 2022  
  - **NetBIOS Computer Name**: WIN-SERVER  
  - **Workgroup**: WORKGROUP  
  - **Current System Time**: 14:32:45 UTC

      ![Results](https://i.imgur.com/N2aQlzZ.png)


---

## Summary

- **Steps Taken**:
  1. Aggressive scan for comprehensive host and service information.
  2. Precise OS detection with `-O`.
  3. Advanced data using the NSE script `smb-os-discovery`, which specifically targets open SMB ports.

- **Key Insights**:
  - Combining different techniques increases the accuracy of OS detection.
  - Open ports such as 445 and 139 are particularly vulnerable and provide detailed information about the operating system.

---

## Learning Points

- **Nmap Parameters**:
  - `-A`: Aggressive scan for comprehensive information.
  - `-O`: OS detection based on TCP/IP fingerprint.
  - `--script smb-os-discovery.nse`: Script for detailed SMB data.

- **Importance of OS Detection**:
  - Provides specific vulnerabilities and attack vectors.
  - Utilizes open ports such as 445 and 139 for additional data.
