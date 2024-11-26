# Footprinting using Netcraft and DNSDumpster

## Host System

- **Device:** MacBook Air (M1, 2020)
- **Processor:** Apple M1
- **RAM:** 8 GB
- **Operating System:** macOS Sequoia 15.1.1
- **Browser:** Mozilla Firefox (used for all tasks)

## Virtual Machine

- **Software:** UTM (QEMU-based)
- **Guest OS:** Parrot Security OS

## Lab Objective

This lab demonstrates the process of extracting domain and subdomain information of a target organization using tools like Netcraft and DNSDumpster. The collected data can be used for reconnaissance purposes, enabling further penetration testing such as web application and network attacks.

---

## Steps Performed

### Task 1: Using Netcraft to Find Subdomains

1. **Navigate to Netcraft**  
   Open Mozilla Firefox and go to Netcraft.

2. **Access the Site Report Tool**  
   - Click on the menu icon in the top-right corner of the page and navigate to `Resources -> Research Tools`.
   - Select `Site Report`.

  ![Alternativtext](https://i.imgur.com/ebBmO7k.png)

3. **Run a Site Report**  
   - Enter the URL `https://www.certifiedhacker.com` in the "What’s that site running?" search box and click `LOOK UP`.

   ![Site Report Placeholder](images/netcraft_site_report.png)

4. **Extract Information**  
   - Review the results on the site report page.
   - Information such as background, hosting history, network details, and subdomains is displayed.

5. **View Subdomains**  
   - In the Network section, click on the target domain (`certifiedhacker.com`) to view a list of subdomains.
   - The results include subdomains, operating systems, and netblocks.

   ![Subdomain Placeholder](images/netcraft_subdomains.png)

---

### Task 2: Using DNSDumpster to Map DNS and Host Information

1. **Navigate to DNSDumpster**  
   - Open a new tab in Mozilla Firefox and go to DNSDumpster.
   - Enter the target domain `certifiedhacker.com` in the search box and click `Start Test`.

   ![DNSDumpster Placeholder](images/dnsdumpster_start_test.png)

2. **Extract GeoIP and DNS Records**  
   - Scroll down to view:
     - DNS Servers
     - MX Records
     - Host Records (A)
     - IP Addresses

   ![DNS Records Placeholder](images/dns_records.png)

3. **Analyze Domain Mapping**  
   - Review the domain mapping diagram provided by DNSDumpster.
   - Use the `Download .xlsx` option to save the list of hosts.

   ![Domain Mapping Placeholder](images/dns_mapping.png)

4. **Analyze Downloaded Data**  
   - Open the downloaded `.xlsx` file in LibreOffice.  
     The Excel sheet displays the details such as Hostname, IP Address, Reverse DNS, Netblock Owner, Country, HTTP Title, etc.

---

## Key Learnings

Through this lab, I gained the following skills and insights:

1. **Reconnaissance Using Internet Research Tools**
   - Learned to extract domains, subdomains, and DNS records using Netcraft and DNSDumpster.
   - Understood the role of such tools in identifying attack vectors for web application and network attacks.

2. **Data Analysis and Interpretation**
   - Interpreted domain mapping, network infrastructure, and DNS records.
   - Identified potential subdomains that could be targeted for further penetration testing.

3. **Tool Utilization**
   - Mastered the use of Netcraft for web infrastructure analysis.
   - Utilized DNSDumpster to visualize DNS data and download host information for offline analysis.

4. **Documentation and Reporting**
   - Structured findings and screenshots for clear presentation and reproducibility.
