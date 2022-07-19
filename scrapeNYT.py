# tutorial follwed from Claudia Ng 
# https://python.plainenglish.io/building-a-news-scraping-twitter-bot-in-python-28eabe17823e

from bs4 import BeautifulSoup
import pandas as pd
import requests

URL = "https://www.nytimes.com/section/world"
page = requests.get(URL)
response = BeautifulSoup(page.text, "html.parser")

# find all elems with <article> tag
articles = response.find_all("article")

articles_dict = []
for article in articles:
    # create new dictionary for each article elem
    article_dict = {}

    title_elem = article.find('h2').find('a')
    # in general: to avoid errors, check if exists before grabbing text 
    if title_elem:
        article_dict['title'] = title_elem.contents[0]

    summary_elem = article.find_all('p')[0]
    if summary_elem :
        article_dict['summary'] = summary_elem.text
    
    link_elem = article.find_all('a')[0]
    if link_elem :
        # if link is not complete, create new full link
        if not link_elem['href'].startswith('https://'):
            article_dict['link'] = 'https://www.nytimes.com/' + link_elem['href']
        else:
            article_dict['link'] = link_elem['href']

    
    # print(article_dict['link'])
    # print()
    articles_dict.append(article_dict)
df = pd.DataFrame(articles_dict)
print(df)
