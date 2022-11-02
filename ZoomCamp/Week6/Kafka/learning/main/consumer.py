from kafka import KafkaConsumer
from json import loads
import pandas as pd

consumer = KafkaConsumer(
    'TeamsV1', # reads the producer sent by its name
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='consumer.group.id.Teams.1',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

# load messages here
while True:
    print('Loading data...')
    for message in consumer:
        message = message.value
        print(message)