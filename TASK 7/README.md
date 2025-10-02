# Cyber Security Internship - Task 7: Identify and Remove Suspicious Browser Extensions

## Objective
The goal was to review browser extensions for potential risks, spot anything suspicious, and clean up to improve security and performance. This helps build awareness of how extensions can affect privacy and safety.

## Installed Extensions Review
I checked all extensions in Firefox. Here's a quick list of what was active:
!{image}(assets/list of extension.png)
- **Bitwarden Password Manager**: Securely stores passwords and passkeys. Looks legit and necessary for daily use.
- **Don't track me Google**: Blocks annoying link-tracking on Google Search and Maps. Standard ad/privacy tool, no red flags.
- **PopUpOFF - Popup and overlay blocker**: Stops popups, overlays, and cookie notices. Useful blocker with no extra permissions needed.
- **SponsorBlock for YouTube - Skip Sponsorships**: Skips ads and intros on YouTube videos. Popular and focused, nothing suspicious.
- **Turn Off the Lights**: Dims the page background for better video watching, mainly for YouTube.

All extensions had good reviews and seemed from trusted sources like addons.mozilla.org.

## Suspicious Findings and Actions Taken
Only one extension stood out as potentially risky: **Turn Off the Lights**.

- **Why suspicious?** It had an optional permission enabled: "Access your data for sites in the youtube.com domain." This means it could read or change data on YouTube pages beyond what's needed for basic dimming. Even though it's a popular tool (over 1 million users), extra access like this can sometimes lead to unintended data collection or conflicts.
  
- **What I did**: I turned off that optional permission to limit its access. I also considered removing the whole extension but kept it enabled with the permission disabled for now, since it's useful for videos. No other extensions had unnecessary permissions or unused features.

No full removals were needed, but this tweak reduces risk. After changes, I restarted Firefox – pages loaded a bit smoother, and no weird slowdowns.

**List of Suspicious Extensions Found and Actions**:
| Extension Name       | Issue Found                          | Action Taken              | Removed? |
|----------------------|--------------------------------------|---------------------------|----------|
| Turn Off the Lights | Optional YouTube data access enabled | Disabled optional permission | No (kept but restricted) |

## Research on Malicious Extensions
Malicious browser extensions are like sneaky apps that pretend to help but actually cause harm. They often get installed accidentally through fake downloads or bundled software. Here's a simple breakdown of how they can hurt users:

- **Steal Personal Info**: They can read your passwords, emails, or banking details by accessing site data without you knowing. For example, a fake ad-blocker might log your logins.
  
- **Track Everything You Do**: Extensions with broad permissions (like "access all sites") follow your browsing history, location, or searches to sell your data or show targeted scams.
  
- **Inject Malware or Ads**: They add unwanted popups, redirect links to phishing sites, or even download viruses in the background.
  
- **Slow Down Your Browser**: By running hidden scripts, they eat up memory and CPU, making everything laggy.
  
- **Real-World Example**: In 2023, over 200 Chrome extensions were caught spying on users via hidden trackers, affecting millions before removal.

To stay safe, always check permissions (stick to "required" only), read recent reviews, and remove anything you haven't used in months. Tools like Firefox's built-in reviewer help flag issues early.

## Outcome and Key Learnings
This review boosted my awareness of browser risks – extensions are handy but can be weak spots if not managed. By disabling that extra permission, I cut potential privacy leaks without losing functionality. Overall, my setup feels more secure and snappier. Next time, I'll audit extensions every few months.
