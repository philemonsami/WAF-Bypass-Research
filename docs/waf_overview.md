# WAF Overview

A Web Application Firewall (WAF) is a security control designed to monitor, filter, and block malicious HTTP traffic traveling to and from a web application.

## Core Functions 
1. **Traffic Filtering**: Inspects HTTP/S requests against a set of predefined security rules.
2. **Reverse Proxy Architecture**: Acts as an intermediary, sitting between the internet and the web servers. 
3. **Attack Prevention**: Specifically designed to stop common layer 7 attacks, such as Cross-Site Scripting (XSS), SQL Injection (SQLi), Path Traversal, and Command Injection.

## WAF Operating Models
*   **Negative Security Model (Blacklisting)**: Denies requests that match known signatures of attacks. This is the most common default.
*   **Positive Security Model (Whitelisting)**: Denies all requests unless they explicitly match allowed patterns (e.g., specific parameters, length, and character sets). 
*   **Hybrid Model**: Combines both approaches, and often integrates machine learning or behavioral analysis to detect anomalies.

## Common Rule Set (CRS)
Many WAFs (such as ModSecurity) heavily rely on community-driven rule sets, most notably the **OWASP ModSecurity Core Rule Set (CRS)**. The CRS provides generic attack detection rules designed to offer base-level protection against the OWASP Top 10 vulnerabilities.
