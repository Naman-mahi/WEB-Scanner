# vulnerabilities/fuzzing.py
from wfuzz import Wfuzz
from faker import Faker

def test_fuzzing(url):
    print(f"[*] Fuzzing {url}")
    fake = Faker()
    
    wf = Wfuzz(target=url)
    
    # Example fuzzing with fake data
    wf.fuzz(
        url=f"{url}/login?username=FUZZ&password=FUZZ",
        payloads=[
            ("list", [fake.user_name(), fake.password()]),
        ]
    )
    
    for r in wf:
        if "error" in r.text:
            print(f"[!] Vulnerability found with payload: {r.text}")
        else:
            print(f"[-] No issues found.")