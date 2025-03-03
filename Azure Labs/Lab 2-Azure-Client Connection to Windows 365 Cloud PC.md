# Lab Report - Client Connection to Windows 365 Cloud PC

## 1. Using the Windows 365 Client App

In this section, I will describe how I connected to my Cloud PC using the Windows 365 Client App. Instead of accessing the Cloud PC through a web browser, I decided to use the local Windows 365 Client App for a more seamless experience.

### Steps I Followed:
1. **Downloaded the Windows 365 Client App:**
   - I visited the official Microsoft website and downloaded the "Windows App" for my local machine.
![img]https://i.imgur.com/ODxp4od.png[/img]

2. **Logged in to the App:**
   - After installing the app, I opened it and entered my Cloud PC login credentials to establish a connection.

3. **Connected to the Cloud PC:**
   - Once authenticated, I was able to access my Cloud PC directly through the app.

The Functionality ist like when you utilize an Image in UTM oder VMWare Fusion.

---

## 2. Using the Remote Desktop Client App

To gain more control over the Cloud PC, especially for administrative tasks, I used the Remote Desktop Client App. This method is different from the traditional Remote Desktop Connection and requires a specific setup.

The traditional Remote Desktop Connection like we know from on-premise environment:
![img]https://i.imgur.com/tLiTd9L.png)

### Steps I Followed:
1. **Downloaded the Remote Desktop Client:**
   - I navigated to [windows365.microsoft.com](https://windows365.microsoft.com) and clicked the download button.
   - Since I was using a Windows machine, I selected the **Microsoft Remote Desktop for Windows** client.
![img](https://i.imgur.com/hSrQ9dV.png)

2. **Copied the Subscription URL:**
   - Before proceeding with the installation, I copied the **"Get subscription URL"** from the Windows 365 portal. This URL is necessary to connect to the Cloud PC because in the set up you will be asked for that, its like an usually API code.

3. **Installed and Configured the Remote Desktop Client:**
   - I installed the Remote Desktop Client on my local machine.
   - After installation, I launched the app and pasted the subscription URL when prompted.

4. **Authenticated and Connected:**
   - I authenticated using my Cloud PC credentials.
   - Once connected, I was able to control the Cloud PC as if I were sitting directly in front of it.
![img](https://i.imgur.com/bWUtLck.png)
---

## Summary

- **Windows 365 Client App:** I used this app to connect to my Cloud PC directly from my local machine. It provided a straightforward and user-friendly experience.
- **Remote Desktop Client App:** For more advanced control, I used the Remote Desktop Client App, which required downloading a specific client and using a subscription URL for connection.

---

### Notes:
- I ensured that I had the correct permissions and licenses to access the Cloud PC before starting the process.
- The subscription URL was essential for connecting via the Remote Desktop Client.
- Screenshots were taken at each step to document the process.

---

### Relevant Links:
- [Windows 365 Client App Download](https://windows365.microsoft.com)
- [Microsoft Remote Desktop Client Documentation](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients)