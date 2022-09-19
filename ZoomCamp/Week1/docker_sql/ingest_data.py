import pandas as pd
import argparse
from time import time
from sqlalchemy import create_engine
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    
    # download data
    csv_name = 'output.parquet' # it is a parquet file

    # os.system(f'curl {url} -O {csv_name}')
    os.system(f'curl -kL {url} -o {csv_name}')

    # change parquet to csv
    df = pd.read_parquet(csv_name)
    df.to_csv('output.csv')
    csv_name = 'output.csv'

    # connect to db
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    engine.connect()

    # ingestion
    df_iterator = pd.read_csv(csv_name, iterator=True, chunksize=100000) # creats iteration of 100000 chunks
    df = next(df_iterator)

    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace') # only gets column names
    n = 1
    while True:
        t_start = time()
        try:
            df = next(df_iterator) # gets next batch
            df.to_sql(name=table_name, con=engine, if_exists='append')
            t_end = time()
            print(f'Inserted chunk {100000*n} in {t_end-t_start}')
            n += 1
        except:
            print('Completed!')
            break

if __name__ == '__main__':

    ## use argparse to configure the pipeline through argv input
    parser = argparse.ArgumentParser(description='Ingest CSV data to postgres.')

    # user, password, host, port, dbname, tablename, url
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='databse name for postgres')
    parser.add_argument('--table_name', help='table name for postgres')
    parser.add_argument('--url', help='url for postgres')
    args = parser.parse_args()

    main(args)

    print('Script complete!')