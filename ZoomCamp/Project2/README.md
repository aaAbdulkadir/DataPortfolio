# Streaming

Producer collects streaming data and sent to kafka. The consumer will be used to read the data in another file which will transform the data using spark transformations. Then, this data will be sent to kafka via the producer and read into the web application using the consumer.

## Collect Data 

- Create python virtual environment. 

```
python3 -m venv venv
```

- Activate the virtual environment

```
source venv/bin/activate
```

- Install relevant modules from requirements.txt

```
pip install -r data/requirements.txt
```
## Scraper

Going to have the top x amount of something and based on them, do sentiment analysis to look at peoples interactions. That will consist of:

- Number of Tweets in different time frames
- The actual tweet text
- Sentiment




## Kafka

## Web Dashboard

- no cashtag
- limited api usage, 2mil tweets per month


improvement:
- run kafka write on another script so queries are faster for dashboard when reading it in
