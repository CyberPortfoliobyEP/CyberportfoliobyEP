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

### 1. DNS Lookup using nslookup
- **Command:**
  nslookup  
  server 10.10.1.22  
  set q=any  
  ceh.com  

- **Description:**
  Queries the DNS server for records of type "ANY" to obtain all available information.
- **Results:**
  The server returned an error message `SERVFAIL`. This indicates a failure in resolving DNS records. No useful information was retrieved.
- **Screenshot:** `1.png`

---

### 2. Advanced DNS Queries using dig
- **Command:**
  dig @10.10.1.22 ceh.com ANY  

- **Description:**
  Queries the DNS server for all record types for the domain `ceh.com`.
- **Results:**
  Successfully retrieved NS, SOA, and A records. Found:
  - NS Record: `server2022.ceh.com`
  - SOA Record: `hostmaster.ceh.com`
  - A Record: `10.10.1.22`
- **Screenshot:** `3-1.png`

---

### 3. DNS Enumeration with dnsenum
- **Command:**
  dnsenum --dnsserver 10.10.1.22 ceh.com  

- **Description:**
  Enumerates DNS records and tests zone transfers while attempting to brute-force subdomains using a predefined wordlist.
- **Results:**
  - Found the DNS server: `server2022.ceh.com`
  - Detected additional subdomain: `adserver.ceh.com` with IP `10.10.1.20`.
  - Zone transfer failed (`AXFR record query failed`).
- **Screenshot:** `3-2.png`

---

### 4. Subdomain Discovery with Fierce
- **Command:**
  fierce --domain ceh.com --dns-servers 10.10.1.22  

- **Description:**
  A reconnaissance tool used for locating non-contiguous IP spaces by testing for subdomains and DNS vulnerabilities.
- **Results:**
  - Found subdomain: `adserver.ceh.com` at `10.10.1.20`.
  - Zone transfer attempts returned failures.
- **Screenshot:** `3-3.png`

---

### 5. Subdomain Brute-Forcing with Gobuster
- **Command:**
  gobuster dns -d ceh.com -w /usr/share/dirb/wordlists/common.txt  

- **Description:**
  Uses a wordlist to brute-force subdomains in the domain `ceh.com`.
- **Wordlist Content:**
  The wordlist `/usr/share/dirb/wordlists/common.txt` contains common directory and subdomain names such as `.config`, `.git`, `ftp`, `mail`, `webmail`.
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
- **Screenshot:** `gobuster.png`

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