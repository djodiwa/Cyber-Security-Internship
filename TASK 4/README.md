# Cyber Security Internship - Task4 : Setup and Use a Firewall on Linux

## Introduction
Firewalls are essential security tools in computing that act as a barrier between a trusted internal network and untrusted external networks, such as the internet. They monitor and control incoming and outgoing network traffic based on predetermined security rules. This task demonstrates basic firewall management using UFW (Uncomplicated Firewall) on Linux, a user-friendly interface for managing iptables. By configuring rules to block or allow specific ports, we can enhance system security, prevent unauthorized access, and test these configurations in a controlled manner. The process involves setting up UFW, adding and testing rules for ports like Telnet (23) and SSH (22), and restoring the original state, all while documenting steps for reproducibility.

## Objective
Configure and test basic firewall rules using UFW on Linux to allow or block traffic.

## Steps and Commands

1. Install and Enable UFW:
   - `sudo apt update && sudo apt install ufw -y`
   - `sudo ufw enable`
   - Screenshot: step1-enable-ufw.png
!{}(resource/step1-enable-ufw.png)
2. List Current Rules:
   - `sudo ufw status verbose`
   - Screenshot: step2-list-rules.png

3. Add Block Rule for Port 23 (Telnet):
   - `sudo ufw deny 23`
   - `sudo ufw reload`
   - Screenshot: step3-block-rule-added.png

4. Test the Rule:
   - Local: `telnet localhost 23` (should fail)
   - Screenshot: step4-test-failure.png

5. Add Allow Rule for SSH (Port 22):
   - `sudo ufw allow 22`
   - `sudo ufw reload`
   - Screenshot: step5-allow-ssh.png

6. Remove Test Block Rule:
   - `sudo ufw delete deny 23`
   - `sudo ufw reload`
   - Screenshot: step6-rule-removed.png

## Summary of How Firewall Filters Traffic
Firewalls like UFW filter network traffic by inspecting packets based on rules. They check source/destination IP, port, protocol, etc. Default policies (e.g., deny inbound) block unless explicitly allowed. Rules are processed in order: allow/deny specific traffic, logging suspicious activity. This prevents unauthorized access while permitting legitimate connections (e.g., allowing SSH but blocking Telnet).
