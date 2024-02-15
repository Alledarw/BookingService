import requests
from flask import jsonify, request
import json
 
class Frontend:
    def __init__(self):
        self.service_items = None
        self.selected_service = None
        self.selected_staff = None

    def request_all_services(self):
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


    def request_reserve_times(self, staff_id, service_id):
        request_reserve = {"staff_id": staff_id,
                "service_id": service_id}
        
        request_url = request.url_root + f"/backend/daily_reserve_time" 
        # Send a POST request with the form data
        response = requests.post(request_url, data=request_reserve)
        if response.status_code == 200:  # Check for a successful HTTP status code
            return response.json()
        else:
            return {}
     
    def reset_selected_value(self):
        self.selected_staff = None
        self.selected_service = None