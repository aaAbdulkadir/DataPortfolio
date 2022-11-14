# Streaming

Producer collects streaming data and sent to kafka. The consumer will be used to read the data in another file which will transform the data using spark transformations. Then, this data will be sent to kafka via the producer and read into the web application using the consumer.

## Collect Data 

- Create python virtual environment. 

```
python3 -m venv
```

- Activate the virtual environment

```
source venv/bin/activate
```

- Install relevant modules from requirements.txt

```
pip install -r data/requirements.txt
```





## Kafka

## Web Dashboard