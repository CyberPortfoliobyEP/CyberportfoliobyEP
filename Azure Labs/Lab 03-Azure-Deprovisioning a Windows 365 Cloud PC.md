# Lab 2-III - Deprovisioning a Windows 365 Cloud PC

For Demonstration that Admins should not only be able to provision a cloud PC but also know how to disable them.

In this section, I will describe how I deprovisioned a Windows 365 Cloud PC for a user who no longer needed access. Deprovisioning involves two main steps: removing the user's license and ending the grace period in Intune.

---

## Steps I Followed:

### 1. **Removing the User's License**
   - I started by navigating to the **Microsoft 365 Admin Center** at [portal.microsoft.com](https://portal.microsoft.com).
   - Under **Billing > Licenses**, I located the Windows 365 license assigned to the user.
   - I selected the user and clicked **Unassign License** to remove their access to the Cloud PC.
   - After unassigning the license, the user entered a **7-day grace period**, during which they could still access the Cloud PC.


---

### 2. **Ending the Grace Period in Intune**
   - By default, Microsoft provides a **7-day grace period** after removing a user's license. During this time, the user can still access their Cloud PC, even though the license has been removed. This is designed to give users time to back up their data or transition to a new device.
   - However, in cases where immediate access revocation is required (e.g., for security reasons or when reassigning the license to another user), it is necessary to **end the grace period early** in Intune.
   - To do this, I went to the **Microsoft Intune Admin Center** at [intune.microsoft.com](https://intune.microsoft.com).
   - Under **Devices > Windows 365 > All Cloud PCs**, I located the device associated with the user.
   - I noticed that the device was in the **Grace Period** status.
   - To end the grace period early, I clicked on **End Grace Period** and confirmed the action.

![img](https://i.imgur.com/ezf4UoO.png)

---

### 3. **Verifying the Deprovisioning**
   - After ending the grace period, I waited approximately **10 minutes** for the process to complete.
   - Once the process was finished, I refreshed the page and confirmed that the device was no longer available to the user.
   - To ensure the user could no longer access the Cloud PC, I attempted to log in as the user on [windows365.microsoft.com](https://windows365.microsoft.com). The system correctly displayed a message indicating that the user no longer had access to a Cloud PC.

---

## Summary

- **Step 1:** I removed the user's Windows 365 license, which initiated a 7-day grace period.
- **Step 2:** I ended the grace period early in Intune to immediately revoke the user's access. This step is crucial when immediate access revocation is required, as the grace period otherwise allows the user to retain access for 7 days even after license removal.
- **Step 3:** I verified that the user could no longer access the Cloud PC.

---

### Notes:
- The grace period allows users to retain access for 7 days after license removal, but this can be ended early in Intune for immediate access revocation.
- Ending the grace period can take a few minutes to complete, depending on the system.
- Screenshots were taken at each step to document the process.

---

### Relevant Links:
- [Microsoft 365 Admin Center](https://portal.microsoft.com)
- [Microsoft Intune Admin Center](https://intune.microsoft.com)
- [Windows 365 Documentation](https://learn.microsoft.com/en-us/windows-365/)