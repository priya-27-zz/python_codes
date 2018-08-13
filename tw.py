import tweepy
from textblob import TextBlob

consumer_key = 'kNkM0YV4MproqJenwr8XL29XP'
consumer_secret = '0QPrPrPzrgpXWWhAbyCHI1NoD13BiHrGZuTrTFMrZveCOCXjdU'
access_token = '948261552850747394-GYvYZyB8XuqlkgVKyzBF0QJgADh8TZG'
access_secret = '2RzHUeWGIRVsfNRiHFoDGbtpFnG5SFAbjnNVjnIcs5bWr'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)
p = api.search('Shawshank Redemption')
for tweet in p:
    print(tweet.text)
    an=TextBlob(tweet.text)
    print(an.sentiment)
