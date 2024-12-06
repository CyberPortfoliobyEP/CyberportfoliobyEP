# Lab 6: Automation of Scans using ShellGPT and GitHub Integration

## Introduction

This lab demonstrates how to use ShellGPT to generate a Python script for an ICMP network scan, integrate it into a GitHub repository, and automate the process for seamless workflow management. By following this lab, you will learn how to use ShellGPT for scripting and manage your code with GitHub CLI.

---

## Lab Details

- **Lab Name:** Automation of Scans using ShellGPT and GitHub Integration
- **Environment:** Parrot Security OS (Virtual Machine)
- **Objective:** Automate the execution of network scans and integrate scripts into GitHub.
- **Target Subnet:** `10.10.1.0/24`
- **Tools Used:**
  - **ShellGPT:** AI-powered command and script generation.
  - **GitHub CLI:** To manage repositories and push changes.
  - **Python:** To execute the generated scripts.

---

## Prerequisites

1. A GitHub account with a repository already created (`CyberPortfolioByEP/AI` in this example).
2. Parrot Security OS with internet connectivity.
3. ShellGPT installed on the machine.
4. GitHub CLI installed. Run the following commands to install:

```bash
sudo apt update
sudo apt install gh
```
---

## Steps

### Step 1: Setting Up GitHub CLI

1. **Authenticate GitHub CLI:**
   - Run the following command:

```bash
gh auth login
```
   - Select `GitHub.com` and choose `HTTPS` as the protocol.
   - Use the **browser-based login** option:
     - Copy the one-time code displayed in the terminal.
     - Open the GitHub login page in your browser and enter the code to authorize.
   - Confirm successful authentication.

   ![Git Auth.](https://i.imgur.com/rziWXTC.png)
   ![Git Auth.](https://i.imgur.com/zezbDe2.png)
    
2. **Clone the Repository:**
   - Clone the repository into your local machine:

```bash
git clone https://github.com/CyberPortfolioByEP/CyberPortfolioByEP.git
```
   ![Git Clone](https://i.imgur.com/tfa1Xbg.png)
   
   - Navigate to the `AI` directory:

```bash
cd CyberPortfolioByEP/AI
```
---

### Step 2: Generate the ICMP Scan Script

1. **Use ShellGPT to Generate the Script:**
   - Run the following command:

```bash
sgpt --chat scan --shell "Generate a Python script to perform an ICMP scan on the subnet 10.10.1.0/24"
```
   - ShellGPT will create a Python script, saving it as `icmp_scan.py` in your current directory.
     
   ![Generate Script](https://i.imgur.com/KGzf8lA.png)

2. **Verify the Generated Script:**
   - Open the file using a text editor (e.g., `nano` or `pluma`):

```bash
nano icmp_scan.py
```
   - Ensure the script is correctly formatted and executable.

---

### Step 3: Move the Script into the GitHub Directory

1. **Move the Script:**

```bash
mv ~/icmp_scan.py ~/CyberPortfolioByEP/AI/
```
2. **Navigate to the Directory:**

```bash
cd ~/CyberPortfolioByEP/AI/
```

---

### Step 4: Commit and Push the Script to GitHub

1. **Stage the File:**

```bash
git add icmp_scan.py
```
2. **Commit the File:**
   - Open the commit editor:

```bash
git commit
```
   - Add a meaningful commit message (e.g., "Added ICMP scan script") and save.

3. **Push to GitHub:**

```bash
git push origin main
```
   ![Git push](https://i.imgur.com/jzG9K0F.png)

---

## Step 5: Execute the Script

1. **Run the Script:**
   - Execute the script to perform the ICMP scan:

```bash
python3 icmp_scan.py
```
2. **Verify the Output:**
   - Confirm that the script scans the specified subnet and displays active hosts.
     
   ![Automation script results](https://i.imgur.com/oBqWA5e.png)
   
---

## Summary

### Key Steps:

1. Authentication with GitHub CLI and cloning the repository.
2. Generating an ICMP scan script with ShellGPT.
3. Committing and pushing the script to GitHub via CLI.
4. Executing the script to verify functionality.
