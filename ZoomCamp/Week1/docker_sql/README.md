Created a docker container of postgres:13 and pgAdmin4 to create a database in a container which can be viewed on the pgAdmin UI. Ingested data into the database by creating a python script which collects the data from the ny dataset website through command line input "curl", and using sqlalchemy to connect to the postgres db. 

Started by learning how to create docker containers for postgres and pgadmin where postgres db was saved locally on my machine. Also, a network was used to connect the two containers which ultimately combined in docker-compose. However, I used a network for the python ingestion docker container created to ingest the data into postgres whenever I needed to.

The following screenshots show how I accessed the postgres database on pgadmin:


Login to database

![image](https://user-images.githubusercontent.com/72317571/187291926-21a5ecc2-a712-4e63-b03c-c4d092378c2b.png)

Data

![image](https://user-images.githubusercontent.com/72317571/187292105-80b563de-b71f-48a2-88a3-ef130097637f.png)
