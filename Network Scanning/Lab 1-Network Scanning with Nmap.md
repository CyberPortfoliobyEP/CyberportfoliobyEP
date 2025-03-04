# Host Discovery with Nmap

## Lab Details

- **Lab Name**: Performing Host Discovery
- **Lab Environment**: EC-Council iLabs
- **Lab Goal**: Identify active hosts in a target network using various Nmap scanning techniques.

## Tools and Environment

- **Virtual Machine**: Parrot Security OS (provided by EC-Council iLabs)
- **Tool Used**: Nmap

---

## Objective

The goal of this lab was to identify active hosts in a target network using multiple Nmap techniques. The results provide a basis for further network analysis and security evaluations.

---

## Procedures and Results

### 1. ARP Ping Scan

- **Command**:  
  `nmap -sn -PR 10.10.1.22`
- **Description**: Sends ARP requests to the target IP. An ARP reply indicates that the host is active.
- **Result**: Host `10.10.1.22` was identified as active.
  
     ![Results](https://i.imgur.com/CyWMg7X.png)
  
---

### 2. UDP Ping Scan

- **Command**:  
  `nmap -sn -PU 10.10.1.22`
- **Description**: Sends UDP packets to the target IP. A response indicates that the host is active.
- **Result**: Host `10.10.1.22` responded successfully.


     ![Results](https://i.imgur.com/z0fcP3D.png)
---

### 3. ICMP ECHO Ping Scan

- **Command**:  
  `nmap -sn -PE 10.10.1.22`
- **Description**: Sends ICMP ECHO requests to the target IP. An ICMP ECHO reply indicates that the host is active.
- **Result**: Host `10.10.1.22` was successfully identified as active.

     ![Results](https://i.imgur.com/sAc9Dip.png)

---

### 4. ICMP ECHO Ping Sweep

- **Command**:  
  `nmap -sn -PE 10.10.1.10-23`
- **Description**: Tests multiple IPs simultaneously. Active hosts respond with ICMP ECHO replies.
- **Result**: Active hosts identified:  
  - `10.10.1.15`  
  - `10.10.1.18`  
  - `10.10.1.22`

     ![Results](https://i.imgur.com/Xz9YQKt.png)

---

### 5. ICMP Timestamp Ping Scan

- **Command**:  
  `nmap -sn -PP 10.10.1.22`
- **Description**: Queries the current time from the target host via ICMP Timestamp. Useful when ICMP ECHO is blocked.
- **Result**: Host `10.10.1.22` responded successfully.

  ![Results](https://i.imgur.com/MxUOeFJ.png)

---

## Supplementary Techniques

### 6. ICMP Address Mask Ping Scan

- **Command**:  
  `nmap -sn -PM 10.10.1.22`
- **Description**: Searches for hosts using an alternative ICMP Ping technique with address masks.
- **Result**: Host `10.10.1.22` was identified.

---

### 7. TCP SYN Ping Scan

- **Command**:  
  `nmap -sn -PS 10.10.1.22`
- **Description**: Sends TCP SYN packets to target ports. A SYN+ACK response indicates an active host.
- **Result**: Host `10.10.1.22` was successfully identified as active.

---

### 8. TCP ACK Ping Scan

- **Command**:  
  `nmap -sn -PA 10.10.1.22`
- **Description**: Sends empty TCP-ACK packets. An RST response indicates an active host.
- **Result**: Host `10.10.1.22` was successfully identified.

---

### 9. IP Protocol Ping Scan

- **Command**:  
  `nmap -sn -PO 10.10.1.22`
- **Description**: Examines various IP protocol responses from the target host.
- **Result**: Host `10.10.1.22` was successfully identified.

---

## Results and Key Learnings

- **Combining Techniques**: Primary techniques (ARP, ICMP) were quick and efficient. Supplementary techniques (e.g., TCP SYN Scan) provided additional reliability, especially in networks with restricted ICMP traffic.
- **Nmap's Effectiveness**: Nmap proved to be an extremely versatile and accurate tool for identifying active hosts.
