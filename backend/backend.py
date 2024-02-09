import json
from backend.connection import connection as db
from backend.service import service_db as Service


class Backend:
    def __init__(self):
        self.db = db()
        self.service = Service(self.db)
        self.service_items = None

    def request_all_services(self):
        if not self.service_items == None: 
            return self.service_items
        
        # Query all service
        json_services = self.service.query_all_service()
        json_staff = self.service.query_all_staff()
        json_bundle = self.service.query_service_relate_staff()
 
        output = [] 
        for service_item in json_services:
            service_id = service_item["id"]

            staff_ids_to_filter = [item for item in json_bundle if item['service_id'] == service_id] 
            staff_list = []
            for staff_id_filter in staff_ids_to_filter:
                staff_id = staff_id_filter["staff_id"]
                selected_staff = next((s for s in json_staff if s["id"] == staff_id), None)

                if not(selected_staff == None):
                    staff_list.append(selected_staff)

            new_item = service_item.copy()
            new_item["staff"] = staff_list
            output.append(new_item)   

        return output

    def request_avalialble_time(self, service_code, staff_code):
        print("your code here")
