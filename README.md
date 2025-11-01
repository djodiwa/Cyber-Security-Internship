# Cyber Security Internship Portfolio

| Name     | Internship Company |
|----------|--------------------|
| DIWAKAR  | Elevate Labs       |

## Introduction

This repository serves as a comprehensive portfolio of the projects and tasks completed during a 45-day Cyber Security Internship with Elevate Labs. The work documented here demonstrates practical, hands-on experience across a wide range of cybersecurity domains, including ethical hacking, network security, vulnerability assessment, and threat analysis. Each task and project was designed to build foundational skills and apply theoretical knowledge to real-world scenarios.

## Tasks and Project Overview

Below is a summary of the key tasks and the final project undertaken during the internship period.

| #   | Title                                      | Domain                  | Key Skills Demonstrated                                      |
|-----|--------------------------------------------|-------------------------|--------------------------------------------------------------|
| 1   | Local Network Port Scanning with Nmap      | Network Reconnaissance  | Network Scanning, Service & Version Detection, Nmap          |
| 2   | Phishing Email Analysis                    | Threat Analysis         | Phishing Detection, Header Analysis, Social Engineering Tactics |
| 3   | Vulnerability Scanning with Nessus Essentials | Vulnerability Management | Vulnerability Scanning, Risk Assessment, Remediation (SSL)   |
| 4   | Linux Firewall Configuration with UFW      | Network Security        | Firewall Management, Rule-Based Filtering, Linux Security (UFW) |
| 5   | Network Traffic Analysis with Wireshark    | Packet Analysis         | Packet Capturing, Protocol Analysis (TCP, UDP, DNS), Filtering |
| 6   | Strong Password Creation and Evaluation    | Security Best Practices | Password Security Principles, Brute-Force/Dictionary Attack Mitigation |
| 7   | Suspicious Browser Extension Audit         | Endpoint Security       | Browser Security, Risk Assessment, Permission Analysis       |
| 8   | VPN for Privacy and Security               | Privacy & Anonymity     | VPN Technology, IP Masking, Traffic Encryption (ProtonVPN)   |
| P   | Keylogger with Encrypted Data Exfiltration | Ethical Hacking & Development | Python, Data Encryption, Network Communication, Persistence Mechanisms |

## Detailed Task Descriptions

### Task 1: Local Network Port Scan

This task focused on network reconnaissance fundamentals by performing scans on a local network using Nmap. The process involved identifying active hosts, discovering open ports, and fingerprinting the services running on them to identify potential security weaknesses.

### Task 2: Analyze a Phishing Email Sample

An analysis of seven phishing email samples was conducted to identify common social engineering tactics and technical indicators of a malicious email. The investigation involved examining sender addresses, analyzing (simulated) email headers, identifying suspicious links, and recognizing urgent or threatening language designed to manipulate users.

### Task 3: Basic Vulnerability Scan with Nessus Essentials

A vulnerability assessment was performed on a local machine using Nessus Essentials. This included setting up the scanner, running a "Basic Network Scan," analyzing the report, and remediating a discovered medium-severity vulnerability related to an untrusted SSL certificate on the Nessus web interface itself.

### Task 4: Setup and Use a Firewall on Linux

This task involved configuring and testing a host-based firewall on a Linux system using Uncomplicated Firewall (UFW). Rules were implemented to block and allow traffic on specific ports (e.g., blocking Telnet port 23, allowing SSH port 22), providing practical experience in enforcing network security policies.

### Task 5: Capture and Analyze Network Traffic Using Wireshark

Live network traffic was captured and analyzed using Wireshark to identify and understand common network protocols. The captured data was filtered to isolate and inspect various protocol flows, including TCP, UDP, DNS, and ARP, demonstrating the fundamentals of packet analysis.

### Task 6: Creating and Evaluating Strong Passwords

This exercise explored the principles of robust password security. Various passwords were created and evaluated using a strength checker to analyze the impact of length, character diversity (uppercase, lowercase, numbers, symbols), and predictability on overall security against common attack vectors like brute-force and dictionary attacks.

### Task 7: Identify and Remove Suspicious Browser Extensions

An audit of installed browser extensions was performed to identify potential privacy and security risks. The review focused on evaluating extension permissions, leading to the restriction of an extension with excessive data access permissions and a broader understanding of how malicious extensions can compromise a system.

### Task 8: Working with VPNs

This task provided hands-on experience with Virtual Private Networks (VPNs) using ProtonVPN. The process included setting up a VPN client, verifying the change in public IP address, confirming traffic encryption, and comparing network performance. The benefits and limitations of using a VPN for privacy and security were also summarized.

## Final Project Description

**Project: Keylogger with Encrypted Data Exfiltration**

This capstone project involved developing a sophisticated keylogging tool for educational purposes within an ethical hacking lab environment. The solution consists of a stealthy client (`enhanced_keylogger.py`) and a Flask-based command-and-control server (`enhanced_server.py`).

**Keylogger Features:**  
Implemented stealth operations, Windows startup persistence, and an emergency stop key. All captured keystrokes were encrypted using AES128-CBC (Fernet) before exfiltration.

**Server Features:**  
A web-based control panel was developed to receive, decrypt, and display logged data in real-time. It included remote control capabilities, such as a kill switch and persistence management.

**Skills Acquired:**  
Advanced Python scripting, symmetric encryption, client-server communication, web application development with Flask, and Windows system interactions.

## Core Competencies and Skills

Throughout this internship, a diverse set of cybersecurity skills were developed and honed:

### Offensive Security
- Network Reconnaissance
- Vulnerability Scanning
- Ethical Hacking Concepts

### Defensive Security
- Firewall Management
- Endpoint Security
- Network Traffic Analysis

### Threat Intelligence
- Phishing Analysis
- Social Engineering Awareness

### Security Principles
- Data Encryption
- Password Security
- Privacy-Enhancing Technologies

### Technical Proficiencies

| Category          | Tools/Technologies                  |
|-------------------|-------------------------------------|
| Tools             | Nmap, Nessus, Wireshark, UFW, ProtonVPN |
| Languages & Frameworks | Python, Flask                       |

## Disclaimer

All projects and tasks documented in this repository were conducted for educational purposes only in a controlled lab environment. The tools and techniques described should not be used for any unauthorized or malicious activities. The author is not responsible for any misuse of the information contained herein.
