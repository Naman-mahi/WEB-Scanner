import requests
from utils.payload_loader import load_payloads

def test_unvalidated_redirects(url, output_file):
    payloads = load_payloads('payloads/unvalidated_redirects.txt')
    for payload in payloads:
        response = requests.get(f"{url}/redirect?url={payload}")
        if response.url != url:
            output_file.write(f"[!] Unvalidated redirect found to: {response.url}\n")
            return
    output_file.write("[-] No unvalidated redirects detected.\n")
