#import os
#import subprocess
#Requests allows you to send HTTP requests using python
import requests
#BeautifulSoup is a library that makes it easy to scrape information from web pages
from bs4 import BeautifulSoup
import urllib.parse

#Script Banner
def display_banner():
    banner = r"""
                                      ████
                                    ████████
                                  ████████████
                                ████████████████
                              ████████████████████
                            ████████████████████████
                          ████████████████████████████
                        ████████████████████████████████
                       ██   Welcome to the XXS Scanner ██
                     ████       ────────────────       ████
                   ██████     Created By Ameer Abh     ██████
                 ████████       ────────────────       ████████
               ██████████    Last Updated 11/10/2023   ██████████
             ████████████       ────────────────       ███████████
           █████████████████████████████████████████████████████████
    """

    print(banner)

#Variables List:
#response: Uses the 'requests' library to send an HTTP GET request through its '.get' method to get the HTML content of the specified domain name.
#soup: is a combo of 'requests' and 'BeautifulSoup' library to fetch a webpage HTML and parse the HTML content of that webpage
#form: uses the 'BeautifulSoup' library to search through HTML content for a specific criteria that is "form" <form>(form are HTML tags that are used for inputs)
#
#

#List of payloads  
payloads = ["<SscriptCRIPT>alert(\"XSS\")</SscriptCRIPT>"]

def extract_form_info(form):
    form_info = {
        'action': form.attrs.get('action', ''),
        'method': form.attrs.get('method', 'get').lower(),
        'inputs': [
            {'name': tag.attrs.get('name'), 'type': tag.attrs.get('type', 'text')}
            for tag in form.find_all('input')
        ]
    }
    return form_info

def test_xss(response, payload):
    return payload in response.text

#Function that gets all input fields from the HTML code using beautifulsoup
def XSS_form_scan(enter_domain_name):
  response = requests.get(enter_domain_name)
  soup = BeautifulSoup(response.content, "html.parser")
  forms = soup.find_all("form")

 #iteration loop for form:  
  for form in forms:
    form_info = extract_form_info(form)
    for payload in payloads:
      response = xss_payload(form_info, payload, enter_domain_name)
      if test_xss(response, payload):
        print(f'Vulnerability detected at {enter_domain_name} letsgoooo!!!')

 
def xss_payload(form_info, payload, enter_domain_name):
    url = urllib.parse.urljoin(enter_domain_name, form_info['action'])
    form_data = {}
    for input_field in form_info['inputs']:
        form_data[input_field['name']] = payload if input_field['type'] != 'submit' else 'submit'
    
    if form_info['method'] == 'post':
        response = requests.post(url, data=form_data)
    else:
        response = requests.get(url, params=form_data)
    
    return response
    

#Main Menu to select options:
def main():
    while True:
        print("Select an option:")
        print("1. Scan web page for XSS vulnerabilities")
        #print("2. SQL Injection Scanner *COMING SOON*")
        print("99. Exit")
        
        choice = input("Enter Your Choice:")

        if choice == '1':
            xss_scan = input("Enter the domain name to start scanning:")
            XSS_form_scan(xss_scan)
        #elif choice == '2':
            #get_domain_ip("SQL Injection Scanner *COMING SOON*")
        elif choice == '99':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
  display_banner()
  main()