# Detection Methods

WAFs employ various techniques to identify anomalous or malicious traffic. Understanding these methodologies is critical for testing their resilience.

## 1. Signature-Based Detection
*   **Mechanism**: The WAF compares the incoming payload against a database of known attack patterns (Regex matching).
*   **Pros**: Fast, efficient, and highly accurate for known vulnerabilities.
*   **Cons**: Prone to evasion through obfuscation. Fails to detect zero-day exploits.

## 2. Anomaly-Based Detection (Behavioral)
*   **Mechanism**: Establishes a baseline of "normal" traffic and flags requests that deviate significantly.
*   **Metrics**: High request rates, unusual header combinations, navigation flows, and geo-location inconsistencies.
*   **Pros**: Capable of stopping zero-days and automated botnets.
*   **Cons**: Higher false-positive rates; requires an initial learning period.

## 3. Protocol Validation
*   **Mechanism**: Ensures that the incoming HTTP requests strictly adhere to RFC specifications.
*   **Metrics**: Checks for missing mandatory headers, malformed URIs, incorrect methods, or invalid character encoding.
*   **Impact**: Blocks HTTP Request Smuggling and basic fuzzing attempts.

## 4. Reputation & Threat Intelligence
*   **Mechanism**: Integrates with IP threat feeds. 
*   **Metrics**: Drops requests originating from known malicious IPs, Tor exit nodes, open proxies, or botnets before inspecting the layer 7 payload.

## 5. Machine Learning (ML) & AI Detection
*   **Mechanism**: Utilizes NLP techniques (Lexical Analysis) or advanced predictive modeling to determine the malicious intent of a string, rather than relying solely on hardcoded regex.
