# Research References

A collection of external resources, blog posts, academic papers, and tools that act as foundational theory or inspiration for modern WAF evasion testing.

## Documentation & Guides

- [OWASP WAF Evaluation Framework](https://owasp.org/www-project-waf-evaluation-framework/)
- [PortSwigger Web Security Academy: Web Application Firewalls](https://portswigger.net/web-security/waf-bypassing)
- [ModSecurity Reference Manual](https://github.com/owasp-modsecurity/ModSecurity)
- [OWASP Core Rule Set Documentation](https://coreruleset.org/)

## Notable Blog Posts and Papers

- *A Look at WAF Bypasses* by various bug bounty hunters (General theory on regex weaknesses).
- *Bypassing ModSecurity CRS* demonstrations (Focusing on PL1 vs PL4 rule variations).
- *Web Application Firewall Bypass Techniques* (Coverage of HPP and HTTP Request Smuggling).

## Tools

- [WAFW00F](https://github.com/EnableSecurity/wafw00f) - Web Application Firewall Fingerprinting Tool.
- [CloudFail](https://github.com/m0rtem/CloudFail) - Tool to uncover backend IPs hiding behind Cloudflare setups.
- [Burp Suite Professional](https://portswigger.net/burp) - Essential for active payload modification and fuzzing.
- [SQLMap](https://github.com/sqlmapproject/sqlmap) - Contains built-in "tamper scripts" meant to obfuscate SQL payloads to evade WAFs.
