import requests

def test_ssrf(url):
    print(f"[*] Testing SSRF on {url}")
    with open('payloads/ssrf_payloads.txt') as payloads:
        for payload in payloads:
            test_url = f"{url}?url={payload.strip()}"
            response = requests.get(test_url)
            if "localhost" in response.text or response.status_code == 200:
                print(f"[!] SSRF Vulnerability found with payload: {payload.strip()}")
            else:
                print(f"[-] No SSRF vulnerability for payload: {payload.strip()}")