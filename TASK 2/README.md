# Cyber Security Internship - Task 2 : Analyze a Phishing Email Sample

## Project Overview
This repository contains a detailed analysis of 7 phishing email samples impersonating trusted brands (FedEx, Microsoft, Intuit, Citibank, Office 365, Chase Bank, and PayPal). The goal is to identify phishing characteristics, such as spoofed senders, suspicious links, and social engineering tactics, to build awareness of email threat detection skills.

As the analyst, I performed this task as part of a cybersecurity training exercise. The analysis follows a structured mini-guide:
- Examine sender's email address for spoofing.
- Check email headers for discrepancies (using online header analyzer simulations via research).
- Identify suspicious links or attachments.
- Look for urgent or threatening language in the email body.
- Note any mismatched URLs (hover to see real link).
- Summarize phishing traits found.

**Key Concepts Covered**: Phishing, email spoofing, header analysis, social engineering, threat detection.

**Outcome**: Enhanced awareness of phishing tactics. Recommendations include never clicking links, verifying via official channels, and reporting suspicious emails.

## What I Did: Analysis Process
I conducted the analysis step-by-step as if performing hands-on research:

1. **Obtained Samples**: Screenshots were captured from online sample phishing emails (e.g., from educational resources like cybersecurity training sites) to safely analyze and raise awareness without handling real threats. These are saved as PNG files in `/resources/`.

2. **Sender Examination**: For each email, inspected the "From" address in the screenshot to detect spoofing (e.g., fake domains mimicking legit ones like @fedex.com).

3. **Header Analysis**: Since full headers aren't visible in screenshots, I simulated checks using web searches for similar phishing campaigns (e.g., querying "FedEx phishing email headers SPF fail"). Tools like MX Toolbox or Google were referenced indirectly via research to identify common discrepancies (e.g., SPF neutral, missing DKIM, foreign IPs).

4. **Link and Attachment Review**: Identified buttons/links in the body (e.g., "Manage Delivery") and inferred phishing destinations based on hover mismatches from known examples.

5. **Language Scan**: Looked for urgency/threats (e.g., "account disabled in 24 hours") to spot social engineering.

6. **URL Verification**: Noted mismatches (e.g., fake URLs like secure-citibank-verification.com).

7. **Summarization**: Compiled traits into bullet-point reports for each email.

The process took ~2 hours, focusing on safety (no links clicked). All findings are based on visual inspection and corroborated online research (no tools executed code or fetched live data).

## Resources Used
- **Screenshot Files**: 7 PNG images in `/resources/` (e.g., `fedex-missed-delivery.png`). These were captured from online sample phishing emails for educational analysis and awareness.
- **Research Sources**: 
  - Web searches for "phishing email headers [brand]" to simulate analyzer results (e.g., SPF/DKIM fails from sites like phishing.org and keepnetlabs.com).
  - Educational sites: mlhale.github.io (for header tracing examples), MX Toolbox (for SPF checks).
- **Tools Simulated**: Email client (e.g., Gmail) for viewing; online header analyzers (e.g., via browser for similar samples).
- **No Additional Files**: Analysis is self-contained in Markdown; no code or PDFs needed.

## Repository Contents
- `README.md`: This file—project overview and process.
- `analyses.md`: Detailed breakdowns of all 7 emails, with embedded image references. 
- `/resources/`: Screenshots for visual reference.
