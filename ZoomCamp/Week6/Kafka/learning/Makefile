virtual:
	pip install virtualenv &&\
	python3 -m venv venv
# source venv/bin/activate
install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
producer:
	python main/producer.py
consumer:
	python main/consumer.py