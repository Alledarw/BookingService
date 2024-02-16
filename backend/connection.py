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
                port=os.getenv("DB_PORT"),
                # Retrieves the password from the .env file
                password=os.getenv("DB_PASSWORD")
            )
        except Exception as e:
            return print(e)

    def execute_query(self, query, parameters=None, fetchall=False):
        if self.conn:
            try:
                with self.conn.cursor() as cursor:
                    cursor.execute(query, parameters)
                    if fetchall == True:
                        return cursor.fetchall()
                    else: 
                        self.conn.commit()
                        return True
            except Exception as e:
                print(f" ----->> SQL syntex faild {e}")
                print(e)
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
                print(f" ----->> SQL syntex faild {e}")
                print(e)
                return None
            finally:
                # Close the cursor
                if cursor:
                    cursor.close()
        else: 
            print(">> Connection faild")
            return None

    def close_connection(self):
        if self.conn:
            self.conn.close()