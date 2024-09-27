import requests

def load_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_sql_injection(url):
    payloads = load_payloads('payloads/sql_injection.txt')
    for payload in payloads:
        response = requests.get(f"{url}/search?query={payload}")
        if "username" in response.text:
            print(f"[!] SQL Injection vulnerability found with payload: {payload}")
            return
    print("[-] No SQL Injection vulnerability detected.")

if __name__ == "__main__":
    test_sql_injection("http://example.com")
