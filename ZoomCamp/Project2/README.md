# Stock Market Streaming

Producer collects data from stock market data and sent to kafka. The consumer will be used to read the data in another file which will transform the data using spark transformations. Then, this data will be sent to kafka via the producer and read into the web application using the consumer.

## Collect Data Using Websocket

- Create python virtual environment. 

```
python3 -m venv
```

- Activate the virtual environment

```
source venv/bin/activate
```

- Install websocket client from requirements.txt

```
pip install -r data/requirements.txt
```





## Kafka

## Web Dashboard