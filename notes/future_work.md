# Future Work

This file outlines ongoing areas of exploration and items to be implemented or tested in upcoming research cycles.

## 1. Test Automation

-   [ ] Develop python scripts to automatically cycle through tampering variations against a known testing endpoint.
-   [ ] Integrate `yaml`-based test definitions for standardized execution against the Docker environment.

## 2. Specific Evasion Scenarios

-   [ ] **Cloudflare Workers Evasion**: Test if serverless edge worker processing behaves differently compared to traditional proxy setups.
-   [ ] **GraphQL and gRPC**: Investigate how deeply commercial WAFs parse and inspect modern API serialization mechanisms schemas beyond standard REST/JSON endpoints.
-   [ ] **HTTP/2 & HTTP/3 Downgrade attacks**: Analyze if WAFs mistakenly normalize or drop HTTP/2 frames in a manner that creates backend desync vulnerabilities when converted back to HTTP/1.1.

## 3. Threat Intelligence Analysis

-   [ ] Gather empirical data on the average time it takes for major WAF vendors to implement signatures for high-profile CVEs (e.g., Log4Shell, Spring4Shell) and analyze the initial bypasses discovered before rules were tightened.
