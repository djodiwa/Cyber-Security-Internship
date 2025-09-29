# Cyber Security Internship - Task 5: Capture and Analyze Network Traffic Using Wireshark

## Objective
The goal of this task is to grab live network packets from a working network link and spot simple rules and kinds of traffic in them. This practice helps learn basic packet checking and know about common network rules.

## Tools Used
- **Wireshark (free)**: A free tool that catches, sorts, and looks at network traffic.

## Methodology and Steps Followed
To finish this task, I did the steps from the guide one by one:

1. **Install Wireshark**: I put Wireshark on a Windows computer from the main site (wireshark.org). It came with the Npcap driver needed to catch live packets.

2. **Start Capturing on Active Network Interface**: I opened Wireshark and picked the working Ethernet link (like "Ethernet" tied to the home router at 192.168.1.1). Catching started right away, taking all packets with no first filters.

3. **Browse a Website or Ping a Server to Generate Traffic**: To make different traffic, I used a web browser (Google Chrome) and went to sites like msn.com and geeksforgeeks.org. This started web asks, name checks, and loads of other stuff (like ads and fast servers). No direct pings, but looking at sites made similar find traffic.

4. **Stop Capture After a Minute**: The catch went for about 73 seconds (from time stamps in the saved data), then I stopped it to keep just the useful part.

5. **Filter Captured Packets by Protocol**: In Wireshark, I used filters like:
   - `tcp` for TCP traffic.
   - `udp` for UDP traffic.
   - `dns` for DNS asks and answers.
   - `arp` for ARP asks and replies.
   These helped pick out and check certain rule flows.

6. **Identify at Least 3 Different Protocols in the Capture**: Checking showed more than 3 rules (listed below). I spotted them by looking at packet info like start/end IPs, doors, and load details.

7. **Export the Capture as a .pcap File**: The full catch was saved as "network_traffic_capture.pcap" using Wireshark's File > Export Objects > Save As. For the report.

8. **Summarize Findings and Packet Details**: See the part below for a short wrap-up based on the catch check.

## Repository Contents
- **Network_traffic_capture**: Packet Capture File (saved from Wireshark).
- **Short Report**: This paper is the report, with packet details and finds.
