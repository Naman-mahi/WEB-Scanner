import requests
from utils.payload_loader import load_payloads

def test_sql_injection(url, output_file):
    payloads = load_payloads('payloads/sql_injection.txt')
    for payload in payloads:
        response = requests.get(f"{url}/search?query={payload}")
        if "error" in response.text or "SQL" in response.text:
            output_file.write(f"[!] SQL Injection vulnerability found with payload: {payload}\n")
            return
    output_file.write("[-] No SQL Injection vulnerability detected.\n")
