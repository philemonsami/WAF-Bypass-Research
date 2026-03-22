# WAF Bypass Research

This repository is dedicated to researching Web Application Firewall (WAF) bypass techniques, evasion theories, and testing methodologies. It contains documentation on how WAFs detect malicious payloads, how these systems normalize input, and theoretical approaches to evading such mechanisms.

## Project Structure

- **`docs/`**: Theoretical documentation on WAF functionality, detection strategies, evasion principles, and normalization behaviors.
- **`notes/`**: Research findings, methodology, references, and directions for future work.
- **`payload-concepts/`**: Specific payload construction methods, logic flaws, obfuscation patterns, and unicode evasion tricks.
- **`test-environment/`**: Setup instructions and configurations (e.g., Docker) to safely evaluate payload effectiveness.
- **`experiments/`**: Raw scripts and tools for automated testing, traffic analysis, input encoding, and manipulating HTTP requests.

## Disclaimer
The information and tools provided in this repository are for educational and research purposes only. They must only be used against systems with explicit authorization to test their WAF implementations. The authors are not responsible for any misuse of the techniques described herein.
