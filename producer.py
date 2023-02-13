from kafka import KafkaProducer
from json import dumps
with open('/Users/pallavisharma/Desktop/job_portal/twitter_data.txt') as f:
    data = f.readlines()

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))

for tweet in data:
    tweet=res = bytes(tweet, 'utf-8')
    print(tweet)
    producer.send('temp',tweet)