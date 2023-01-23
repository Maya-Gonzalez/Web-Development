import os
from os import environ

twitter_auth_keys = {
    "consumer_key": os.getenv('twitter_consumer_key', ''),
    "consumer_secret": os.getenv('twitter_consumer_secret', ''),
    "access_token": os.getenv('twitter_access_token', ''),
    "access_token_secret": os.getenv('twitter_access_token_secret', '')
}

bitly_auth_keys = {
    "username": os.getenv('bitly_username', ''),
    "password": os.getenv('bitly_password', ''),
    "auth_token": os.getenv('bitly_auth_token', '')
}

BITLY_ACCESS_TOKEN = "07e97263f45195a1fa62d7f154f1c8bed03049b2"# FIXMEEE

ACCESS_TOKEN = "1550211171117985792-etGKgvnhsmX8k23T4u7HynYTpGD2hE"
ACCESS_TOKEN_SECRET = "K7SfRJcFsozAn9beIaxTRJ6PdhlofXxNAo4h7NjWC0U09"

API_KEY = "zjpL33zdENqbwwT7IaFouuHGq"
API_KEY_SECRET = "Jc8ulzyKRnp6x6mO9qpvQVmq0ScJQnzGN16cCzirdCd4j73dyC"

TWITTER_API_KEY = 'Bn5dmjPj2d5MFinkvWqmx1Gxo'
TWITTER_API_KEY_SECRET = 'c4SlQibm58NPy5zmRgHZTWEquq8EdX4hQvwJ4Gf1iMv0Sj5VZw'

TWITTER_BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAI1WfAEAAAAAubbisZnvruUhnRU7lDL0QCsh59k%3DNZWgRzmuHdogK8r7KBZ7vZ7tyAsG0OgfPS6gK55HxCZSPWzuU5'

TWITTER_ACCESS_TOKEN ='1550211171117985792-N1UPUja8qdhXfGbrWa8ahRwPFNpcmm'
TWITTER_ACCESS_TOKEN_SECRET ='1550211171117985792-N1UPUja8qdhXfGbrWa8ahRwPFNpcmm'