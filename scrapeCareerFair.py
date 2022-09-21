'''
A program to quickly identify companies/people/time slots that have available meeting times to book. 
The site does not have any native support to filter by companies, roles, prereqs and availabilty.
Thus, it is incredibly hard to manually sift through all this information, especially during such a time-sensitive situation. 

Current caveat: only works with one url at a time. Does not account for time constraints with personal calendar.
'''
# run with command:
    # /Users/mayagonzalez/miniconda3/bin/python /Users/mayagonzalez/Desktop/Coding/web-scraping/scrapeNYT.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Make GET request
URL = "https://app.careerfairplus.com/abiwt_ca/fair/4382/employer/309034"
response = requests.get(URL)


def checkStatus():
    # check status code (200 is success)
    if response.ok:
        print('Success!')
    else:
        print('Cannot access URL. HTTP response status code: ', response.status_code)       
checkStatus()

# Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Get tags
# print(soup.title)
# print(soup.title.name)
# print(soup.title.child)


# s = soup.find('div', class_='employer-card-title')
# # content = s.find_all('p')
# print(s)
avail = soup.find('div', class_='mobile-employer-card-container')
print(avail)
divs = soup.find_all('div', {'class': 'MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault jss361  jss355 jss356 css-154ogbs'})
for div in divs:
    print(div['data'])


# Get unique URL for each company
    # Get data for each posting. Include availability, session title
        # Nice to have: Go to linked URL and get prereqs.