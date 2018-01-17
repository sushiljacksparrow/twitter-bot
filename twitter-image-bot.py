import tweepy as tp
import time
import os

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('tech')

for tech_image in os.listdir('.'):
    api.update_with_media(tech_image)
    time.sleep(60)
