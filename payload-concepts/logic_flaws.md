# Logic Flaws

Evasion through logic flaws involves abusing the architectural functionality of the Web Application Firewall itself, rather than obfuscating the payload string.

## HTTP Protocol Manipulation

### 1. HTTP Request Smuggling (CL.TE or TE.CL)
Exploiting disagreements over where a request ends between the WAF acting as a proxy and the internal web server.
By manipulating the `Content-Length` (CL) and `Transfer-Encoding` (TE) headers, an attacker can "smuggle" a malicious request past the WAF, appending it to the start of the next user's legitimate request on the backend pipeline.

### 2. HTTP Verb Manipulation
WAF rules often attach to specific HTTP verbs like `GET` or `POST`.
Sending a malicious payload using `PUT`, `DELETE`, or a fake method like `TEST` might bypass rules bound strictly to `GET/POST`, while a poorly designed backend API processes the request regardless of the verb.

### 3. Header Forgery
Faking internal request headers to convince the WAF the request is trusted.
- `X-Forwarded-For: 127.0.0.1`
- `X-Originating-IP: 127.0.0.1`

## Content-Type Exploits

WAFs parse payloads based on the declared `Content-Type`. If a WAF isn't configured to parse a specific type (or fails gracefully), it may pass raw data to the backend.

- Changing `application/x-www-form-urlencoded` to `multipart/form-data` with slight malformations in boundary values.
- Submitting JSON payloads as application/xml or plain text. If the backend accepts the payload indiscriminately but the WAF fails to parse the structure, rules won't trigger.
