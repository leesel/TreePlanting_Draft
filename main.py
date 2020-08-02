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

q = ["I am cancer free", "beat it"]
for tweet in tweepy.Cursor(api.search, q , result_type = "recent", include_entities = False, include_rts = False, tweet_node = "extended").items(25):
    id_tweet = tweet._json['id']
    username_tweet = tweet._json['user']['screen_name']
    link_tweet = "https://twitter.com/" + str(username_tweet) + "/status/" + str(id_tweet)
    status = "Congratulations! We are so happy to hear that, come to our website to meet your own virtual tree "
    congrats = status + link_tweet
    user_id = tweet._json['user']['id']
    #text = tweet.text
    #username = tweet.author.screen_name
    
    if 'RT' not in tweet.text:
        api.update_status(congrats)
        api.send_direct_message(user_id, text = "We are so happy and proud that you win this battle with cancer. For that, we want to honor you with a virtual tree on your name, you can visit it on our website. You deserve it. "+ link_tweet)

        #print([username, text])















if __name__ == '__main__':
   app.run()

