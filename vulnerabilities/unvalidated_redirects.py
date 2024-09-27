import requests

def load_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_unvalidated_redirects(url):
    payloads = load_payloads('payloads/unvalidated_redirects.txt')
    for payload in payloads:
        response = requests.get(f"{url}/redirect?url={payload}")
        if response.url != url:
            print(f"[!] Unvalidated redirect found to: {response.url}")
            return
    print("[-] No unvalidated redirects detected.")

if __name__ == "__main__":
    test_unvalidated_redirects("http://example.com")
