# Cyber Security Internship - Task 3: Basic Vulnerability Scan on PC using Nessus Essentials

This README documents the process of performing a basic vulnerability scan on my local PC using Nessus Essentials, a free vulnerability scanner from Tenable. The objective is to identify common vulnerabilities on my computer. I'll cover the steps up to running the scan; documentation of the reports, critical vulnerabilities, fixes, and screenshots will be added later.

Nessus Essentials is chosen for this task (alternative: OpenVAS Community Edition). It's free for non-commercial use, limited to scanning up to 16 IP addresses.

## Prerequisites
- A computer running Windows 10/11, macOS 11+, or a supported Linux distribution (e.g., Ubuntu).
- At least 4GB RAM and a modern CPU.
- Internet connection for registration, download, and plugin updates.

## Step 1: Register and Get Activation Code
- Go to https://www.tenable.com/products/nessus/nessus-essentials.
- Fill out the form with your details. Use a work email or a temporary email service like temp-mail.org if needed to receive the free activation code.
- Receive the activation code via email and note it down.

## Step 2: Download Installer
- Visit https://www.tenable.com/downloads/nessus.
- Select "Nessus" and choose your OS (e.g., Windows 64-bit MSI).
- Download the installer.

## Step 3: Install Nessus
- **Windows:** Double-click the MSI file, accept the license, and install.
- **macOS:** Open the DMG and drag Nessus to Applications.
- **Linux (Ubuntu):** In terminal, run `sudo dpkg -i [file.deb]` then `sudo systemctl start nessusd`.
- Nessus runs as a background service after installation.

## Step 4: Setup and Activate Nessus
- Open a browser and go to https://localhost:8834/ (or http://127.0.0.1:8834/).
- Select "Nessus Essentials," enter your activation code.
- Create a username and password.
- Wait for plugins to download and compile (10-20 minutes).

## Step 5: Update Plugins and Create Scan
- Log in to the web interface.
- Go to Settings > Plugins > Update Plugins (takes a few minutes).
- Then, go to Scans > New Scan > Select "Basic Network Scan."
- Name the scan (e.g., "Local PC Scan").
- Set target to 127.0.0.1 or localhost.
- Optional: Add credentials (e.g., Windows login) for a more thorough authenticated scan.
- Save the scan.

## Step 6: Run the Scan
- In "My Scans," find your scan and click the play button (▶).
- The scan will run for 5-15 minutes (or longer for full scans, up to 30-60 minutes).
- Monitor progress in the interface.

## Next Steps 

# 📝 Problem and Resolution Documentation

## **Problem Identified**

During a Nessus Essentials **vulnerability scanning** session on my Kali Linux laptop (192.168.1.9), the tool reported a **Medium severity issue** with a CVSS score of 6.5:

* **Issue**: *SSL Certificate Cannot Be Trusted (Plugin ID 51192)*
* **Cause**: Nessus generates a default **self-signed certificate** for its web interface (port 8834/TCP). Browsers do not trust this type of certificate, which creates a potential for man-in-the-middle attacks.
* **Impact**: While not critical in a home setup, it reduces the trustworthiness of the secure connection to the Nessus dashboard.

---

## **Resolution (Using mkcert, Zero Cost)**

To remediate the issue without purchasing a domain or certificate, I used the **mkcert** utility. This tool creates locally trusted SSL/TLS certificates for IP addresses.

### **Steps Taken**

1. **Installed mkcert and prerequisites**:

   ```bash
   sudo apt install libnss3-tools -y
   wget https://dl.filippo.io/mkcert/latest?for=linux/amd64 -O mkcert
   chmod +x mkcert
   sudo mv mkcert /usr/local/bin/
   ```

2. **Set up a local Certificate Authority (CA)**:

   ```bash
   mkcert -install
   ```

3. **Generated a certificate for the Nessus IP (192.168.1.9)**:

   ```bash
   mkcert 192.168.1.9
   ```

4. **Replaced Nessus default certs with the new ones**:

   ```bash
   sudo cp 192.168.1.9.pem /opt/nessus/com/nessus/CA/servercert.pem
   sudo cp 192.168.1.9-key.pem /opt/nessus/com/nessus/CA/serverkey.pem
   sudo systemctl restart nessusd
   ```

5. **Verification**: Accessing `https://192.168.1.9:8834` in the browser no longer showed SSL trust warnings.

---

## **Conclusion**

Through this exercise, I successfully conducted a **risk assessment** and applied a **remediation** for the Nessus certificate trust issue. I deepened my understanding of how **security tools** report issues, how **CVSS scores** help prioritize fixes, and how to apply practical solutions. Overall, I learned to link the concepts of **vulnerability scanning**, **risk assessment**, **remediation**, and effective use of **security tools** into a complete workflow.


## Repository Contents
- `README.md`: This file project overview and process.
- `report.pdf`: Scaned report of my laptop-IP
