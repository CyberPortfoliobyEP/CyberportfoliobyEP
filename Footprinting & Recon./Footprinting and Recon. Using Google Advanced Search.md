# Footprinting and Reconnaissance Using Google Advanced Search

## Lab Objective
The goal of this lab was to demonstrate the process of footprinting as part of the reconnaissance phase in ethical hacking. The aim was to use advanced search engine techniques to gather publicly available information about a target organization.

---

## Host System
- **Device:** MacBook Air (M1, 2020)
- **Processor:** Apple M1
- **RAM:** 8 GB
- **Operating System:** macOS Sequoia 15.1.1

---

## Virtual Machine: Parrot Security OS
- **Software:** UTM (QEMU-based)
- **Guest OS:** Parrot Security OS (Version 6.2 Lorikeet)
- **Web Browser:** Mozilla Firefox (used for all searches)
- **Default Login Credentials:**
  - Username: `parrot`
  - Password: `parrot`
- **Network Configuration:**
  - Mode: Isolated Network (Gemeinsames Netzwerk in UTM)

### Steps to Set Up the VM
1. **Download Parrot Security OS:**
   - Official source: [Parrot Security](https://parrotsec.org/).
   - Chose the UTM-compatible version for ARM processors.
   - Verified the file hash for integrity.
2. **Virtual Machine Configuration:**
   - Allocated 2 CPU cores, 4 GB RAM, and 20 GB disk space.
   - Used UTM to emulate an isolated networking environment to ensure security.
3. **Installation:**
   - Parrot OS was installed as the guest OS.
   - Mozilla Firefox was pre-installed and configured as the primary browser.

---

## Reconnaissance Using Google Advanced Search

### Search Tasks and Techniques

#### Identifying Login Pages
- **Search Query:** `intitle:login site:eccouncil.org`
- **Description:**
  - Used the `intitle` operator to find pages containing "login" in their title.
  - Limited the search to the domain `eccouncil.org` using the `site` operator.
- **Outcome:** Multiple login pages (e.g., frontend, iLabs) were identified. These could be used for penetration testing or assessing vulnerabilities.
  
![Screenshot showing identified login pages]

#### Searching for Publicly Available Documents
- **Search Query:** `filetype:pdf ceh site:eccouncil.org`
- **Description:**
  - Used the `filetype` operator to find PDF files on the `eccouncil.org` domain.
  - Searched specifically for documents related to "CEH" (Certified Ethical Hacker).
- **Outcome:** Found sensitive documents like the CEH course brochure, which can provide insights into an organization’s products, structure, and potential vulnerabilities.

![Screenshot showing search results for CEH documents]

---

## Additional Google Operators Used (with Examples)
- **intitle:** Searches for pages with specific terms in the title.
  - **Example:** `intitle:login site:eccouncil.org`
- **filetype:** Filters results by specific file types (e.g., PDFs, DOCs).
  - **Example:** `filetype:pdf ceh site:eccouncil.org`
- **cache:** Displays the cached version of a webpage stored by Google.
  - **Example:** `cache:www.eccouncil.org`
- **inurl:** Searches for specific terms in the URL of a webpage.
  - **Example:** `inurl:admin site:eccouncil.org`
- **related:** Shows websites similar to or related to a given domain.
  - **Example:** `related:www.eccouncil.org`
- **info:** Retrieves information about a specific webpage.
  - **Example:** `info:www.eccouncil.org`

---

## Key Learnings
Through this lab, I gained the following skills and knowledge:

1. **Advanced Search Techniques:**
   - Learned to use Google operators like `intitle`, `filetype`, and `cache` to extract valuable information.
   - Understood the importance of search queries in reconnaissance during penetration testing.

2. **Reconnaissance and Footprinting:**
   - Practiced gathering publicly available data to assess an organization’s online footprint.
   - Identified login pages and public documents as potential attack vectors.

3. **Virtual Environment Setup:**
   - Configured an isolated Parrot OS virtual environment using UTM.
   - Used Mozilla Firefox as the primary browser for controlled web reconnaissance.

4. **Documentation and Reporting:**
   - Structured and documented the process clearly and reproducibly.
   - Included screenshots to enhance the report’s professionalism.

---

## Screenshots and References
1. **Screenshots:**
   - Parrot Security OS setup in UTM.
   - Google searches using advanced operators (`intitle`, `filetype`).
2. **References:**
   - Parrot Security OS: [Download Link](https://parrotsec.org/).
   - Google Advanced Operators: [Documentation](https://support.google.com/websearch/answer/2466433).