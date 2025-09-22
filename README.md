# Cyber Security Internship - Task 1: Local Network Port Scan

## What I Did
For this task, I learned basic network recon by scanning my home network (192.168.1.0/24) with Nmap. Started with a fast TCP SYN scan (-sS) to spot open ports, then followed up with version detection (-sV) to learn more about the services.

Steps:
1. Installed Nmap: sudo apt install nmap (on Kali Linux).
2. Got IP range: ip addr show.
3. Quick scan: sudo nmap -sS 192.168.1.0/24 -oN scan_results.txt (found router opens).
4. Detailed scan: sudo nmap -sV 192.168.1.0/24 -oN scan_results1.txt (got versions like old FTP).
5. Analyzed: Listed devices, researched services/MACs online, noted risks.
6. No Wireshark this time, but could add packet captures later.

## Key Findings
- 9 hosts up; router has FTP/HTTP/HTTPS (old Boa server – risky!).
- New device (1.13) for streaming with Chromecast ports.
- Phones mostly closed/filtered – secure setup.
- Risks: Unencrypted services, outdated software.

## Files
- scan_results.txt: First -sS scan (attached for basics).
- scan_results1.txt: -sV details.
- commands.txt: What I ran.
- analysis.md: My beginner write-up.

This built my recon skills – understanding exposure is key!
