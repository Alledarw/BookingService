import requests
from flask import jsonify, request
import random
import string
 
class Frontend:
    def __init__(self):
        self.service_items = None
        self.selected_service = None
        self.selected_staff = None
        self.time_slots = None
        self.reserve_info = None

    def random_booking_code(self):
        return ''.join(random.choices(string.ascii_lowercase, k=5))


    def request_all_services(self):
        #reset value everytime when enter to frontpage
        self.selected_staff = None
        self.selected_service = None
        self.time_slots = None
        self.reserve_info = None

        if not self.service_items == None: 
            return self.service_items

        request_url = request.url_root + "/backend/services"
        response = requests.get(request_url)
        if response.status_code == 200:  # Check for a successful HTTP status code
            return response.json()
        else:
            return {'services': []}
    
    def fillter_service(self, text_search):
        matching_items = []
        for item in self.service_items:
            if text_search.lower() in item["service_name"].lower() or text_search.lower() in item["service_code"].lower():
                matching_items.append(item)
        return matching_items
    
    def get_seleted_reserve_time(self, slot_id):
        # for item in self.time_slots:
        #     if item["slot_id"] == slot_id:
        #         return item

        return {}


    def request_reserve_times(self):
        if self.selected_staff == None:
            return {}
        
        #get avaliable reserve time slots
        staff_id = self.selected_staff["id"]
        service_id = self.selected_service["id"]

        request_reserve = {"staff_id": staff_id,
                "service_id": service_id}
        
        request_url = request.url_root + f"/backend/daily_reserve_time" 
        # Send a POST request with the form data
        response = requests.post(request_url, data=request_reserve)
        if response.status_code == 200:  # Check for a successful HTTP status code
            return response.json()
        else:
            return {}
     
 