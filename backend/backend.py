import json
from backend.connection import connection as db
from backend.service import service_db as Service

class Backend:
    def __init__(self):
        self.db = db()
        self.service = Service(self.db)
        
    def request_all_services(self):
        # Query all service
        json_services = self.service.query_all_service()
        json_staff = self.service.query_all_staff()
        json_bundle = self.service.query_service_relate_staff()
       
        output = []
        for bundle_item in json_bundle:
            service_id = int(bundle_item["service_id"])
            staff_id = int(bundle_item["staff_id"]) 

            service_id = bundle_item["service_id"]
            staff_id = bundle_item["staff_id"]

            # Find the service and staff based on their IDs
            selected_service = next((s for s in json_services if s["id"] == service_id), None)
            selected_staff = next((s for s in json_staff if s["id"] == staff_id), None)

            # If both service and staff are found, create the desired output
            if selected_service and selected_staff:
                output_item = selected_service.copy()
                output_item["staff"] = [{
                    "image": selected_staff["image"],
                    "staff_code": selected_staff["staff_code"],
                    "staff_name": selected_staff["staff_name"]
                }]
                output.append(output_item)

        return output
    
    def request_avalialble_time(self, service_code, staff_code):
        print("your code here")
 