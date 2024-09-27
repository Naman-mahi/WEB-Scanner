import requests

def load_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_auth_failures(url):
    payloads = load_payloads('payloads/auth_failures.txt')
    login_url = f"{url}/login"
    
    for credentials in payloads:
        username, password = credentials.split(':')
        response = requests.post(login_url, data={"username": username, "password": password})
        if "Login successful" in response.text:
            print(f"[!] Weak Credentials Found: {username}:{password}")
            return
    print("[-] No weak credentials detected.")

if __name__ == "__main__":
    test_auth_failures("http://example.com")
