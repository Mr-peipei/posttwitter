import twitter
import sys
import os

args = sys.argv

auth = twitter.OAuth(consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
        consumer_secret=os.environ["TWITTER_CONSUMER_SECRET_KEY"],
        token=os.environ["TWITTER_TOKEN"],
        token_secret=os.environ["TWITTER_TOKEN_SECRET"])

tweet = twitter.Twitter(auth=auth)

tweet.statuses.update(status=args[1])

