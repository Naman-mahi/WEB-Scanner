import requests

def load_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_rce(url):
    payloads = load_payloads('payloads/rce.txt')
    for payload in payloads:
        response = requests.get(f"{url}/execute?cmd={payload}")
        if "root" in response.text or "user" in response.text:
            print(f"[!] RCE vulnerability found with payload: {payload}")
            return
    print("[-] No RCE vulnerability detected.")

if __name__ == "__main__":
    test_rce("http://example.com")
