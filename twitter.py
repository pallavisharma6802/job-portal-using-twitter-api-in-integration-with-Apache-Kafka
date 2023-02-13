import json
import tweepy
import pandas as pd
import numpy as np
from kafka import KafkaProducer
from json import dumps
 
with open('/Users/pallavisharma/Desktop/job_portal/big_data/config.json','r') as json_file:
   data = json.loads(json_file.read())
 
CONSUMER_KEY = data['CONSUMER_KEY']
CONSUMER_SECRET = data['CONSUMER_SECRET']
ACCESS_TOKEN = data['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = data['ACCESS_TOKEN_SECRET']
BEARER_TOKEN= data[ 'BEARER_TOKEN']
query="recruitment"
max_results=100
start_time ="2023-01-02T16:00:00Z"

client=tweepy.Client(bearer_token=BEARER_TOKEN, 
    consumer_key=CONSUMER_KEY, 
    consumer_secret=CONSUMER_SECRET, 
    access_token=ACCESS_TOKEN, 
    access_token_secret=ACCESS_TOKEN_SECRET)
    
tweets = client.search_recent_tweets(query=query, 
    max_results=max_results,
    start_time =start_time,
    expansions =['geo.place_id', 'author_id'],
    tweet_fields = ['id','author_id','created_at','text','source','lang','public_metrics'],
    user_fields = ['name','username','location','verified']
    )
tweet_data=tweets.data

f = open("twitter_data.txt", "w")


count=0
data=[]
for tweet in tweet_data:
    count=count+1
    l=[tweet.text,tweet.id,tweet.public_metrics['like_count'],tweet.public_metrics['retweet_count'],len(tweet.text)]
    data.append(l)
    f.write(f"{count} : {l}\n")
f.close()
print(f"Number of tweets extracted: {count}.\n")
data=pd.DataFrame(data=data,columns=['tweet','id','likes','retweet','len'])

result = data.to_json(orient="split")
data.to_csv("data.csv")







