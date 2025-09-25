# Task 3: Basic Vulnerability Scan on PC using Nessus Essentials

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

## Next Steps (To Be Added Later)
- Review the report for vulnerabilities and severity.
- Research fixes/mitigations for found issues.
- Document the most critical vulnerabilities.
- Include screenshots of scan results.
