import os
import tweepy
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

def tweet_dog_fact():
    dog_api_url = 'https://dog-api.kinduff.com/api/facts'
    print('fetching dog fact...')
    res = requests.get(dog_api_url)
    tweet_text = res.json()['facts'][0]
    print('tweeting dog fact...')
    client.create_tweet(text=tweet_text)

tweet_dog_fact()
