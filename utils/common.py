import urllib.parse

def normalize_url(url):
    if not url.startswith('http'):
        return f"http://{url}"
    return url