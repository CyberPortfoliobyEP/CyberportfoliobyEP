# Lab Report: HTTP/HTTPS Enumeration for Web Servers

## Lab Details

- **Lab Name:** HTTP/HTTPS Enumeration for Web Servers
- **Lab Environment:** Parrot Security OS (attacker machine) and Windows 11 (target machine)
- **Objective:** Discover web server vulnerabilities and directories
- **Resources:**
  - Parrot Security VM
  - Windows 11 VM
  - Web server with IP address: `10.10.1.22`
  - **Tools:**
    - Gobuster
    - Nikto
    - Curl
    - FFuF

## Introduction

The objective of this lab is to identify potential vulnerabilities and directories on a web server. Tools such as Gobuster, Nikto, Curl, and FFuF are employed to pinpoint potential attack vectors. The results are analyzed to determine potential follow-up actions.

---

## Techniques and Results

### 1. Directory Bruteforcing with Gobuster

**Command:**
gobuster dir -u http://10.10.1.22 -w /usr/share/dirb/wordlists/common.txt

**Description:**
Gobuster was used to discover potential directories and files on the web server by iterating through a wordlist and analyzing HTTP status codes like `200`, `301`, `401`, and `403`.

**Results:**
- **Identified Directories:**
  - `/aspnet_client` (Status: 301)
  - `/rpc` (Status: 401)
- **Interpretation:**
  - The `/aspnet_client` directory may contain ASP.NET-specific files.
  - The `401` status for `/rpc` indicates that authentication is required.

**Next Steps:**
- Attempt authentication against `/rpc` if credentials are available.
- Inspect `/aspnet_client` for configuration files or vulnerabilities.

---

### 2. Vulnerability Scanning with Nikto

**Command:**
nikto -h https://10.10.1.22

**Description:**
Nikto was used to identify general web server vulnerabilities and insecure configurations.

**Results:**
- No specific vulnerabilities were identified.
- Nikto did not provide any relevant output.

**Next Steps:**
- Use additional tools (e.g., Nessus or OpenVAS) for more comprehensive scans.
- Perform manual checks on the server.

---

### 3. Manual Header Analysis with Curl

**Command:**
curl -I http://10.10.1.22

**Description:**
Curl was used to retrieve HTTP headers from the web server and extract information such as server versions or technologies in use.

**Results:**
- **Server:** Microsoft-IIS/10.0
- **X-Powered-By:** ASP.NET
- **Additional Information:** The web server is running Microsoft IIS with ASP.NET.

**Next Steps:**
- Investigate vulnerabilities in the identified Microsoft IIS version.
- Examine ASP.NET-specific security issues.

---

### 4. Directory Bruteforcing with FFuF

**Command:**
ffuf -u http://10.10.1.22/FUZZ -w /usr/share/dirb/wordlists/common.txt

**Description:**
FFuF was employed to discover directories on the web server. It supports multithreading and is optimized for fast scans.

**Results:**
- **Identified Directories:**
  - `/aspnet_client` (Status: 200)
  - `/rpc` (Status: 401)
- **Interpretation:**
  - `/aspnet_client`: Access is possible; content should be examined.
  - `/rpc`: Access is restricted.

**Next Steps:**
- Test `/rpc` with valid credentials.
- Analyze `/aspnet_client` for files and potential vulnerabilities.

---

## Summary

- **Steps Taken:**
  - Directory bruteforcing using Gobuster and FFuF.
  - Header analysis using Curl.
  - Vulnerability scanning with Nikto.
- **Findings:**
  - Directories such as `/aspnet_client` and `/rpc` were identified.
  - The web server is running Microsoft IIS/10.0 with ASP.NET.
  - No specific vulnerabilities were found using Nikto.
- **Recommendations:**
  - Inspect `/aspnet_client` and `/rpc` for potential vulnerabilities.
  - Perform further scans with specialized tools.
  - Ensure regular updates and patches for the web server.

---