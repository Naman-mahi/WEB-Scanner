from vulnerabilities import (
    broken_access_control, cryptographic_failures, injection, insecure_design,
    security_misconfigurations, outdated_components, auth_failures, 
    integrity_failures, logging_failures, ssrf
)

# Test URL
target_url = "http://example.com"

# Run each OWASP Top 10 vulnerability test
broken_access_control.test_broken_access_control(target_url)
cryptographic_failures.test_cryptographic_failures(target_url)
injection.test_sql_injection(target_url)
insecure_design.test_insecure_design(target_url)
security_misconfigurations.test_security_misconfiguration(target_url)
outdated_components.test_vulnerable_components(target_url)
auth_failures.test_auth_failures(target_url)
integrity_failures.test_software_integrity(target_url)
logging_failures.test_logging_failures(target_url)
ssrf.test_ssrf(target_url)