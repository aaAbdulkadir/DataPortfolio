# parent image
FROM python:3.9

# install FreeTDS and dependencies
RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y

# populate "ocbcinst.ini"
RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini

# install pyodbc (and, optionally, sqlalchemy)
RUN pip install --trusted-host pypi.python.org pyodbc==4.0.26 sqlalchemy==1.3.5 
RUN pip install pandas psycopg2 pyarrow fastparquet

WORKDIR /app
COPY ingest.py ingest.py

ENTRYPOINT [ "python", "ingest.py"]

