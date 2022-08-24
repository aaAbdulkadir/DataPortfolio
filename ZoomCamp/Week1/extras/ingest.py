from venv import create
import pandas as pd
import argparse
from time import time
from sqlalchemy import create_engine
import os
import urllib
import pyodbc

def main(params):
    user = params.user
    password = params.password
    server = params.server
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
    import sqlalchemy as sa
    connstr = f"mssql+pyodbc://{user}:{password}@{server}/?driver=FreeTDS&port=1433&odbc_options='TDS_Version=8.0'"
    engine = sa.create_engine(connstr, fast_executemany=True)
    conn = engine.connect()

    create_db = f'''
    IF EXISTS (SELECT * FROM sys.databases WHERE name = '{db}')
    BEGIN
        DROP DATABASE {db};  
    END;
    CREATE DATABASE {db};
    '''
    conn.execute(create_db)
    
    # ingestion
    df_iterator = pd.read_csv(csv_name, iterator=True, chunksize=100000) # creats iteration of 100000 chunks
    df = next(df_iterator)

    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace') # only gets column names
    n = 1
    while True:
        t_start = time()
        try:
            df = next(df_iterator) # gets next batch
            df.to_sql(name={table_name}, con=engine, if_exists='append')
            t_end = time()
            print(f'Inserted chunk {100000*n} in {t_end-t_start}')
            n += 1
        except:
            print('Completed!')
            break

if __name__ == '__main__':

    ## use argparse to configure the pipeline through argv input
    parser = argparse.ArgumentParser(description='Ingest CSV data to mssql.')

    # user, password, host, port, dbname, tablename, url
    parser.add_argument('--user', help='user name for mssql')
    parser.add_argument('--password', help='password for sqsql')
    parser.add_argument('--server', help='server for mssql')
    parser.add_argument('--db', help='databse name for mssql')
    parser.add_argument('--table_name', help='table name for mssql')
    parser.add_argument('--url', help='url for mssql')
    args = parser.parse_args()

    main(args)

    print('Script complete!')