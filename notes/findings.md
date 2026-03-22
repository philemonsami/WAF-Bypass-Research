# Findings

This document tracks empirical findings from testing various WAF instances or default rule sets.

## General Observations

*   **Default Deny is Rare**: In commercial WAFs, "Block-by-Default" policies are exceptionally rare due to massive false-positive rates disrupting legitimate traffic. Consequently, WAFs mostly rely on extensive blacklisting, making them inherently open to evasion via obscure syntax.
*   **JSON Parsing Weaknesses**: Many traditional regex rules perform poorly when parsing deeply nested JSON payloads or GraphQL queries due to complex data serialization formats.
*   **Length Restrictions**: WAFs often limit the amount of data they inspect. If a payload exceeds the WAF's `SecRequestBodyLimit`, it may fail open or ignore trailing parameters, allowing the backend to process malicious input appending an excessive amount of junk data.

## Log of Confirmed Bypasses
*(To be populated with concrete examples during specific tests, detailing target WAF, vulnerability class, blocked generic payload, and the bypassed variant)*

**Example Entry Format:**
*   **Target WAF**: XYZ Cloud WAF 
*   **Vulnerability**: SQL Injection
*   **Base Payload**: `' UNION SELECT 1,2,3--` (Blocked: Rule ID 98129)
*   **Bypass Payload**: `'/*!50000UniON*/ /*!50000SeLeCt*/ 1,2,3--`
*   **Notes**: WAF failed to parse MySQL-specific inline comments.
