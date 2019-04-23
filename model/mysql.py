import os
import time
import pandas as pd
from mysql.connector import Connect
from dotenv import load_dotenv, find_dotenv
from helpers import dotenv
from helpers.spinner import Spinner
load_dotenv(find_dotenv())


class MySqlDB:
    def __init__(self, *params):
        self.params = params
        self.connection = self.connect()

    def connect(self):
        conn = Connect(
            host=os.getenv("MYSQL_HOST"),
            port=os.getenv("MYSQL_PORT"),
            database=os.getenv("MYSQL_SCHEMA"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD")
        )
        return conn
    
    def read(self, sql):
        print("\nQuerying MySQL database\n")
        spinner = Spinner()
        spinner.start()
        start = time.time()
        df = pd.read_sql(sql=sql, con=self.connection, parse_dates=True)
        end = time.time()
        spinner.stop()
        total_time = round((end - start) / 60, 2)
        print(f"It took {total_time} minutes to query MySQL database\n")
        return df
