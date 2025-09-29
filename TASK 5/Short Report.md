## REPORT

## Protocols Identified
The catch had many rules, showing normal web looking. We found at least 4 rules (more than the least needed of 3). Here is a table with the first 4 rules, what they are, how many, and samples from the catch:

| Protocol | Description | Packet Count (Approx.) | Example Packets from Capture |
|----------|-------------|------------------------|------------------------------|
| **TCP** | A safe way to send data that checks if it gets there, used for most web stuff like safe links. | ~70% of all packets | Packets 1-2: TCP push and okay between 192.168.1.12 and 192.168.1.3 on doors 49789 to 8009 (local talk). Packets 24-25: TCP start and okay for link to 104.17.111.223 on door 443. |
| **UDP** | A fast way to send data without checking if it arrives, good for quick things like name checks. | ~15% of all packets | Packets 9, 26, 29: UDP sends to 192.168.1.255 on door 2008 (maybe finding devices). Packets 30-41: UDP swaps with 23.11.215.217 on door 443 (for fast media). |
| **DNS** | A system that turns website names into number addresses, like a phone book for the web. | ~10% of all packets | Packets 35-38: DNS ask for "srtb.msn.com" (A and safe types) to 103.57.86.10, with answers having other names and numbers like 204.79.197.203. Packets 51-54: Asks for "browser.events.data.msn.com". |
| **ARP** | A way to find the hardware address for a number address on the local net, like asking who has this number. | ~5% of all packets | Packets 15-23: ARP asks from router (PPCBroadband_ae:4b:0c) for numbers like 192.168.1.4, 192.168.1.3, with answer for 192.168.1.12 at hardware 00:17:7c:9b:e6:27. Again at ~72s (packets 15059-15067). |

These rules were sorted and checked in Wireshark's packet view, showing layers (like Ethernet > IP > TCP) and signs (like start, okay, end for TCP links).

## Summary of Findings and Packet Details
The catch lasted about 73 seconds and had around 15,168 packets, with sizes mostly 200 to 1500 bytes. Most traffic came from the home computer (192.168.1.12) going out to web servers, making finds, name checks, and data sends. Main points:

- **How Traffic Was Made**: Going to msn.com and geeksforgeeks.org caused DNS asks for names like srtb.msn.com, c.msn.com, and sb.scorecardresearch.com (for tracking), plus the main site (linked to CloudFront). This started TCP links to Microsoft and Google numbers. Local sends (UDP to 192.168.1.255) look like device finding, and ARP groups show router checking.

- **Packet Details Key Parts**:
  - **Amount and Ways**: Big rush of DNS (~20-30 packets in seconds 2-3) for name fixing, then TCP starts (start/okay) and safe handshakes. TCP parts often joined (like packets 44-45: 1440-byte loads). No bad stuff seen, but ad UDP to 23.11.215.217 hints at video or sound.
  - **Odd Things**: Some TCP resends (like packet 15163) and repeat okays (packet 15164) mean small net slow. End signs (like packets 4-7) show clean link stops.
  - **How Rules Work Together**: DNS on UDP fixes names before TCP sessions; ARP fixes local hardware for net sending.

This check shows how simple web looking uses many rules, with TCP for safe data and UDP/DNS for fast name finds. Learned skills like sorting, rule looking, and traffic following help fix net issues later.
