# Cyber-Security-Internship
Cyber Security Internship - Task 1: Local Network Scan
## What I Did
I scanned my local home network (192.168.1.0/24) using Nmap to find open ports and understand service exposure. First scan was basic (-sS), second with -sV for versions.

Steps:
1. Installed Nmap on Kali Linux: sudo apt install nmap
2. Found IP range: ip addr show
3. Ran scan: sudo nmap -sV 192.168.1.0/24 -oN scan_results1.txt
4. Analyzed results: Noted IPs, ports, services, versions, and risks.
5. Researched: Looked up MAC vendors online and port meanings.

## Key Findings
- Router has FTP/HTTP/HTTPS open – risks if not updated.
- A new device (maybe Chromecast) has casting ports.
- Most devices closed – good security!
- Risks: Old software, unencrypted services.

## Files in Repo
- scan_results1.txt: The Nmap output.
- commands.txt: Commands I used.
- analysis.md: My full write-up (this report).

This helped me learn recon basics!
