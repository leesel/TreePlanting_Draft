import tweepy
import credentials
from models import UserTree
from flask import Flask, render_template, json


app = Flask(__name__)

auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_key, credentials.access_secret)
api = tweepy.API(auth)


p_tweets = api.search("I beat cancer")

accounts = {}


for tweet in p_tweets:
    userInstance = UserTree(tweet.author.screen_name, tweet.author.name,
                            tweet.author.profile_image_url, tweet.text, tweet.author.created_at)
    accounts[tweet.author.name] = userInstance
    print(tweet.text)

c = p_tweets[0].text

#val = accounts['PJ']
#print(val.tweet_text)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/tree')
def tree_page(value):
    val = "Charles"
    return '{}'.format(value)

@app.route('/test')
def test():
    for val in p_tweets:
        g = tree_page(value=val)
        return g
    return


if __name__ == '__main__':
   app.run()