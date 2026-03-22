# Normalization Issues

Normalization is the process by which a WAF translates obscure or encoded payloads into a standard format before applying its rules. Flaws or limitations in normalization are one of the primary causes of WAF bypasses.

## The Normalization Problem

When an HTTP request is received, the WAF must decode it (e.g., URL unescape, Hex decode). However, the backend application server (e.g., IIS, Apache) and the specific application framework (e.g., PHP, Java, Node.js) may perform varying degrees of *additional* decoding.

If the WAF's normalization routine doesn't exactly match the backend's normalization, an impedance mismatch occurs.

## Common Normalization Weaknesses

1.  **Multiple Encodings**: 
    If a payload is double URL-encoded (`%2527` for `'`), the WAF might decode it only once, inspecting `%27` (which is harmless). The backend application might decode it a second time, executing the `'` character.

2.  **Unicode Equivalence**: 
    The backend might accept full-width unicode characters (e.g., `＜script＞`) and normalize them into standard ASCII (`<script>`). If the WAF doesn't map those characters correctly, it misses the payload.

3.  **Path Normalization**: 
    Directory traversal payloads (`/../../etc/passwd`) can be obfuscated using backslashes (`\..\..\etc\passwd`), self-referential directories (`/././`), or excessive slashes (`////etc/passwd`). WAFs often fail to collapse these correctly.

4.  **Null Byte Injection**:
    Injecting a null byte (`%00`) can cause older WAFs (especially C-based rule engines) to prematurely terminate string parsing, viewing the payload as harmless, while the PHP/Java backend processes the entire string.

5.  **Invalid Encodings**:
    Providing malformed URL encodings (e.g., `%u0027` or `%qs`) might cause the WAF to skip decoding, while a lenient backend (like IIS) automatically fixes and parses the character.
