import psycopg2
from psycopg2 import sql

class connect_db:
    def load_config():
        dbname = 'intro'
        user = 'postgres'
        password = 'deknoi3004'
        host = 'localhost'
        port = '5432' 
        try:
            conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            return conn
        except Exception as e:
            return e
            # print("Error: Unable to connect to the database.")
            # print(e)