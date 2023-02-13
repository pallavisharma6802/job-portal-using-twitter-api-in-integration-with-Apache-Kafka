from kafka import KafkaConsumer
consumer = KafkaConsumer('temp_topic',
                        bootstrap_servers=['localhost:9092'],
                        group_id=None)
for msg in consumer:
 print (msg)    