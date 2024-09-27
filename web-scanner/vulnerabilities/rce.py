import requests
from utils.payload_loader import load_payloads

def test_rce(url, output_file):
    payloads = load_payloads('payloads/rce.txt')
    for payload in payloads:
        response = requests.get(f"{url}/execute?cmd={payload}")
        if "root" in response.text or "user" in response.text:
            output_file.write(f"[!] RCE vulnerability found with payload: {payload}\n")
            return
    output_file.write("[-] No RCE vulnerability detected.\n")
