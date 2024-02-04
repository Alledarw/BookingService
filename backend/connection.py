import json
from dotenv import load_dotenv
from psycopg2 import DatabaseError, connect
import os

class connection: 
    def __init__(self):
        self.conn = None
        self.load_config()

    def load_config(self):
        # Load environment variables from the .env file
        load_dotenv()
        try:
            self.conn = connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                host=os.getenv("DB_HOST"),
                # Retrieves the password from the .env file
                password=os.getenv("DB_PASSWORD")
            )
        except Exception as e:
            return print(" ++ " + e)
        
    def execute_query(self,query, parameters=None, fetchall=False):
        if self.conn:
            try:
                with self.conn.cursor() as cursor:
                    cursor.execute(query, parameters)
                    return cursor.fetchall() 
            except Exception as e:
                return None
            finally:
                # Close the cursor
                if cursor:
                    cursor.close()
        else: 
            return None
        
    def execute_return_attributed(self,query, parameters=None, fetchall=False):
        if self.conn:
            try:
                with self.conn.cursor() as cursor:
                    cursor.execute(query, parameters)
                    results = cursor.fetchall() 
                    items = []
                    for result in [json.dumps(item[0], indent=2) for item in results]:
                        items.append(result)

                    items = [json.loads(item) for item in items]
                    
                    return items
            except Exception as e:
                return None
            finally:
                # Close the cursor
                if cursor:
                    cursor.close()
        else: 
            return None


    def close_connection(self):
        if self.conn:
            self.conn.close()


# Example query to test the execute_query function
# db = connection() 
# test_query = "SELECT * FROM service"
# result = db.execute_query(test_query, fetchall=True)
# if result:
#     print(result)
# else:
#     print("Query Fail") 



# # Setting up connection to local database
# def execute_query(query, parameters=None, fetchall=False):
#     conn = None
#     try:
#         conn = connect(
#             dbname=os.getenv("DB_NAME"),
#             user=os.getenv("DB_USER"),
#             host=os.getenv("DB_HOST"),
#             # Retrieves the password from the .env file
#             password=os.getenv("DB_PASSWORD")
#         )
#         # Create a cursor to interact with the database
#         with conn.cursor() as cursor:
#             cursor.execute(query, parameters)
#             conn.commit()
#             if fetchall and cursor.description:
#                 return cursor.fetchall()
#     except DatabaseError as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()


# # Example query to test the execute_query function
# test_query = "SELECT * FROM service"
# result = execute_query(test_query, fetchall=True)

# if result:
#     print(result)
# else:
#     print("No data found.") 
