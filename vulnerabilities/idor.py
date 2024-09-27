import requests

def load_payloads(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def test_idor(url):
    ids = load_payloads('payloads/idor.txt')
    for id in ids:
        response = requests.get(f"{url}/user/profile?id={id}")
        if "User not found" not in response.text:
            print(f"[!] IDOR vulnerability found with ID: {id}")
            return
    print("[-] No IDOR vulnerability detected.")

if __name__ == "__main__":
    test_idor("http://example.com")
