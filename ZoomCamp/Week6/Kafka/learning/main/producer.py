import pandas as pd
from kafka import KafkaProducer
from json import dumps

# kafa producer on local host for broker 9092, encode utf-8 is needed
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=lambda x: dumps(x).encode('utf-8'))

# read data in
league_table = pd.read_excel('data/FootballData.xlsx', 'LeagueTableExport')

# produce a message
for team in league_table['Team']:
    print('Producing teams...')
    producer.send('TeamsV1', value=team)

