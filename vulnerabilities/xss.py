import requests

def load_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_xss(url):
    payloads = load_payloads('payloads/xss.txt')
    for payload in payloads:
        response = requests.get(f"{url}/search?input={payload}")
        if payload in response.text:
            print(f"[!] XSS vulnerability found with payload: {payload}")
            return
    print("[-] No XSS vulnerability detected.")

if __name__ == "__main__":
    test_xss("http://example.com")
