# Methodology

This document outlines the testing methodology used to analyze Web Application Firewalls (WAFs) and systematically discover bypasses.

## Setup Requirements

1. **Target Web Application**: A deliberately vulnerable web application (like DVWA or OWASP Juice Shop) deployed behind the WAF.
2. **WAF Deployment**: The WAF should be deployed in enforcing mode (dropping payloads) to confirm that bypass techniques are functional, not just logging events.
3. **Fuzzing Infrastructure**: Scripts and tools (Python, Burp Suite Intruder, custom wrappers) to systematically inject payloads into the target app.

## Testing Phases

### 1. Baslining & Policy Discovery

Send known, harmless traffic to understand standard WAF responses (HTTP 200 vs. HTTP 403 pages). Establish how the WAF terminates connections (RST vs. Block Page). Attempt to trigger intentional alerts using basic payloads (e.g., `<script>alert(1)</script>`) to verify the WAF is active.

### 2. Identifying Normalization Behaviors

Test how the WAF handles edge cases in encoding and parsing before moving on to full evasion. Send different character encodings and observe backend vs. WAF processing paths.

### 3. Systematic Fuzzing

Execute targeted fuzzing for specific vulnerability classes (SQLi, XSS, Path Traversal) with variations in syntax, whitespace, and encoding, focusing on rules that might have loose constraints. Measure and analyze which exact components of a payload trigger explicit blocks.

### 4. Payload Refinement

When specific characters trigger blocks, begin substituting those characters. For example, if `<script>` is blocked, attempt `<svg/onload=...>` or `<img/src=x/onerror=...>`. Apply the principles defined in `docs/evasion_theory.md`.
