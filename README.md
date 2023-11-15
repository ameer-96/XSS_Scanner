# XSS Vulnerability Scanner
By: Ameer Abh

Last Updated: 11/13/2023

## Description
This is a Python-based tool designed to detect and report potential Cross-Site Scripting (XSS) vulnerabilities in web applications. It identifies forms and input fields, and tests them for XSS vulnerabilities.

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/xss-scanner.git

# Navigate to the project directory
cd xss-scanner

# Install dependencies
pip install -r requirements.txt
```
# Docker Container
```bash
1. Install Docker
2. Run docker pull bkimminich/juice-shop
3. Run docker run --rm -p 3000:3000 bkimminich/juice-shop
4. Browse to http://localhost:3000
```
## Usage
```bash
# Run the scanner
python3 xss_scanner.py
```
** Note: Remember to make it an executable file. 

## Features
- Web crawling to identify potential injection points.
- Testing forms and URL parameters with XSS payloads.
- Reporting detected vulnerabilities with detailed information.

## Ethical Considerations
- Always obtain permission before scanning a website.
- Use this tool responsibly and ethically for security testing purposes only.