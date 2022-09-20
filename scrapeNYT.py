# tutorial follwed from Claudia Ng 
# https://python.plainenglish.io/building-a-news-scraping-twitter-bot-in-python-28eabe17823e

from bs4 import BeautifulSoup
import pandas as pd
import requests
import nltk
import bitly_api
import tweepy
from utils.credentials import twitter_auth_keys 

# folling comment is to fix [the nltk_data] error of 'certificate verify failed' 
# https://github.com/gunthercox/ChatterBot/issues/930#issuecomment-322111087

# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download()

nltk.download('punkt')
from nltk.corpus import stopwords


# WEB SCRAPING 
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


# TEXT PROCESSING
def clean_text(article):
    #FIXMEEEE
    # if(article is None) or (pd.isna(article)):
    #     return None
    if(article is None):
        return None
    
    
    # tokenization: split string sequence into individual words
    summary_elem = article.find_all('p')[0]
    if summary_elem :
        summary_elem= summary_elem.text
    tokens = nltk.word_tokenize(summary_elem)

    # remove leading and trailing spaces
    tokens_flattened = [t.strip() for t in tokens] 

    # remove any non-alphabet characters
    token_chars = [t.lower() for t in tokens_flattened if t.isalpha()]

    # method without using list comprehension 
    # tokenChars = []
    # for t in tokens_flattened:
    #     if(t.isalpha()):
    #         tokenChars.append(t.lower())
     
    
    # create list of stop words (non-target words)
    stop_words = list(set(stopwords.words('english')))
    # append extras to list of stop words
    [stop_words.append(x) for x in ['said', 'says', 'say']]
    # Remove stop words 
    cleaned_tokens = [t for t in token_chars if t not in stop_words]
    return cleaned_tokens


# for article in articles:
#     clean_text(article)

print(clean_text(articles[0]))
print(articles[0].find_all('p')[0])

# Count word frequences
def get_token_frequencies(cleaned_text, n_tokens=5):
    # count frequency of tokens
    fdist_tokens = nltk.FreqDist(cleaned_text)
    fdist_tokens_sorted = {k:v for k,v in sorted(fdist_tokens.items(), key = lambda x : x[1],reverse= True)[:n_tokens]}
    return fdist_tokens_sorted
print(get_token_frequencies(clean_text(articles[0])))

# shorten URLs

# FIXMEE: save keys in another file that isn't pushed to github
# Autherntication



auth = tweepy.OAuthHandler(twitter_auth_keys[API_KEY], twitter_auth_keys[API_KEY_SECRET])
auth.set_access_token(twitter_auth_keys[ACCESS_TOKEN], twitter_auth_keys[ACCESS_TOKEN_SECRET])

# Tweet message using API
api = tweepy.API(auth)
api.update_status(status = "Tweeting with Tweepy in Python!!")

