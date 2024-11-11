#### Overview

This repository contains two Python scripts designed for categorization and processing of cybersecurity data. Here's a brief description of each script:

1. **`category-optiv.py`**:
   - This script processes data from a PDF document containing cybersecurity landscape information. It maps grid codes (e.g., "A1", "B2") to cybersecurity categories (e.g., "Application Security", "Network Security") and associates company names with these categories based on their positions in the document.
   - It uses the PyMuPDF library (`fitz`) to read PDF contents and relies on regular expressions to identify and categorize company data.

2. **`scrapy.py`**:
   - This script fetches and parses content from a given URL, categorizing the page based on cybersecurity-related keywords.
   - It leverages the `requests` library for HTTP requests and `BeautifulSoup` for web scraping.
   - The categorization is determined based on matching specific keywords within the text content of the webpage.

---

#### Prerequisites

- Ensure Python 3.x is installed.
- Required libraries:
  - `PyMuPDF` (for `category-optiv.py`)
  - `requests` and `BeautifulSoup` from `beautifulsoup4` (for `scrapy.py`)
- You can install the dependencies using the following commands:
  ```bash
  pip install PyMuPDF requests beautifulsoup4
  ```

---

#### How to Use

##### 1. `category-optiv.py`

**Description**:  
This script processes a cybersecurity landscape map PDF to categorize companies based on predefined grid codes.

**Steps to Run**:
1. Place the target PDF (e.g., `Cybersecurity-Landscape-Map-2024.pdf`) in the working directory. Download it from the Optiv offical website.
2. Modify the `pdf_path` variable to point to your PDF file.
3. Run the script:
   ```bash
   python category-optiv.py
   ```
4. Or you can open the file in softwares like Googel Colab or Jupyter etc.
5. The script outputs categorized companies based on grid codes, printed to the console.

##### 2. `scrapy.py`

**Description**:  
This script scrapes content from a provided URL and categorizes it based on keywords associated with cybersecurity categories.

**Steps to Run**:
1. Execute the script:
   ```bash
   python scrapy.py
   ```
2. Or you can open the file in softwares like Googel Colab or Jupyter etc.
3. Enter the target URL when prompted.
4. The detected cybersecurity categories (if any) will be printed to the console.

---
