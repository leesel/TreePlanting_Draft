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


#for tweet in p_tweets:
    #userInstance = UserTree(tweet.author.screen_name, tweet.author.name,
                            #tweet.author.profile_image_url, tweet.text, tweet.author.created_at)
    #accounts[tweet.author.name] = userInstance
    #print(tweet.text)


#val = accounts['PJ']
#print(val.tweet_text)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/tree')
def tree_page():
    return render_template('tree.html')

for tweet in tweepy.Cursor(api.search,q = "I am cancer free", result_type = "recent", include_entities = False, include_rts = False, tweet_node = "extended").items(25):
    #id_tweet = tweet._json['id']
    #username_tweet = tweet._json['user']['screen_name']
    #link_tweet = "https://twitter.com/" + str(username_tweet) + "/status/" + str(id_tweet)
    #status = "Congrats, we are so happy to hear that "
    #congrats = status + link_tweet
    #api.update_status(congrats)

    if 'RT' not in tweet.text:
        username = tweet.author.screen_name
        text = tweet.text

        print([username, text])















if __name__ == '__main__':
   app.run()

