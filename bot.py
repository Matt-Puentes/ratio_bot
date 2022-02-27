from pydoc import cli
import tweepy
from credentials import *

def main():
    # Authenticate to Twitter
    api = connect_to_twitter_OAuth()

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

    # Create a tweet
    api.update_status("Hello Tweepy!")


def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    # auth = tweepy.Client(BEARER_TOKEN)
    # auth = tweepy.AppAuthHandler(API_KEY, API_KEY_SECRET)
    api = tweepy.API(auth)
    return api

if __name__ == "__main__":
    main()


