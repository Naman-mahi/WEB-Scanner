import requests

def load_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_security_misconfig(url):
    paths = load_payloads('payloads/security_misconfig.txt')
    for path in paths:
        response = requests.get(f"{url}{path}")
        if response.status_code == 200:
            print(f"[!] Security misconfiguration found at: {url}{path}")
            return
    print("[-] No security misconfiguration detected.")

if __name__ == "__main__":
    test_security_misconfig("http://example.com")
