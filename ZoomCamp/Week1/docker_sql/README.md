Created a docker container of postgres:13 and pgAdmin4 to create a database in a container which can be viewed on the pgAdmin UI. Ingested data into the database by creating a python script which collects the data from the ny dataset website through command line input "curl", and using sqlalchemy to connect to the postgres db. 

Started by learning how to create docker containers for postgres and pgadminm where postgres db was saved locally on my machine. Also, a network was used to connect the two containers which ultimately combined in docker-compose. However, I used a network for the python ingestion docker container created to ingest the data into postgres whenever I needed to.

