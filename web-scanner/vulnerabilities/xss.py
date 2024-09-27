import requests
from utils.payload_loader import load_payloads

def test_xss(url, output_file):
    payloads = load_payloads('payloads/xss.txt')
    for payload in payloads:
        response = requests.get(f"{url}/search?input={payload}")
        if payload in response.text:
            output_file.write(f"[!] XSS vulnerability found with payload: {payload}\n")
            return
    output_file.write("[-] No XSS vulnerability detected.\n")
