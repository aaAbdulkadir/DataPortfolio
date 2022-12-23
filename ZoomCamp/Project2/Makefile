install:
	pip install -r requirements.txt
twitter_data:
	python3 data/twitter_data.py
stocks_data:
	python3 data/stocks_data.py
kafka_read:
	python3 kafkas/read_data_from_kafka.py
kafka_write:
	python3 kafkas/write_data_to_kafka.py
transform_data:
	python3 kafkas/data_transformations.py
dashboard:
	python3 dashboard/dashboard.py
write:
	python3 dashboard/testing.py
app:
	streamlit run dashboard/dashboard.py;python3 dashboard/testing.py