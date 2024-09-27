# vulnerabilities/cryptographic_failures.py
import requests

def test_cryptographic_failures(url):
    if not url.startswith("https"):
        print("[!] Cryptographic Failure: HTTPS is not enforced.")
    
    try:
        response = requests.get(url, verify=True)
        if response.raw.version in [768, 769]:  # TLS 1.0 or 1.1
            print("[!] Weak TLS Version Detected.")
        else:
            print("[-] Strong TLS version detected.")
    except requests.exceptions.SSLError:
        print("[!] SSL Error or Invalid Certificate Detected.")