
# Lab Report: Network Scanning with Various Scanning Tools

## Lab Details

- **Lab Name:** Network Scanning with Various Scanning Tools
- **Lab Environment:** EC-Council iLabs
- **Lab Objective:** Conduct a comprehensive network scan to identify active hosts, open ports, and operating system details using Metasploit and Nmap.
- **Resources Used:**
  - Parrot Security OS (Attacker machine)
  - Target Machine: Windows 11 (IP Address: 10.10.1.11, Subnet: 10.10.1.0/24)
  - Tools: Metasploit Framework and Nmap

---

## Introduction

The goal of this lab is to demonstrate techniques for collecting detailed information about target networks to identify potential vulnerabilities. This includes identifying active hosts, open ports, and operating system details. The information gathered serves as the foundation for vulnerability analysis and security assessments. The scans are conducted on a Windows target machine within the 10.10.1.0/24 subnet.

---

## Techniques and Results

### 1. Network Scan with Metasploit

#### Step 1: Starting the Metasploit Console
```
msfconsole
```
- **Description:**  
  This command starts the Metasploit Framework console, a central platform for various security and scanning tools. Once launched, modules and external tools like Nmap can be used for network scans.

#### Step 2: Network Scan with Nmap
```
nmap -Pn -sS -A -oX Test 10.10.1.0/24
```
- **Description:**  
  The Nmap scan is initiated directly from the Metasploit console. The parameters used are explained below:
  - `-Pn`: Disables host discovery (ping scan) and treats all hosts as active, useful when firewalls block ICMP requests.
  - `-sS`: Performs a SYN scan using half-open TCP connections. This method is faster and more discreet than a full TCP handshake.
  - `-A`: Enables advanced scanning functions, including OS detection, service versioning, and traceroute.
  - `-oX Test`: Saves the scan results in XML format to a file named "Test".
  
  The goal is to obtain a comprehensive overview of the 10.10.1.0/24 subnet, including active hosts, open ports, running services, and operating system details.

- **Results:**  
  - The scan identified multiple active hosts within the subnet.
  - Open ports and information on services and operating systems of the target hosts were successfully gathered.

      ![Results](https://i.imgur.com/qcEvLmJ.png)
      ![Results](https://i.imgur.com/zYCZsXR.png)
      ![Results](https://i.imgur.com/jENpNp8.png)

---

### 2. SYN Scan with Metasploit
```
use auxiliary/scanner/portscan/syn
set INTERFACE eth0
set PORTS 80
set RHOSTS 10.10.1.5-23
set THREADS 50
run
```
      ![Results](https://i.imgur.com/vg2efje.png)

- **Description:**  
  This SYN scan targeted the range 10.10.1.5-23 to specifically identify open ports, such as port 80. The use of multiple threads ensures efficient scanning.


- **Results:**  
  - Port 80 was identified as open on several hosts within the target range.

      ![Results](https://i.imgur.com/5YGjAWY.png)

---

### 3. TCP Scan with Metasploit
```
use auxiliary/scanner/portscan/tcp
set RHOSTS 10.10.1.22
run
```
- **Description:**  
  A TCP scan was performed on the specific target IP address 10.10.1.22 to create a detailed list of open TCP ports.

- **Results:**  
  - All open TCP ports on the target machine were successfully identified.

      ![Results](https://i.imgur.com/iDb7lqC.png)

---

### 4. SMB Version Scan
```
use auxiliary/scanner/smb/smb_version
set RHOSTS 10.10.1.5-23
set THREADS 11
run
```
- **Description:**  
  The SMB version scan collected detailed information about the SMB versions running on target hosts. This helps determine the operating systems in use (e.g., Windows or Samba on Linux).

- **Results:**  
  - The operating systems and SMB versions of the target machines were successfully identified.

---

## Summary

### Steps Taken:
1. Conducted a network scan with Metasploit and Nmap to identify active hosts, open ports, and services in the subnet.
2. Performed SYN and TCP scans to gather specific information about open ports.
3. Executed an SMB scan to identify operating system details of the target hosts.

### Key Learnings:
- Combining Metasploit and Nmap provides a powerful approach for comprehensive network analysis.
- Targeted scans of specific IP ranges and ports yield detailed insights for further analysis.
- Collected data is essential for identifying potential vulnerabilities and planning mitigations.

### Recommendations:
- Regularly conduct network scans to identify potential security gaps early.
- Implement and routinely test Intrusion Detection Systems (IDS) and firewalls to block unauthorized scans.
- Provide training for IT staff and penetration testers to stay updated on modern tools like Metasploit.
- Establish a continuous vulnerability management process to timely patch security issues.

---

