import requests
from bs4 import BeautifulSoup

categories = {
    "Network Security": ["firewall", "VPN", "intrusion detection", "IDS", "IPS"],
    "Endpoint Security": ["antivirus", "EDR", "endpoint security", "malware"],
    "Application Security": ["WAF", "code analysis", "application security", "OWASP"],
    "Cloud Security": ["cloud security", "CASB", "IAM", "cloud protection"],
    "Data Security": ["data encryption", "DLP", "tokenization", "data security"],
    "Identity and Access Management": ["multi-factor authentication", "MFA", "SSO", "IAM"],
    "SIEM": ["SIEM", "security information and event management", "log analysis", "Graylog", "Splunk"],
}

def categorize_security(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        page_text = soup.get_text().lower()

        detected_categories = set()
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword.lower() in page_text:
                    detected_categories.add(category)
                    break  

        return detected_categories if detected_categories else "No specific cybersecurity category detected."

    except requests.RequestException as e:
        return f"An error occurred: {e}"

url = input("enter url")
security_categories = categorize_security(url)
print("Detected cybersecurity categories:", security_categories)
