def load_payloads(file_path):
    """Load payloads from a specified file."""
    try:
        with open(file_path, 'r') as file:
            payloads = file.readlines()
        return [payload.strip() for payload in payloads if payload.strip()]
    except FileNotFoundError:
        print(f"[!] Payload file not found: {file_path}")
        return []
