from turtle import title
import requests
from bs4 import BeautifulSoup

# tutorial follwed from Martin Breuss
# https://realpython.com/beautiful-soup-web-scraper-python/#an-alternative-to-web-scraping-apis

# 2nd Website!!! : Python Job Board
URL = "https://pythonjobs.github.io/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


results = soup.find(id = 'content')
# print(results.prettify())

job_elements = results.find_all('div', class_ = 'job')

for job_element in job_elements:
    title_element = job_element.find('h1').find('a').contents[0]
    location_element = job_element.span.text
    # location_element = job_element.find('span', class_ = 'info').text
    time_element = job_element.find('span') .contents[0].text
    company_element = job_element.span
    # print(job_element, end = '\n'*2)
    print(time_element)
    print()

