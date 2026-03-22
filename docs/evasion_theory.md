# Evasion Theory

WAF evasion is the practice of modifying a malicious payload such that it successfully achieves its goal on the backend server while remaining undetected by the WAF inspecting the traffic.

## Fundamental Principles 

1. **Semantic Equivalence**: The modified payload must mean the exact same thing to the backend parser as the original payload, despite looking different to the WAF.
2. **Parser Impendence Mismatch**: Exploiting the differences in how the WAF parses the request versus how the backend application parses the request. 
3. **State Exhaustion**: Overwhelming the WAF's memory or CPU thresholds to force an "allow-by-default" fail-open scenario.

## Core Evasion Strategies

*   **Encoding & Obfuscation**: Using URL encoding, HTML entity encoding, Unicode variants, Base64, or Hex encoding. If the backend decodes an extra layer that the WAF ignores, the payload bypasses detection.
*   **String Manipulation**: Concatenation (`'s'.'e'.'l'.'e'.'c'.'t'`), case toggling (`SeLEcT`), and using uninitialized variables (`sel${empty}ect`).
*   **White Space Manipulation**: Replacing spaces with alternative characters (e.g., `/**/`, `%09`, `%0a`, `%0c`, `+`) to bypass regex boundaries that rely on standard space characters.
*   **HTTP Parameter Pollution (HPP)**: Sending multiple parameters with the same name (e.g., `?id=1&id=inject`). The WAF might only inspect the first parameter, while the backend application might use the second.
*   **HTTP Request Smuggling**: Desyncing the WAF and backend server through malformed `Content-Length` and `Transfer-Encoding` headers.
