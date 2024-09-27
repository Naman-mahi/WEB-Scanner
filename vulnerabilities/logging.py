import requests

def test_logging(url):
    response = requests.get(f"{url}/admin/logs")
    if "Error" in response.text:
        print("[!] Insufficient logging or monitoring detected.")
    else:
        print("[-] Logging and monitoring appear sufficient.")

if __name__ == "__main__":
    test_logging("http://example.com")
