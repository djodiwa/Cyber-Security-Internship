# Step 1: Find my network range
ip addr show

# Step 2: First quick scan to find open ports
sudo nmap -sS 192.168.1.0/24 -oN scan_results.txt

# Step 3: Deeper scan for service details
sudo nmap -sV 192.168.1.0/24 -oN scan_results1.txt
