import requests
from utils.payload_loader import load_payloads

def test_idor(url, output_file):
    payloads = load_payloads('payloads/idor.txt')
    for payload in payloads:
        response = requests.get(f"{url}/resource?id={payload}")
        if "Unauthorized" not in response.text:
            output_file.write(f"[!] IDOR vulnerability found with ID: {payload}\n")
            return
    output_file.write("[-] No IDOR vulnerability detected.\n")
