# import tweepy
# from  textblob import TextBlob
# # consumer_key="OeGopngjZ9P1r2UxfYKZfM1ez"
# # consumer_key_secret="n1MlljiJq9pu8osFG4RT9pOj99SA76t0r2GbkkILyv5DWaIz8n"
# # access_token="1425550413261000705-QRveycJAwSPi2WtEW6hIFvQ8Y20ynf"
# # access_token_secret="AHvvjphtuLSYGc5WNT7TdWaAculidbqBaFue4PC1dadgQ"
# # auth=tweepy.OAuthHandler(consumer_key,consumer_key_secret)
# # auth.set_access_token(access_token,access_token_secret)
# # api=tweepy.API(auth)
# # tweets = tweepy.Cursor(api.search_tweets, q="India",lang="en").items(10)

# import snscrape.modules.twitter as sntwitter


# query = "india"
# tweets = []
# limit = 50


# for tweet in sntwitter.TwitterSearchScraper(query).get_items():

#     # print(vars(tweet))
#     # break
#     if len(tweets) == limit:
#         break
#     else:
#         tweets.append([tweets.content])
# for tweet in tweets:
#   print(tweet.text)
#   analysis=TextBlob(tweet.text)
#   print(analysis.sentiment)
#   if analysis.sentiment[0]>0:
#     print("Positive")
#   elif analysis.sentiment[0]<0:
#     print("Negative")
#   else:
#     print("Neutral")

# import snscrape.modules.twitter as sntwitter
# from textblob import TextBlob

# query = "india"
# tweets = []
# limit = 50

# for tweet in sntwitter.TwitterSearchScraper(query).get_items():
#     if len(tweets) == limit:
#         break
#     else:
#         tweets.append(tweet.content)

# for tweet in tweets:
#     print(tweet)
#     analysis = TextBlob(tweet)
#     print(analysis.sentiment)
#     if analysis.sentiment.polarity > 0:
#         print("Positive")
#     elif analysis.sentiment.polarity < 0:
#         print("Negative")
#     else:
#         print("Neutral")


# from twitter_scraper_selenium import scrape_profile
# import json

# microsoft = scrape_profile(twitter_username="microsoft", output_format="json", browser="firefox", tweets_count=10)
# with open("a.txt", 'w') as f:
#     json.dump(microsoft, f, indent=4)
from  textblob import TextBlob
f=open("a.txt","r")
tweets=f.readlines()
f.close()
for tweet in tweets:
  # print(tweet.text)
  analysis=TextBlob(tweet)
  # print(analysis.sentiment)
  if analysis.sentiment[0]>0:
    print("Positive")
  elif analysis.sentiment[0]<0:
    print("Negative")
  else:
    print("Neutral")