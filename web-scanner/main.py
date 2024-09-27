import sys
import datetime
from vulnerabilities.auth_failures import test_auth_failures
from vulnerabilities.sql_injection import test_sql_injection
from vulnerabilities.xss import test_xss
from vulnerabilities.rce import test_rce
from vulnerabilities.lfi import test_lfi
from vulnerabilities.unvalidated_redirects import test_unvalidated_redirects
from vulnerabilities.idor import test_idor
from vulnerabilities.csrf import test_csrf
from vulnerabilities.security_misconfig import test_security_misconfig

def main(url):
    # Generate a filename based on URL and current date/time
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_url_name = url.replace("http://", "").replace("https://", "").replace("/", "_")
    output_filename = f"{safe_url_name}_{timestamp}.txt"
    
    with open(output_filename, 'w') as output_file:
        output_file.write(f"Testing vulnerabilities for: {url}\n\n")
        
        output_file.write("=== Authentication Failures ===\n")
        result = test_auth_failures(url, output_file)
        if result:
            output_file.write(f"Found: {result}\n")
            output_file.write("Solution: Use strong, unique passwords for all accounts.\n")
            output_file.write("Consider implementing multi-factor authentication.\n")

        output_file.write("\n=== SQL Injection ===\n")
        result = test_sql_injection(url, output_file)
        if result:
            output_file.write(f"Found: {result}\n")
            output_file.write("Solution: Use parameterized queries and prepared statements to prevent SQL injection.\n")

        output_file.write("\n=== Cross-Site Scripting (XSS) ===\n")
        result = test_xss(url, output_file)
        if result:
            output_file.write(f"Found: {result}\n")
            output_file.write("Solution: Sanitize user input and use Content Security Policy (CSP) headers.\n")

        output_file.write("\n=== Remote Code Execution (RCE) ===\n")
        result = test_rce(url, output_file)
        if result:
            output_file.write(f"Found: {result}\n")
            output_file.write("Solution: Validate and sanitize all user inputs before executing any commands.\n")

        output_file.write("\n=== Local File Inclusion (LFI) ===\n")
        result = test_lfi(url, output_file)
        if result:
            output_file.write(f"Found: {result}\n")
            output_file.write("Solution: Validate and sanitize file paths and restrict file access permissions.\n")

        output_file.write("\n=== Unvalidated Redirects ===\n")
        result = test_unvalidated_redirects(url, output_file)
        if result:
            output_file.write(f"Found: {result}\n")
            output_file.write("Solution: Validate redirect URLs against a whitelist of allowed domains.\n")

        output_file.write("\n=== Insecure Direct Object References (IDOR) ===\n")
        result = test_idor(url, output_file)
        if result:
            output_file.write(f"Found: {result}\n")
            output_file.write("Solution: Implement proper access controls and authorization checks for sensitive resources.\n")

        output_file.write("\n=== Cross-Site Request Forgery (CSRF) ===\n")
        result = test_csrf(url, output_file)
        if result:
            output_file.write(f"Found: {result}\n")
            output_file.write("Solution: Implement anti-CSRF tokens and validate them on the server side.\n")

        output_file.write("\n=== Security Misconfigurations ===\n")
        result = test_security_misconfig(url, output_file)
        if result:
            output_file.write(f"Found: {result}\n")
            output_file.write("Solution: Review security configurations and implement best practices for server and application security.\n")

    print(f"Testing completed. Results saved to {output_filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)

    website_url = sys.argv[1]
    main(website_url)
