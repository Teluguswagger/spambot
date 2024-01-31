import tweepy
from datetime import datetime

# Twitter API credentials
api_key = os.environ.get("TWITTER_API_KEY")
api_secret = os.environ.get("TWITTER_API_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Tweet text and timing
tweet_text = "#Pushpa2TheRule Updates ivvandi ra munda\n@MythriOfficial @PushpaMovie @SukumarWritings @imsarathchandra"
tweet_time = "2024-01-31 21:45:00"  # Format: "YYYY-MM-DD HH:MM:SS"

# Convert tweet_time to datetime object
tweet_datetime = datetime.strptime(tweet_time, "%Y-%m-%d %H:%M:%S")

# Check if it's time to tweet
if datetime.now() >= tweet_datetime:
    # Send tweet
    api.update_status(tweet_text)
    print("Tweeted successfully at:", datetime.now())
else:
    print("It's not time to tweet yet.")
