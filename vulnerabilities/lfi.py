import requests

def load_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_lfi(url):
    payloads = load_payloads('payloads/lfi.txt')
    for payload in payloads:
        response = requests.get(f"{url}/file?name={payload}")
        if "root" in response.text or "admin" in response.text:
            print(f"[!] LFI vulnerability found with payload: {payload}")
            return
    print("[-] No LFI vulnerability detected.")

if __name__ == "__main__":
    test_lfi("http://example.com")
