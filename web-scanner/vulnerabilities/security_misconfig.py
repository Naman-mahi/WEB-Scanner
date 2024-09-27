import requests

def test_security_misconfig(url, output_file):
    # This would typically include checks for security headers, etc.
    response = requests.get(url)
    security_headers = ["X-Content-Type-Options", "X-Frame-Options", "X-XSS-Protection"]
    for header in security_headers:
        if header not in response.headers:
            output_file.write(f"[!] Missing security header: {header}\n")
    if all(header in response.headers for header in security_headers):
        output_file.write("[-] No security misconfigurations detected.\n")
