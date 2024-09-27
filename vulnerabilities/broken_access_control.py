# vulnerabilities/broken_access_control.py
import requests

def test_broken_access_control(url):
    restricted_url = f'{url}/admin'
    response = requests.get(restricted_url)
    
    if response.status_code == 200:
        print(f"[!] Broken Access Control: {restricted_url} is accessible without authorization.")
    else:
        print(f"[-] Access Control enforced: {restricted_url} returned {response.status_code}")