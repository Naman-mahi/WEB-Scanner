import requests
from utils.payload_loader import load_payloads

def test_lfi(url, output_file):
    payloads = load_payloads('payloads/lfi.txt')
    for payload in payloads:
        response = requests.get(f"{url}/file?name={payload}")
        if "root" in response.text or "admin" in response.text:
            output_file.write(f"[!] LFI vulnerability found with payload: {payload}\n")
            return
    output_file.write("[-] No LFI vulnerability detected.\n")
