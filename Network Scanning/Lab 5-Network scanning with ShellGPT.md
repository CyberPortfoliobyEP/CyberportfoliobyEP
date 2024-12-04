# Lab 5: Network Scanning with ShellGPT (SGPT)

## Lab Details

- **Lab Name:** Network Scanning with ShellGPT (SGPT)
- **Lab Environment:** EC-Council iLabs
- **Lab Objective:** Conduct ICMP scans, Host Discovery, XMAS scans, and Firewall/Operating System scans to identify vulnerabilities and system information.
- **Resources Used:**
  - **Attacker Machine:** Parrot Security OS
  - **Target Machine:** Windows 11 (IP Address: 10.10.1.11, Subnet: 10.10.1.0/24)
  - **Tools:**
    - **ShellGPT:** AI-powered network scanning tool
    - **Nmap:** Tool for specific network scans such as XMAS and firewall scans
- **Preparation:** The ShellGPT API must be integrated. Follow the instructions in "Integrate ShellGPT in Parrot Security Machine."

## Introduction

This lab demonstrates the use of ShellGPT for network scanning. The focus is on verifying the target machine's reachability via ICMP scans, identifying active hosts, performing XMAS scans, and conducting firewall/operating system scans to identify vulnerabilities and gather system information.


## Task 1: ICMP Scan
```bash
`sgpt --chat scan --shell "Use hping3 to perform ICMP scanning on the target IP address 10.10.1.11 and stop after 10 iterations"`
```
- **Description:** Hping3 is a flexible network tool capable of generating and sending custom packets. It was used to send specific ICMP packets to the target IP `10.10.1.11` to verify its reachability and measure response times.
- **Results:** All 10 ICMP packets were successfully answered. The average response time was 1.2 ms.

## Task 2: Host Discovery
```bash
`sgpt --chat scan --shell "Perform an XMAS scan on the first two targets from the file scan1.txt"`
```
- **Description:** Identifies active hosts in the subnet `10.10.1.0/24`. The IP addresses of the hosts are stored in `scan1.txt`.
- **Results:** Five active hosts were identified: `10.10.1.11`, `10.10.1.12`, `10.10.1.13`, `10.10.1.14`, `10.10.1.15`.

## Task 3: XMAS Scan
```bash
`sgpt --chat scan --shell "Perform an XMAS scan on the first two targets from the file scan1.txt"`
```
- **Description:** The XMAS scan sends specific TCP packets with the **FIN**, **PSH**, and **URG** flags to identify vulnerabilities such as unfiltered ports or open firewalls. Although the command specifies scanning the first two targets from `scan1.txt`, three IP addresses were scanned in this instance.
- **Results:** On `10.10.1.9` and `10.10.1.10`, no notable vulnerabilities were found. On `10.10.1.11`, two vulnerabilities were identified on:
  - Port 80 (HTTP)
  - Port 443 (HTTPS)

## Task 4: Firewall and Operating System Scan
```bash
`sgpt --chat scan --shell "Discover if there is any Firewall active on the subnet 10.10.1.0/24 and then find the list of the IP addresses of the firewalls and operating systems"`
```
- **Description:** Using ShellGPT and Nmap, active firewalls were detected, and attempts were made to identify operating systems. The results were saved in two files: `firewalls.txt` and `os_info.txt`.
- **Results:** 
  - **Firewalls Detected:**
    - `10.10.1.14`: Microsoft Windows 10 with an active Stateful Firewall.
    - `10.10.1.19`: FreeBSD 11.X.
  - **Operating Systems Identified:**
    - `10.10.1.11`: Linux 4.X/5.X.
    - `10.10.1.14`: Microsoft Windows 10.

## Summary

- **Steps:**
  1. ICMP scan to verify the target machine's reachability.
  2. Identification of active hosts in the subnet and saving them in `scan1.txt`.
  3. Execution of an XMAS scan on the first two IPs from `scan1.txt`.
  4. Execution of a firewall and operating system scan to detect firewalls and gather system details.

- **Results of the Scans:**
  - The ICMP scan confirmed the target machine's reachability.
  - The XMAS scan revealed vulnerabilities on ports 80 and 443 for `10.10.1.11`.
  - The firewall scan detected active Stateful Firewalls, particularly on Windows hosts.
  - The operating system analysis uncovered systems such as Linux and Windows.

- **Recommendations:**
Regularly perform network scans to identify vulnerabilities early. Improve firewall and security configurations to obscure OS details and minimize exposed ports.