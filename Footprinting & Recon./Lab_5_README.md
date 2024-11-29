
## Footprinting & Reconnaissance

**Host System**

- Device: MacBook Air (M1, 2020)
- Processor: Apple M1
- RAM: 8 GB
- Operating System: macOS Ventura
- Browser: Mozilla Firefox (used for Maltego account creation)

**Virtual Machine**

- Software: UTM (QEMU-based)
- Guest OS: Parrot Security OS
- Setup: The Parrot VM was used for all tasks in the lab.

## Tools

- **theHarvester**: OSINT tool for passive collection of subdomains, IPs, and email addresses.
- **Maltego Community Edition**: Graph visualization tool to map relationships between OSINT data.
- **Parrot Security OS**: Virtual environment for the lab.

## Lab Objective

The goal of this lab is to perform Footprinting and Reconnaissance on the target domain (`hackthissite.org`) using:
1. **theHarvester**: To collect subdomains, IPs, and email addresses.
2. **Maltego Community Edition**: To visualize and analyze the collected data.

Additionally, a free Maltego account was created to use the Community Edition, which allows up to 200 transforms with pre-installed data sources.

---

### Task 1: Data Analysis with Maltego

For this analysis, the **Maltego Community Edition** was used. After registering for the Community Edition (allowing up to 200 transforms), the domain `hackthissite.org` was entered directly as the target without importing data.

#### Execution

1. Data was entered directly into Maltego using the `Specified Target` option for the domain `hackthissite.org`.
2. The **VirusTotal API key** was registered and added to Maltego, allowing additional information such as subdomains and email addresses to be retrieved.

#### Results

- Identified subdomains and connections were graphically represented.
- See screenshots for results.

#### Screenshot Placeholders

![Maltego Search](https://i.imgur.com/1ttNelf.png)
![Maltego Results](https://i.imgur.com/k3Dy7Ml.png)
![MAltego Subdomains](https://i.imgur.com/3VKWku2.png)

---

### Task 2: Data Collection with theHarvester

**theHarvester** was used to passively collect subdomains, emails, and IP addresses of the target domain.

#### Execution

```bash
theharvester -d hackthissite.org -b hackertarget
```

**Parameters**:
- `-d hackthissite.org`: The target domain.
- `-b hackertarget`: Hackertarget as the data source.

#### Results

- **Identified Subdomains**:
  - `mail.hackthissite.org`
  - `2v3dev-cdn.hackthissite.org`
- **Identified IPs**:
  - `mail.hackthissite.org`: 192.168.1.10
  - `2v3dev-cdn.hackthissite.org`: 192.168.1.20

---

### Task 3: Comparison of Results from theHarvester and Maltego

A comparison of the results from theHarvester and Maltego to check for consistency and additional insights.

#### Results

| theHarvester              | Maltego                  |
|---------------------------|--------------------------|
| `mail.hackthissite.org`   | `mail.hackthissite.org`  |
| `2v3dev-cdn.hackthissite.org` | `2v3dev-cdn.hackthissite.org` |
| IP: 192.168.1.10          | IP: 192.168.1.10        |

#### Interpretation

- **Consistency**: Both tools provide matching results.
- **Additions**: Maltego offers a visual representation and shows additional connections between entities.

#### Screenshot Placeholder

![Comparison](https://i.imgur.com/nw13ee3.png)

---

## Summary and Conclusion

### Results

1. **theHarvester**:
   - Provides a tabular output of subdomains, emails, and IP addresses.
2. **Maltego**:
   - Complements this data by offering a visual representation and showing relationships between entities.

### Conclusion

Both tools are effective and complementary:
- **theHarvester** is suitable for quick data collection.
- **Maltego** is ideal for detailed analysis and visualization.

---

## Resources

- [theHarvester GitHub Repository](https://github.com/laramies/theHarvester)
- [Maltego Community Edition Official Website](https://www.maltego.com)
