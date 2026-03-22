# Unicode Variations

Unicode Homoglyphs and visual equivalencies present a massive challenge for legacy defensive regex systems. If the WAF doesn't normalize specific Unicode variants to simple ASCII before inspection but the backend framework does, evasion is highly probable.

## Full-Width Characters
Characters that map to ASCII but are visually wider, often interpreted correctly by modern parsers (like IIS/ASP.NET).

*   `＜` (`U+FF1C`) for `<`
*   `＞` (`U+FF1E`) for `>`
*   `＇` (`U+FF07`) for `'`
*   `＂` (`U+FF02`) for `"`

*Payload Construction*: `＜script＞alert(1)＜/script＞`

## Alternative Quotes
The backend may treat typographically similar quotes as standard string delimiters, bypassing generic rules looking for single (`'`) or double (`"`) quotes.

*   `‘` (Left Single Quotation: `U+2018`)
*   `’` (Right Single Quotation: `U+2019`)
*   `“` (Left Double Quotation: `U+201C`)
*   `”` (Right Double Quotation: `U+201D`)

*Payload Construction*: `SELECT * FROM users WHERE username = ‘admin‘--`

## Specific Framework Variations
- Node.js normalization mapping vulnerabilities.
- IIS Best-Fit mapping techniques.
