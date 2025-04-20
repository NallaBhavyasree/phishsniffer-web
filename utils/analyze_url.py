# utils/analyze_url.py

def analyze_url(url):
    # Simple rule-based check for phishing
    if len(url) > 75 or '@' in url or 'http' not in url:
        return 'Phishing'
    return 'Legitimate'
