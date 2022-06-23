#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
from sqlalchemy import create_engine
import argparse


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    url = params.url
    table_name = params.table_name
    data_size = params.data_size
    
    parquet_name = "output.parquet"
    
    # Download the data
    os.system(f"wget {url} -O {parquet_name}")
    
    # Postgres engine for connection
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    df = pd.read_parquet(parquet_name).iloc[-data_size:, :]
    df.head()


    # We change datetime from text
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Create table columns
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    # Insert data into table
    df.to_sql(name=table_name, con=engine, if_exists='append')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest parquet data to Postgres')

    # args: user, password, host, port, database name, table name, parquet url and data size

    parser.add_argument('--user', metavar='u', type=str, help='user name for postgres')
    parser.add_argument('--password', metavar='p', type=str, help='password name for postgres')
    parser.add_argument('--host', metavar='h', type=str, help='host name for postgres')
    parser.add_argument('--port', metavar='pr', type=int, help='port name for postgres')
    parser.add_argument('--db', metavar='d', type=str, help='database name for postgres')
    parser.add_argument('--table_name', metavar='u', type=str, help='name of the table name for storing data')
    parser.add_argument('--url', metavar='r', type=str, help='url of the parquet file')
    parser.add_argument('--data_size', metavar='s', type=int, help='number of line to take')

    args = parser.parse_args()
    
    main(args)






