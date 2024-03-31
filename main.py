import tweepy
import time

# Credentials
api_key = "FENHX6h3SwfOIPDWlFsJOcQr3"
api_secret = "ifvLyVXytfmy0fAvWnfR5Nl2n6NTNh1BTDYmdPP2tfD4qXA0k1"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAADKZsAEAAAAACfq5YP%2FtCKXSr%2BrPs6YpnIe%2FOXI%3Dn1KTggn5dQ6wlqOfvUXXlo3dZ9MKAdKVLg6km1wDWQGHTb6jRm"
access_token = "1752015439629316096-MhqqlKKPnjgBhuOZQ4ffikMDOXedQI"
access_token_secret = "8D7daj2XTgspeJIoS9fQBpjARVsQCYv9tB9nRrolfNPUe"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):

        # Retweeting the tweet
        try:
            # Retweet
            client.retweet(tweet.id)

            # Printing Tweet
            print(tweet.text)

            # Delay
            #time.sleep(1)

        except Exception as error:
            # Error
            print(error)


# Creating Stream object
stream = MyStream(bearer_token=bearer_token)

# Adding terms to search rules
rule = tweepy.StreamRule("( #Pushpa2TheRule) (-is:retweet -is:reply)") 
stream.add_rules(rule, dry_run=True)

# Starting stream
stream.filter()
