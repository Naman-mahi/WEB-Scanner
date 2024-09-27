import requests
from utils.payload_loader import load_payloads

def test_csrf(url, output_file):
    # Here you would simulate CSRF attack vectors
    payloads = load_payloads('payloads/csrf.txt')
    for payload in payloads:
        response = requests.post(f"{url}/action", data={"token": payload})
        if "action performed" in response.text:
            output_file.write(f"[!] CSRF vulnerability potentially exploitable with payload: {payload}\n")
            return
    output_file.write("[-] No CSRF vulnerability detected.\n")
