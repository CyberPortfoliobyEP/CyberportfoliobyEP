
# Lab Report: Footprinting with Social Media Research Tools

## Introduction

The goal of this lab was to collect personal and professional information about employees of a target organization. Using social media platforms, publicly accessible data was extracted, which could potentially be used for attacks such as social engineering or other targeted actions. This lab demonstrates how an ethical hacker systematically collects, analyzes, and securely stores such information.

---

## Technical Environment and Tools

### Virtual Machine: Kali Linux

- **Name:** E. Popal LAB – Debian Kali
- **Operating System:** Debian 12.x (64-Bit ARM)
- **Processor:** 2 CPU Cores
- **RAM:** 2048 MB (2 GB RAM)
- **Disk Space:** 15 GB
- **Snapshots:** 2 GB

### Tools Used

1. **Sherlock:** A Python-based open-source framework for social media research.
2. **Social Searcher:** An online service for analyzing and searching social media content.

---

## Steps and Results

### Task 1: Preparing the Environment

1. **Start the Kali Linux VM**  
   - Launch the virtual machine to create an isolated and secure environment.  

2. **Activate Root Access**  
   - Use the following command to enable root access:
     ```bash
     sudo su
     ```

---

### Task 2: Installing Sherlock

1. **Install Sherlock**  
   - Run the following command to install the tool using the `apt` package manager:
     ```bash
     apt install sherlock
     ```

2. **Verify Installation**  
   - Use the following command to check if Sherlock is installed and functional:
     ```bash
     sherlock --help
     ```

---

### Task 3: Running Sherlock

1. **Execute Sherlock**  
   - Search for social media profiles by providing the target name:
     ```bash
     sherlock "Thomas Müller"
     ```

2. **Analyze Results**  
   - Review the results in the terminal, which include platform names and URLs for profiles associated with "Thomas Müller."

3. **Save Results to a File**  
   - Use the following command to save the results to a text file on the Desktop:
     ```bash
     touch ~/Desktop/results_thomas_mueller.txt
     ```

4. **Run Sherlock with Output to File**  
   - Save the results directly in the file:
     ```bash
     sherlock "Thomas Müller" --output ~/Desktop/results_thomas_mueller.txt
     ```

5. **Verify the File**  
   - Check the file's content using:
     ```bash
     cat ~/Desktop/results_thomas_mueller.txt
     ```

---

### Task 4: Additional Search with Social Searcher

1. **Access Social Searcher**  
   - Open the Social Searcher website in a web browser.

2. **Search for Target**  
   - Input "Thomas Müller" into the search box and apply filters for platforms (e.g., Twitter, Instagram) and time ranges (e.g., last 30 days).

3. **Analyze Results**  
   - Review the output, including posts and links to public profiles mentioning the target.

---

## Key Learnings

1. **Effective Use of Sherlock**  
   - Sherlock simplifies the process of finding social media profiles and structuring collected information.

2. **Importance of Result Storage**  
   - Storing results in a text file ensures easy documentation and future reference.

3. **Supplemental Tools**  
   - Social Searcher provides additional insights into trends and activities across social media platforms.

4. **Secure Environment**  
   - Using an isolated virtual machine ensures data integrity and protects against leaks.

---

## Conclusion

This lab demonstrated how publicly accessible data from social media platforms can be collected, analyzed, and securely stored. Combining Sherlock and Social Searcher provides a comprehensive approach to extracting and documenting target information. This highlights the importance of structured data storage and secure workflows in the reconnaissance phase.
