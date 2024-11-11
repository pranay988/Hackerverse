import fitz  # pip install PyMuPDF
import re
from collections import defaultdict

pdf_path = '/content/Cybersecurity-Landscape-Map-2024.pdf'
document = fitz.open(pdf_path)

grid_to_category = {
    "A1": "Application Security",
    "A2": "Data Protection",
    "A3": "Endpoint Security",
    "A4": "Identity and Access Management",
    "B1": "Network Security",
    "B2": "Cloud Security",
    "B3": "Threat Intelligence",
    "B4": "Risk Management",
    "C1": "Security Operations",
    "C2": "Incident Response",
    "C3": "Compliance",
    "C4": "Privacy Management",
    "D1": "Digital Forensics",
    "D2": "Vulnerability Management",
    "D3": "Penetration Testing",
    "D4": "Security Awareness",
    "E1": "IoT Security",
    "E2": "Supply Chain Security",
    "E3": "Blockchain Security",
    "E4": "Cryptography",
    "F1": "Access Control",
    "F2": "Privilege Management",
    "F3": "Governance",
    "F4": "Policy Management",
    "G1": "DevSecOps",
    "G2": "Application Lifecycle Security",
    "G3": "Fraud Detection",
    "G4": "Anti-Phishing",
    "H1": "Insider Threat Detection",
    "H2": "Digital Identity",
    "H3": "Authentication",
    "H4": "Authorization",
    "I1": "Behavioral Analysis",
    "I2": "Data Loss Prevention",
    "I3": "Security Analytics",
    "I4": "Malware Protection",
    "J1": "Content Filtering",
    "J2": "Email Security",
    "J3": "Firewall",
    "J4": "Intrusion Prevention System",
    "K1": "Physical Security",
    "K2": "Mobile Security",
    "K3": "Access Management",
    "K4": "Public Key Infrastructure (PKI)",
    "L1": "SIEM (Security Information and Event Management)",
    "L2": "Web Application Firewall (WAF)",
    "L3": "DNS Security",
    "L4": "Endpoint Detection and Response (EDR)",
    "M1": "Zero Trust",
    "M2": "Threat Hunting",
    "M3": "Cybersecurity Insurance",
    "M4": "Cybersecurity Consulting",
    "N1": "Red Teaming",
    "N2": "Blue Teaming"
}


category_data = defaultdict(list)

code_pattern = re.compile(r'^[A-Z]\d{1,2}$')  # Matches codes like "C3", "F6"
company_pattern = re.compile(r'^[\w\s\.\-,&]+$')  # Matches company names

current_code = None

for page_num in range(document.page_count):
    page = document.load_page(page_num)
    text = page.get_text("text").splitlines()  
    
    for line in text:
        line = line.strip()
        
        if code_pattern.match(line):
            current_code = line
        elif current_code and company_pattern.match(line):
            category = grid_to_category.get(current_code, "Unknown Category")
            category_data[category].append(line)

document.close()

for category, companies in category_data.items():
    print(f"{category}:")
    for company in companies:
        print(f"  - {company}")
    print("\n")
