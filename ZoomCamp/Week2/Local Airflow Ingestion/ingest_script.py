import pandas as pd
from time import time
from sqlalchemy import create_engine

def ingest_callabe(user, password, host, port, db, table_name, parquet_name, csv_name):
# these variables will be passed into the script through the .env file

    # change parquet to csv
    df = pd.read_parquet(parquet_name)
    df.to_csv(csv_name)
    print('File saved as csv and ready to ingest...')

    # connect to db
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()
    print('Connected to the database! Now inserting the data...')

    # ingestion
    df_iterator = pd.read_csv(csv_name, index_col=[0], iterator=True, chunksize=100000) # creats iteration of 100000 chunks
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
    print('Succesful! Terminating.')
