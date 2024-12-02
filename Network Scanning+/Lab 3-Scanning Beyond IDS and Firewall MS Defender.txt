# Lab Report: Scanning Beyond IDS and Firewall

## Lab Details

- **Lab Name:** Scanning Beyond IDS and Firewall
- **Lab Environment:** EC-Council iLabs
- **Lab Objective:** Analyze the weaknesses of IDS and firewall security mechanisms by bypassing them using Nmap.
- **Resources Used:**
  - Parrot Security OS (attacker machine)
  - Windows 11 (target machine with IP address: 10.10.1.11)
  - **Tools:** Nmap and Wireshark

---

## Introduction

The goal of this lab is to demonstrate methods to bypass IDS and firewall systems. Various techniques such as packet fragmentation, source port manipulation, and others were executed on the Parrot Security OS machine using Nmap. After each technique, the packets were analyzed on the Windows 11 machine using Wireshark to validate the results.

---

## Techniques and Results

### 1. Packet Fragmentation
- **Command:**  
  `nmap -f 10.10.1.11`

- **Description:**  
  Breaks down IP packets into smaller fragments that IDS/firewalls often ignore due to the resource complexity required for processing.

- **Results:**
  - Nmap successfully identified open ports and services on the target machine.
  - **Wireshark Analysis:** Fragmented packets were captured and displayed correctly.

---

### 2. Source Port Manipulation
- **Command:**  
  `nmap -g 80 10.10.1.11`

- **Description:**  
  Uses a commonly allowed port (HTTP/port 80) as the source port to bypass security rules and make traffic appear legitimate.

- **Results:**
  - Nmap displayed all open TCP ports and the services running on them, regardless of the active firewall.
  - **Wireshark Analysis:** Packets initiated with port 80 as the source port were visible.

---

### 3. MTU Size Adjustment
- **Command:**  
  `nmap -mtu 8 10.10.1.11`

- **Description:**  
  Reduces the packet size (MTU) to 8 bytes to bypass firewall filters and IDS detection mechanisms.

- **Results:**
  - The scans successfully retrieved the expected information about open ports without triggering security mechanisms.
  - **Wireshark Analysis:** Captured packets with a maximum size of 8 bytes were displayed correctly.

---

### 4. IP Address Decoy
- **Command:**  
  `nmap -D RND:10 10.10.1.11`

- **Description:**  
  Generates random source IP addresses to mask the actual scanner’s IP and make tracking by IDS more difficult.

- **Results:**
  - IDS was unable to determine the actual source IP; Nmap successfully identified open ports.
  - **Wireshark Analysis:** Multiple source IP addresses, including spoofed ones, were displayed.

---

### 5. MAC Address Spoofing
- **Command:**  
  `nmap -sT -Pn --spoof-mac 0 10.10.1.11`

- **Description:**  
  Alters the MAC address to disguise the traffic as legitimate user traffic and bypass security mechanisms.

- **Results:**
  - Nmap identified open ports without being blocked by IDS or firewalls.
  - **Wireshark Analysis:** Packets with spoofed MAC addresses were captured.

---

## Summary

- **Steps Taken:**
  1. Various Nmap techniques (e.g., fragmentation, source port manipulation) were successfully used to bypass security mechanisms.
  2. Results were validated on the target machine (Windows 11) using Wireshark after each technique.

- **Insights:**
  - IDS and firewalls have vulnerabilities that can be exploited through specialized techniques such as packet manipulation and spoofing.
  - Detailed information about open ports and services was retrieved despite the active firewall.

- **Recommendations:**
  - IDS and firewalls should be regularly updated and hardened to address known vulnerabilities.
  - Anomaly detection systems and advanced monitoring solutions should be implemented to identify unusual network activities.
  - Regular penetration testing is necessary to evaluate the effectiveness of security mechanisms.