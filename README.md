# 🛡️ Cybersecurity Portfolio – by EP

Welcome to my personal cybersecurity portfolio!  
This repository documents hands-on labs covering attack techniques, defensive strategies, cloud security, and automation — with a strong focus on **Microsoft Azure**, **AI-driven analysis**, and **open-source tools**.

---

## 📘 Table of Contents

1. [🎓 Certifications & Learning Paths](#-certifications--learning-paths)
2. [⚠️ Legal Notice](#-legal-notice)
3. [🤖 AI for Cybersecurity](#-ai-for-cybersecurity--6-labs)
4. [☁️ Azure Labs](#-azure-labs--21-labs)
5. [🔍 Enumerating](#-enumerating--5-labs)
6. [🛰️ Footprinting & Reconnaissance](#-footprinting--reconnaissance--5-labs)
7. [🌐 Network Scanning](#-network-scanning--6-labs)
8. [🛠️ Vulnerability Analysis](#-vulnerability-analysis--5-labs)
9. [🧰 Tools Summary (Red & Blue)](#-tools-summary-red--blue-team)
10. [📚 Planned Labs & To-Do](#-planned-labs--to-do)
11. [📫 Contact](#-contact)

---

## 🎓 Certifications & Learning Paths

| Certification / Course                             | Provider        |
|----------------------------------------------------|-----------------|
| ✅ Google Cybersecurity Certificate                | Google          |
| ✅ ISC2 Certified in Cybersecurity (CC)            | ISC2            |
| ✅ CompTIA Security+                               | CompTIA         |
| ✅ SC-900                                          | Microsoft       |
| ✅ AZ-900                                          | Microsoft       |
| ✅ CEH (Certified Ethical Hacker)                  | EC-Council      |
| ✅ MITRE ATT&CK® Foundation                        | AttackIQ        |
| ✅ ITIL 4 Foundation                               | PeopleCERT      |
| ✅ NIST Cybersecurity Framework Foundation         | Infosec         |
| ✅ ISO/IEC 27001:2022 Foundation                   | PECB            |

---

## ⚠️ Legal Notice

> **All labs were executed in isolated, controlled, and legally compliant environments strictly for educational purposes.**  
> No unauthorized scanning or interaction with external systems occurred.  
> Any resemblance to real-world scenarios is purely for learning simulation.

---

## 🤖 AI for Cybersecurity – 6 Labs

> Application of AI-driven tools for security analysis, vulnerability assessment, and incident response.  
> Focus on scan automation and code-level insight using **ShellGPT**, **GitHub Copilot**, **Nikto**, **Skipfish**, and more.

| Lab | Topic | Description | Link |
|-----|-------|-------------|------|
| Lab 2 | Vulnerability Analysis using ShellGPT with Nikto and Skipfish | AI-assisted web application analysis with classic tools | [View](./AI/Lab%202-Vulnerability%20Analysis%20using%20ShellGPT%20with%20nikto%20and%20skipfish.md) |
| Lab 5a | Enumeration using ShellGPT AI | Automated enumeration using GPT queries and guidance | [View](./AI/Lab%205-Enum.%20using%20ShellGPT%20AI.md) |
| Lab 5b | Network Scanning with ShellGPT | Combining ShellGPT with **Nmap-style** scans | [View](./AI/Lab%205-Network%20scanning%20with%20ShellGPT.md) |
| Lab 6 | Automation of Scans with ShellGPT & GitHub Integration | Automated scans using GitHub Actions + ShellGPT | [View](./AI/Lab%206-Automation%20of%20Scans%20with%20ShellGPT%20%26%20Github%20Integration.md) |
| Lab 20 | Copilot – Malicious Code Analysis | Static analysis of malicious code using **GitHub Copilot** | [View](./AI/Lab%2020-Copilot-Malicious%20Code%20Analysis.md) |
| Lab 21 | Copilot – Investigating Incidents | Using **Copilot** to support triage and incident analysis | [View](./AI/Lab%2021-Copilot-Investigating%20Incidents.md) |

---

## ☁️ Azure Labs – 21 Labs

> Hands-on configuration and security labs in **Microsoft Azure** and **Microsoft 365**.  
> Focus on provisioning, endpoint hardening with **Microsoft Defender**, policy enforcement via **Intune**, and detection with **Microsoft Sentinel**.

📂 See full lab list here: [Azure Labs Overview](#-azure-labs--21-labs)  
(For brevity, full table can be inserted in a separate file or below.)

---

## 🔍 Enumerating – 5 Labs

> Gathering system and service information using classic enumeration techniques.  
> Tools used include **Nmap**, **enum4linux**, **gobuster**, **FFUF**, **Metasploit**, and **ShellGPT**.

| Lab | Topic | Description | Link |
|-----|-------|-------------|------|
| Lab 1 | SMB Enumeration with Nmap, enum4linux & smbclient | Gathering shared resources and user info via SMB | [View](./Enumerating/Lab%201-Enum.%20SMB%20with%20nmap%2C%20enum4linux%2C%20smbclient.md) |
| Lab 2 | DNS Enumeration with gobuster, nslookup, dnsenum, Fierce, dig | Subdomain discovery and DNS info gathering | [View](./Enumerating/Lab%202-Enum.%20DNS%20using%20gobuster%2C%20nslookup%2Cdnsenum%2CFierce%2Cdig.md) |
| Lab 3 | Web Server Enumeration with gobuster, Nikto, FFUF | Directory and vulnerability discovery on web servers | [View](./Enumerating/Lab%203-Enum.%20Webserver%20using%20gobuster%2C%20Nikito%2C%20FFuF.md) |
| Lab 4 | Enumeration with Metasploit | Automated service and version discovery | [View](./Enumerating/Lab%204-Enum.%20with%20Metasploit.md) |
| Lab 5 | Enumeration with ShellGPT | Semantic enumeration using AI-powered queries | [View](./Enumerating/Lab%205-Enum.%20using%20ShellGPT%20AI.md) |

---

## 🛰️ Footprinting & Reconnaissance – 5 Labs

> Passive reconnaissance to gather intelligence before engagement.  
> Tools include **Google Dorks**, **DNSDumpster**, **Sherlock**, **Maltego**, and **theHarvester**.

| Lab | Topic | Description | Link |
|-----|-------|-------------|------|
| Lab 1 | Google Advanced Search | OSINT using Google Hacking techniques | [View](./Footprinting%20%26%20Reconnaissance/Lab%201-F%26R%20Using%20Google%20Advanced%20Search.md) |
| Lab 2 | Netcraft & DNSDumpster | Mapping DNS and infrastructure info | [View](./Footprinting%20%26%20Reconnaissance/Lab%202-F%26R%20using%20Netcraft%20and%20DNSDumpster.md) |
| Lab 3 | Sherlock & Social Networks | Profile discovery using usernames | [View](./Footprinting%20%26%20Reconnaissance/Lab%203-F%26R%20using%20sherlock%20and%20Social%20Networking%20Sites.md) |
| Lab 4 | Whois & dnsrecon | Domain registration and DNS mapping | [View](./Footprinting%20%26%20Reconnaissance/Lab%204-F%26R%20using%20whois%20and%20dnsrecon.md) |
| Lab 5 | theHarvester & Maltego | Visualizing relationships and metadata | [View](./Footprinting%20%26%20Reconnaissance/Lab%205-F%26R%20using%20theHarvester%20and%20Maltego.md) |

---

## 🌐 Network Scanning – 6 Labs

> Active network probing for services, hosts, and firewall evasion.  
> Tools used include **Nmap**, **Metasploit**, **ShellGPT**, **Wireshark**, and evasion techniques.

| Lab | Topic | Description | Link |
|-----|-------|-------------|------|
| Lab 1 | Network Scanning with Nmap | Classic port and service discovery | [View](./Network%20Scanning/Lab%201-Network%20Scanning%20with%20Nmap.md) |
| Lab 2 | OS Discovery with Nmap | Identifying systems and TTL fingerprints | [View](./Network%20Scanning/Lab%202-OS%20Discovery%20with%20Nmap.md) |
| Lab 3 | Bypassing IDS & Firewall (Defender) | Evasion scanning vs. Microsoft Defender | [View](./Network%20Scanning/Lab%203-Scanning%20Beyond%20IDS%20and%20Firewall%20MS%20Defender.md) |
| Lab 4 | Network Scanning with Metasploit | Auxiliary scanner modules for fingerprinting | [View](./Network%20Scanning/Lab%204-Network%20Scanning%20with%20Metasploit%20Framework.md) |
| Lab 5 | Network Scanning with ShellGPT | GPT-generated scan techniques | [View](./Network%20Scanning/Lab%205-Network%20scanning%20with%20ShellGPT.md) |
| Lab 6 | Automation with ShellGPT & GitHub | Scheduled network scans using AI + GitHub | [View](./Network%20Scanning/Lab%206-Automation%20of%20Scans%20with%20ShellGPT%20%26%20Github%20Integration.md) |

---

## 🛠️ Vulnerability Analysis – 5 Labs

> Identifying vulnerabilities and responding to real-world threats in isolated environments.  
> Tools include **OpenVAS**, **Wireshark**, **Microsoft Defender**, **ShellGPT**, **Nikto**, and **NetCraft**.

| Lab | Topic | Description | Link |
|-----|-------|-------------|------|
| Lab 1 | OpenVAS in Docker | Vulnerability scan in isolated container environment | [View](./Vulnerability%20Analysis/Lab%201-Vulnerability%20Analysis%20using%20OpenVAS%20in%20a%20Docker%20Environment.md) |
| Lab 2 | ShellGPT + Nikto + Skipfish | Automated web vulnerability analysis | [View](./Vulnerability%20Analysis/Lab%202-Vulnerability%20Analysis%20using%20ShellGPT%20with%20nikto%20and%20skipfish.md) |
| Lab 3 | Wireshark + Microsoft Defender | Packet analysis and detection of exploits | [View](./Vulnerability%20Analysis/Lab%203-Detect%20and%20Response%20with%20Wireshark%20%26%20Microsoft%20Defender.md) |
| Lab 4 | Phishing Email Defense | Response to phishing using **NetCraft** and **Defender** | [View](./Vulnerability%20Analysis/Lab%204-Attack%2C%20Detection%20and%20Response%20to%20Phishing%20E-Mail%20with%20E-Mail%2C%20NetCraft%2C%20Microsoft%20Defender.md) |
| Lab 5 | DDoS Response Simulation | Identifying and mitigating DDoS attacks | [View](./Vulnerability%20Analysis/Lab%205-Incident%20Reponse%20to%20DDoS%20Attacks%20with%20Windows%20Firewall%2C%20Anti%20DDoS%20Guardian%20and%20Wireshark.md) |

---

## 🧰 Tools Summary (Red & Blue Team)

### 🔴 Red Team Tools
- **Metasploit Framework**
- **Parrot OS**
- **Gobuster**, **FFUF**, **Nikto**
- **theHarvester**, **Sherlock**
- **Social Engineering** (Phishing)
- **dnsenum**, **dnsrecon**, **enum4linux**

### 🔵 Blue Team Tools
- **Microsoft Defender for Endpoint**
- **Microsoft Sentinel**
- **Microsoft Intune** (Autopatch, Compliance)
- **Microsoft Purview / DLP**
- **GitHub Copilot**
- **OpenVAS**
- **Wireshark**
- **UEBA**, **Logic Apps**, **Log Analytics**

---

## 📚 Planned Labs & To-Do

- [ ] USB Malware Detection
- [ ] Reverse Engineering with CyberChef
- [ ] YARA-assisted Threat Detection
- [ ] SIEM Integration with external sources
- [ ] Automated Incident Response (Logic Apps)
- [ ] Forensics: Memory & Artifact Analysis
- [ ] ISO 27001 Policy Lab

---

## 📫 Contact

📧 [Email me](mailto:your.email@example.com)  
💼 [LinkedIn Profile](https://linkedin.com/in/your-profile)

---

> 🔄 This portfolio is continuously updated with new labs, blue team scenarios, red team challenges, and real-world simulations!