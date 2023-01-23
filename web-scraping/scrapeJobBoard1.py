from turtle import title
import requests
from bs4 import BeautifulSoup

# tutorial follwed from Martin Breuss
# https://realpython.com/beautiful-soup-web-scraper-python/#an-alternative-to-web-scraping-apis

URL = "https://realpython.github.io/fake-jobs/"
# requests library allows you to fetch static HTML
page= requests.get(URL)

# BeautifulSoup package allows you to parse HTML
# create BS object, page.content holds raw bytes of HTML content (better to decode than text)
soup = BeautifulSoup(page.content, "html.parser")


# find elems by ID, by creating BS object
results = soup.find(id = "ResultsContainer")
print(results.prettify())
# find by class name, select job postings from results object
    # find_all returns iterable
job_elements = results.find_all("div", class_ = "card-content")

# iterate through all jobs
for job_element in job_elements:
    title_element = job_element.find("h2", class_ = 'title is-5')
    company_element = job_element.find('h3', class_ = 'company')
    location_element = job_element.find('p', class_ = 'location')
    print(title_element.text)
    print(company_element.text)
    print(location_element.text.strip())
    print()

# search for jobs based on keyword, only want the h2 title elements
python_jobs = results.find_all('h2', string = lambda text: 'python' in text.lower() )


# Accessing Parent Elements
python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]
for job_element in python_job_elements:
    print(job_element.prettify())
    print()

# Extract Attributes from Elements
for job_element in python_job_elements:
    # pick out the second link
    link_url = job_element.find_all('a')[1]['href']
    print('Apply Here:', link_url)
    # links = job_element.find_all('a')
    # for link in links:
    #     link_url = link['href']
    #     if(link_url == 'https://www.realpython.com'):
    #         continue
    #     print("Apply Here: ", link_url )


# response code 
response = requests.get(URL)
if(response):
    # response will evaluate to True if response.status_code is between 200 and 400 (indicates general success)
    print("Success!")
else:
    print("Not Found")

# # code to save HTML as .txt file
# with open('readme.txt', 'w') as f:
#     f.write(page.text)

# print(page.text)




