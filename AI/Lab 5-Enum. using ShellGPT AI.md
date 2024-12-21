# Lab: General Enumeration Using ShellGPT with Parrot Security OS

---

## Lab Details
- **Infrastructure**: Parrot Security OS (Attacker Machine), Windows Server 2022 (Target Machine)
- **Purpose**: Perform enumeration tasks to discover and analyze subdomains, DNS records, and HTTP headers using ShellGPT.
- **Tools Used**: ShellGPT with Gobuster, Metasploit, Curl.
- **Target Machine IP**: `10.10.1.22`
- **Domain**: `ceh.com`

---

## Tasks and Execution

### Task 1: Subdomain Enumeration

**Command:**
```bash
sgpt --chat scan --shell "enumerate with gobuster for subdomains on the domain ceh.com"
```
**Execution Details**:  
ShellGPT processed the query and executed a Gobuster command for subdomain enumeration.

**Command executed from SGPT**:
```bash  
gobuster dns -d ceh.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50
```
**Explanation of Command**:  
- `dns`: Specifies that Gobuster should perform DNS enumeration.
- `-d ceh.com`: The domain to enumerate subdomains for.
- `-w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`: The wordlist to use for bruteforcing subdomains.
- `-t 50`: Sets the number of concurrent threads to 50, improving speed.

![img](https://i.imgur.com/lA2K1Zj.png)

**Results**:  
Subdomains identified:
1. email.ceh.com
2. ftp.ceh.com
3. webmail.ceh.com

**Interpretation**:  
- **email.ceh.com**: Likely used for email communications. Could be checked for open ports or vulnerable email services.
- **ftp.ceh.com**: Indicates an FTP server. Requires further exploration for authentication bypass or file access.
- **webmail.ceh.com**: Potentially a webmail service. Might contain credentials if improperly secured.

**Next Steps**:  
- Perform detailed enumeration on each subdomain.
- Analyze open ports and services for possible vulnerabilities.

---

### Task 2: DNS Enumeration

**Command**:
```bash
sgpt --chat scan --shell "perform enumerating on the domain ceh.com using metasploit"
```
**Execution Details**:  
ShellGPT processed the query and executed a Metasploit auxiliary module for DNS enumeration.

**Command utilized from SGPT**:  
```bash
use auxiliary/gather/enum_dns  
set DOMAIN ceh.com  
run
```

![img](https://i.imgur.com/sGn4t5a.png)

**Results**:  
DNS records discovered:
1. ceh.com NS ns07.domaincontrol.com
2. ceh.com MX aspmx3.googlemail.com
3. ceh.com TXT google-site-verification

**Interpretation**:  
- **NS Records**: Shows the authoritative name servers for the domain.
- **MX Records**: Reveals mail servers, indicating email infrastructure.
- **TXT Records**: May include security or verification information.

**Next Steps**:  
- Query mail servers for potential misconfigurations.
- Investigate TXT records for security-related information.

---

### Task 3: HTTP Header Analysis

**Command**:
```bash
sgpt --chat scan --shell "analyze the HTTP header and interpret the results for http://10.10.1.22"
``
**Execution Details**:  
ShellGPT processed the query and used Curl for analyzing HTTP headers.

**Command utilized from SGPT**:  
```bash
curl -I http://10.10.1.22
```

[img](https://i.imgur.com/0p82TpR.png)

**Results**:  
HTTP headers retrieved:
- Server: Microsoft-IIS/10.0
- X-Powered-By: ASP.NET

**Interpretation**:  
- **Microsoft-IIS/10.0**: Indicates the web server and version, which can be checked for known vulnerabilities.
- **ASP.NET**: Suggests the use of ASP.NET framework, which could have misconfigurations.

**Next Steps**:  
- Use specific tools to check for vulnerabilities in Microsoft IIS/10.0.
- Investigate ASP.NET applications for potential weaknesses.

---

## Summary

### Steps Taken:
1. Subdomain enumeration using Gobuster.
2. DNS record enumeration using Metasploit.
3. HTTP header analysis using Curl.

### Findings:
- Subdomains such as email.ceh.com, ftp.ceh.com, and webmail.ceh.com were identified.
- DNS records revealed NS, MX, and TXT entries.
- HTTP headers indicated the server is running Microsoft-IIS/10.0 with ASP.NET.

### Recommendations:
- Perform detailed scans on identified subdomains.
- Investigate discovered DNS records for further enumeration.
- Check for known vulnerabilities in Microsoft-IIS/10.0 and ASP.NET applications.
- Regularly update and patch web servers and DNS configurations.