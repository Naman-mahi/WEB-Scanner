import requests
from utils.payload_loader import load_payloads

def test_auth_failures(url, output_file):
    payloads = load_payloads('payloads/auth_failures.txt')
    login_url = f"{url}/login"
    
    for credentials in payloads:
        username, password = credentials.split(':')
        response = requests.post(login_url, data={"username": username, "password": password})
        if "Login successful" in response.text:
            output_file.write(f"[!] Weak Credentials Found: {username}:{password}\n")
            return
    output_file.write("[-] No weak credentials detected.\n")
