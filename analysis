Analysis of My Nmap Scan Results
I'm new to cybersecurity; this is an internship task on network scanning. I ran a TCP SYN scan (-sS) to quickly identify open ports on my home network, revealing main ports on the router and responsive devices. Then, a version scan (-sV) on the same range provided software names and versions for risk assessment. First scan report (scan_results.txt) is in my GitHub repo for comparison.
Summary

Network Scanned: 192.168.1.0/24 (home Wi-Fi, found via ip addr show).
Hosts Found: 9 online in -sV scan (more than in -sS, likely due to other devices came online later ).
Scan Duration: -sS: 83 seconds; -sV: 303 seconds (deeper probing).

Detailed Device Analysis
Compared both scans for completeness: -sS for basics (open/closed ports), -sV for details. Identified devices via names and MAC vendors (searched online); some MACs "Unknown" for privacy.

RTKGW.bbrouter (192.168.1.1): Main router.

Open Ports:

21/tcp: FTP (GNU Inetutils FTPd 1.4.1).
80/tcp: HTTP (Boa HTTPd 0.93.15).
443/tcp: HTTPS (Boa HTTPd 0.93.15).


MAC: 64:FB:92:AE:4B:0C (PPC Broadband, ISP router).


192.168.1.2: Samsung smart device (fridge).

Open Ports: None; all 1000 ports closed (device responsive but secured).
MAC: 3A:68:48:3C:29:03 (SAMJIN Co., Ltd., Samsung smart home components).


Archer_C5.bbrouter (192.168.1.5): TP-Link router or Wi-Fi booster.

Open Ports: None; all filtered (firewall hiding responses).
MAC: 34:60:F9:85:14:86 (TP-Link Limited).


Galaxy-F15-5G.bbrouter (192.168.1.7): Samsung Galaxy F15 phone.

Open Ports: None; all closed.
MAC: CE:4A:35:DB:64:92 (Unknown, but name indicates Samsung).


192.168.1.13: Smart TV (more details in -sV).

Open Ports:

8008/tcp: HTTP (no version).
8009/tcp: SSL/Castv2 (Ninja Sphere Chromecast driver).
8443/tcp: SSL/HTTPS-alt.
9000/tcp: SSL/CSListener.


MAC: 7C:25:DA:F0:A9:1C (FN-Link Technology Limited, IoT Wi-Fi).


POCO-X3-Pro.bbrouter (192.168.1.38): POCO phone (Xiaomi brand).

Open Ports: None open; 7/tcp filtered (echo service).
MAC: 22:59:39:1A:E2:F9 (Unknown, likely Xiaomi).


Redmi-Note-10.bbrouter (192.168.1.65): Redmi Note 10 phone (Xiaomi).

Open Ports: None open; 7/tcp filtered (echo).
MAC: CA:59:CD:96:26:93 (Unknown, fits Xiaomi patterns).


192.168.1.66: Possibly another phone or gadget.

Open Ports: None; all closed.
MAC: 06:34:04:FA:0F:C1 (Unknown).


kali.bbrouter (192.168.1.9): Kali Linux laptop (scanning device).

Open Ports: None; all closed (for security).
MAC: Not shown (self-scan).



Learned About Services
-sS identified open ports (e.g., router's 21, 80, 443); -sV revealed software details. Researched basics:

21/tcp (FTP, GNU Inetutils 1.4.1): File transfer; unencrypted (exposes passwords).
80/tcp (HTTP, Boa HTTPd 0.93.15): Router web interface; simple, outdated server.
443/tcp (HTTPS, Boa HTTPd 0.93.15): Secure web interface.
8008/tcp (HTTP): Alternative web port for device apps.
8009/tcp (SSL/Castv2, Ninja Sphere Chromecast): Streaming support; outdated smart home tech.
8443/tcp (SSL/HTTPS-alt): Non-standard secure web.
9000/tcp (SSL/CSListener): Connection listener, possibly remote access.
7/tcp (Echo, filtered): Bounces data; obsolete, potential for amplification attacks.

Possible Security Problems
Most network closed (good firewalls), but router and 192.168.1.13 expose services. Risks by severity:
High Risks:

Router FTP (21, GNU Inetutils 1.4.1): Outdated (2000s), unencrypted; vulnerable to file/login theft.
SSL ports on 192.168.1.13 (8009, 8443, 9000): Outdated software risks hijacking streaming or eavesdropping.

Medium Risks:

Router HTTP (80, Boa 0.93.15): Unencrypted login; risky for credential exposure.
Other ports on 1.13 (8008, 8443): Non-standard, potentially overlooked updates.
Filtered echo (7) on phones: Blocked, but open could enable network slowdown attacks.

Low Risks:

Closed/filtered ports elsewhere: Firewalls effective, minimal entry points

What I Think Next: The -sS was great for a quick map, and -sV added the story behind it. My network's mostly safe, but I gotta update that router firmware soon. Maybe I'll try a UDP scan or Wireshark next to see the packets flying. This task is teaching me how recon works – spot the opens, then poke for weaknesses!
