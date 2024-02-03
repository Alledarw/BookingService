from dotenv import load_dotenv
from psycopg2 import DatabaseError, connect

import os

# Load environment variables from the .env file
load_dotenv()


# Setting up connection to local database
def execute_query(query, parameters=None, fetchall=False):
    conn = None
    try:
        conn = connect(
            dbname="BookingDB",
            user="postgres",
            host="localhost",
            # Retrieves the password from the .env file
            password=os.getenv("DB_PASSWORD")
        )
        # Create a cursor to interact with the database
        with conn.cursor() as cursor:
            cursor.execute(query, parameters)
            conn.commit()
            if fetchall and cursor.description:
                return cursor.fetchall()
    except DatabaseError as e:
        print(e)
    finally:
        if conn:
            conn.close()


# Example query to test the execute_query function
test_query = "SELECT * FROM service"
result = execute_query(test_query, fetchall=True)

if result:
    print(result)
else:
    print("No data found.")
