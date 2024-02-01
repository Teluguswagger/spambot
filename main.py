import tweepy
import os
from json import dumps

# Twitter API credentials
bearer_key = os.environ.get("TWITTER_BEARER_KEY")
api_key = os.environ.get("TWITTER_API_KEY")
api_secret = os.environ.get("TWITTER_API_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# V2 Twitter API Authentication
client = tweepy.Client(
    bearer_key,
    api_key,
    api_secret,
    access_token,
    access_token_secret,
    wait_on_rate_limit=True,
)

# Upload image to Twitter. Replace 'filename' your image filename.
media_id = api.media_upload(filename="twitter_image.jpg").media_id_string
print(media_id)

# Text to be Tweeted
text = "#Pushpa2TheRule Updates ivvandi ra munda\n@MythriOfficial @PushpaMovie @SukumarWritings @imsarathchandra"

# Send Tweet with Text and media ID
client.create_tweet(text=text, media_ids=[media_id])
print("Tweeted!")
