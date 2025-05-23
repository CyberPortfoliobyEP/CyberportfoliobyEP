# Lab Report: DNS Enumeration

## Lab Details
- **Lab Name:** DNS Enumeration
- **Lab Environment:** Parrot Security OS
- **Lab Goal:** Enumerate DNS records, discover subdomains, and investigate DNS vulnerabilities using various tools.
- **Resources Used:**
  - Parrot Security OS (attacker machine)
  - DNS server: 10.10.1.22
  - Tools: nslookup, dig, dnsenum, Fierce, and Gobuster

---

## Introduction
The objective of this lab is to explore and utilize different tools for DNS enumeration. The techniques employed aim to extract DNS records, identify subdomains, and test zone transfers to gather critical information. This lab emphasizes the steps taken from an attacker’s perspective without prior knowledge of the DNS infrastructure.

---

## Conducted Techniques and Results

## 1. DNS Server Lookup

### Objective:
Determine if the DNS server `10.10.1.22` is responsive and can resolve queries for the domain `ceh.com`.

### Command:
```bash
nslookup ceh.com 10.10.1.22
```
### Result:
From the screenshot:
- The query successfully resolved the domain `ceh.com` using the DNS server `10.10.1.22`.
- The server returned the following information:
  - **Name**: ceh.com
  - **Address**: 10.10.1.22
    
![Results](https://i.imgur.com/Xk6Qina.png)

### Explanation for Lack of Detailed Results:
- The DNS server provided basic resolution (domain name to IP address) but did not return detailed DNS record types (e.g., MX, TXT, or CNAME records). 
- This could be due to:
  - Limited permissions or restrictions on the queried DNS server.
  - The absence of additional DNS records configured for the domain.
  - The DNS server only hosting minimal configuration for resolving the primary domain.
---

### 2. Advanced DNS Queries using dig
- **Command:**
```bash
  dig @10.10.1.22 ceh.com ANY  
```
- **Description:**
  Queries the DNS server for all record types for the domain `ceh.com`.
- **Results:**
  Successfully retrieved NS, SOA, and A records. Found:
  - NS Record: `server2022.ceh.com`
  - SOA Record: `hostmaster.ceh.com`
  - A Record: `10.10.1.22`
    
![Results](https://i.imgur.com/u3VQfgR.png)
---

### 3. DNS Enumeration with dnsenum
- **Command:**
```bash
  dnsenum --dnsserver 10.10.1.22 ceh.com  
```
- **Description:**
  Enumerates DNS records and tests zone transfers while attempting to brute-force subdomains using a predefined wordlist.
- **Results:**
  - Found the DNS server: `server2022.ceh.com`
  - Detected additional subdomain: `adserver.ceh.com` with IP `10.10.1.20`.
  - Zone transfer failed (`AXFR record query failed`).

![Results](https://i.imgur.com/u3FlQs4.png)
---

### 4. Subdomain Discovery with Fierce
- **Command:**
```bash
  fierce --domain ceh.com --dns-servers 10.10.1.22  
```
- **Description:**
  A reconnaissance tool used for locating non-contiguous IP spaces by testing for subdomains and DNS vulnerabilities.
- **Results:**
  - Found subdomain: `adserver.ceh.com` at `10.10.1.20`.
  - Zone transfer attempts returned failures.
![Results](https://i.imgur.com/BZyGkEr.png)

---

### 5. Subdomain Brute-Forcing with Gobuster
- **Command:**
```bash
  gobuster dns -d ceh.com -w /usr/share/dirb/wordlists/common.txt  
```
- **Description:**
  Uses a wordlist to brute-force subdomains in the domain `ceh.com`.
- **Wordlist Content:**
  The wordlist `/usr/share/dirb/wordlists/common.txt` contains common directory and subdomain names such as `.config`, `.git`, `ftp`, `mail`, `webmail`.
![Results](https://i.imgur.com/TrXbkAm.png)
![Results](https://i.imgur.com/TY2MkEL.png)

- **Results:**
  - Found multiple subdomains:
    - `e.ceh.com`
    - `email.ceh.com`
    - `ftp.ceh.com`
    - `mail.ceh.com`
    - `pop.ceh.com`
    - `smtp.ceh.com`
    - `webmail.ceh.com`
    - `www.ceh.com`

---

## Summary
- **Conducted Steps:**
  1. DNS queries and lookups using nslookup and dig were performed to extract basic DNS information.
  2. DNS enumeration tools like dnsenum and Fierce were used to discover subdomains and test zone transfers.
  3. Subdomain brute-forcing was successfully conducted using Gobuster with a common wordlist.

- **Insights:**
  - The DNS server revealed multiple subdomains and valid records.
  - Zone transfer attempts were unsuccessful, indicating a configured security measure against unauthorized transfers.
  - Brute-forcing with Gobuster proved effective in identifying hidden subdomains.

- **Recommendations:**
  - Disable public-facing zone transfers to prevent data leakage.
  - Employ rate-limiting and monitoring to detect and block brute-force attacks.
  - Regularly audit DNS configurations and minimize exposed records.
