import json
from backend.service import service
from backend.connect_db import connect_db as connect

class backend:
    def __init__(self):
        self.conn = connect.load_config()
        print(" >>>>> " + self.conn)
    
    def request_all_services():
        return service.get_all_services()

 