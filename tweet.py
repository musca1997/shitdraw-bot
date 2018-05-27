import tweepy
from random import randint
from keys import consumer_key, consumer_secret, access_token, access_token_secret
import time
import os

def post():
    num = randint(0,5000)
    pic_name = str(num) + '.png'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_with_media(pic_name, status='NO.' + str(num) + 'drawing by shitdraw bot')
    os.remove(pic_name)
    print('tweet done! sleeping for another 900s')


if __name__ == '__main__':
    while True:
        post()
        time.sleep(900)
