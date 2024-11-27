
# Lab Report: Whois Footprinting with DNS Recon

## Host System
- **Device:** MacBook Air (M1, 2020)
- **Processor:** Apple M1
- **RAM:** 8 GB
- **Operating System:** macOS Sequoia 15.1.1
- **Browser:** Mozilla Firefox

## Virtual Machine
- **Software:** UTM (QEMU-based)
- **Guest OS:** Parrot Security OS

## Lab Objective
The objective of this lab is to gather information about target domains using Whois and DNS Recon. These tools assist in analyzing networks, domain registrations, and DNS data. The collected information provides insights for further testing and security assessments.

## Task 1: Whois Lookup

### Execution via Terminal
```bash
whois www.certifiedhacker.com
```
**Results:**  
The query returned no data. The command displayed the message "No match for 'WWW.CERTIFIEDHACKER.COM'." This indicates that no information about this domain was found in the standard Whois database.

![Screenshot Placeholder](URL_TO_SCREENSHOTS)

### Execution via Web Browser
A Whois lookup was performed using the DomainTools website:  
[https://whois.domaintools.com](https://whois.domaintools.com)

**Screenshots:**  
1. **Search Interface**:  
   ![Screenshot Placeholder](URL_TO_SCREENSHOTS)  
   **Description:** Displays the search interface of DomainTools where the domain was entered. Options like "Monitor Domain Properties" and "Reverse IP Address Lookup" provide capabilities for reverse engineering.

2. **Detailed View**:  
   ![Screenshot Placeholder](URL_TO_SCREENSHOTS)  
   **Description:** Shows additional information such as admin emails and technical contacts, which are useful for reconnaissance.

---

## Task 2: DNS Recon

### Preparation
If the tool was not pre-installed, it was installed using the following commands:
```bash
sudo apt update
sudo apt install dnsrecon
```

### Execution
DNS Recon was executed with the following command:
```bash
dnsrecon -d certifiedhacker.com
```

**Results:**  
- **DNSSEC**: Not configured for the domain, indicating a lack of additional security measures for DNS entries.  
- **Nameservers (NS)**: `ns1.bluehost.com` and `ns2.bluehost.com`.  
- **MX Records**: Mail server `mail.certifiedhacker.com`.  
- **SRV Records**: 12 SRV entries were found, including services like `_autodiscover._tcp` and `_caldav._tcp`.

![Screenshot Placeholder](URL_TO_SCREENSHOTS)  
**Description:**  
The screenshot shows the command output. The identified SRV records provide insights into applications or configurations that could be targeted for further testing.

---

## Key Learnings

1. **Complementary Tools**  
   Whois provides basic registration details, while DNS Recon offers deeper technical insights.

2. **Identifying Potential Vulnerabilities**  
   Analysis of SRV records and DNSSEC configurations can reveal attack vectors.

3. **Understanding Data Sources**  
   Web tools like DomainTools offer extended access to information not available through local queries.

---

## Conclusion
This lab highlights the importance of using different tools such as Whois and DNS Recon. While Whois provides basic information, DNS Recon extends the analysis with technical DNS data. Combining these tools enables a comprehensive security assessment.

