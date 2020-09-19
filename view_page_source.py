#This is a Python program that output the source code of the Web-Page

import requests
from bs4 import BeautifulSoup

#function to parse and print the page source code
def parse_page(page):
    soup = BeautifulSoup(page, 'html.parser')
    print(soup.prettify())


url = input("Enter url including eg:'http://codehundred.com: ")

#check if url is valid
if (('http' in url) or ('https' in url)) and '.com' in url:
    page = requests.get(url)
    if page.status_code ==200:
        parse_page(page.text)
    else:
        print(page.status_code,"An Error has occured!" )
else:
    print('please enter a valid url')
