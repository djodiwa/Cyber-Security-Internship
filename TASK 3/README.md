# Step-by-Step Guide to Download and Use Nessus for a Basic Vulnerability Scan on Your PC

Nessus is a popular vulnerability scanner developed by Tenable. This guide covers how to download, install, and use Nessus Essentials (the free version) to perform a basic scan on your local PC. Note that Nessus Essentials is limited to non-commercial use and scanning up to 16 IP addresses.

### Step 1: Register for Nessus Essentials and Obtain an Activation Code
- Visit the official Tenable Nessus Essentials registration page at https://www.tenable.com/products/nessus/nessus-essentials.
- Fill out the registration form with your details (name, email, etc.). This is free for personal use and allows scanning up to 16 IP addresses.
- After submitting, you'll receive an activation code via email. Note this code down, as you'll need it during setup.

### Step 2: Download the Nessus Installer
- Go to the Tenable downloads page at https://www.tenable.com/downloads/nessus.
- Select "Nessus" from the product dropdown.
- Choose the appropriate version for your operating system (e.g., Windows, macOS, or Linux). For a personal PC, Windows is common—download the 64-bit MSI installer if applicable.
- Save the installer file to your computer. Ensure your system meets the minimum requirements: at least 4 GB RAM, modern CPU, and supported OS (Windows 10/11, macOS 11+, or Linux distributions like Ubuntu).

### Step 3: Install Nessus
- **For Windows:**
  - Double-click the downloaded MSI file (e.g., Nessus-x.x.x-x64.msi).
  - Follow the installation wizard: Accept the license agreement, choose the installation directory (default is fine), and click "Install."
  - If prompted by User Account Control (UAC), allow the installation.
  - The process takes a few minutes; Nessus will install as a service.
- **For macOS:**
  - Double-click the DMG file, then drag the Nessus app to your Applications folder.
  - Run the installer if prompted.
- **For Linux (e.g., Ubuntu):**
  - Open a terminal and navigate to the download directory.
  - Install using dpkg: `sudo dpkg -i Nessus-x.x.x-ubuntuxxxx_amd64.deb` (replace with your file name).
  - Start the service: `sudo systemctl start nessusd`.
- After installation, Nessus runs as a background service. It may take a moment to start.

### Step 4: Set Up and Activate Nessus
- Open a web browser and navigate to https://localhost:8834/ (or http://127.0.0.1:8834/ if HTTPS fails). This accesses the Nessus web interface.
- On the welcome page, select "Nessus Essentials" as the product.
- Enter the activation code from your email.
- Create a user account by providing a username and password (this will be your admin login).
- Nessus will download and compile plugins (vulnerability checks). This can take 10-20 minutes depending on your internet speed. Wait for it to complete.

### Step 5: Create a Basic Vulnerability Scan
- Log in to the Nessus web interface using your username and password.
- In the top navigation, click "Scans" > "New Scan."
- Select the "Basic Network Scan" template (this is suitable for a simple vulnerability scan).
- Configure the scan:
  - Give it a name, e.g., "Local PC Vulnerability Scan."
  - In the "Targets" field, enter "127.0.0.1" or "localhost" to scan your own computer.
  - Optionally, adjust other settings like enabling credentials for deeper scans (under "Credentials" tab—add Windows or SSH credentials if you want authenticated scanning for more accurate results).
  - Leave other defaults for a basic scan.
- Click "Save" to create the scan.

### Step 6: Run the Scan
- On the "My Scans" page, find your new scan.
- Click the play button (▶) next to it to launch the scan.
- The scan will run, typically taking 5-15 minutes for a local PC depending on your system's complexity. Monitor progress in the interface.

### Step 7: View and Analyze Scan Results
- Once complete, click on the scan name to view results.
- The dashboard shows vulnerabilities by severity (Critical, High, Medium, Low, Info).
- Click on tabs like "Hosts," "Vulnerabilities," or "Remediations" for details.
- For each vulnerability, you'll see descriptions, risk levels, and remediation steps.
- Export the report if needed (PDF or CSV) via the "Export" button.
- Address any found issues by updating software, applying patches, or configuring settings as recommended.

**Notes:**
- Nessus Essentials is for non-commercial use only. For professional features, consider upgrading.
- Scanning your own PC is safe, but ensure no critical services are disrupted. For best results, run as administrator and use credentials.
- If you encounter issues, check the Tenable Community forums or documentation for troubleshooting.

**Sources:** This guide is based on official Tenable documentation and user guides from reliable sources like Tenable's website, cybersecurity blogs, and tutorials (e.g., from HackTheBox, YouTube tutorials, and official docs).
