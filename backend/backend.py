import json
from backend.connection import connection as db
from backend.service import service_db as Service
from backend.appoitment import appoitment_db as Appointment
import random
import string

class Backend:
    def __init__(self):
        self.db = db()
        self.appoitment = Appointment(self.db)
        self.service = Service(self.db)

    # Sprint 1
    # Service Feature
    def request_all_services(self):
        # Query all service
        json_services = self.service.query_all_service()
        json_staff = self.service.query_all_staff()
        json_bundle = self.service.query_service_relate_staff()
 
        output = [] 
        for service_item in json_services:
            service_id = service_item["id"]

            filter_bundle_items = [item for item in json_bundle if item['service_id'] == service_id] 
            staff_list = []
            for bundle_item in filter_bundle_items:
                staff_id = bundle_item["staff_id"]
                selected_staff = next((s for s in json_staff if s["id"] == staff_id), None)
                selected_staff["srs_id"] = bundle_item["srs_id"]

                if not(selected_staff == None):
                    staff_list.append(selected_staff)

            new_item = service_item.copy()
            new_item["staff"] = staff_list
            output.append(new_item)   

        return output

    # Sprint 2 
    # Book feature
    def get_reservation_info(self, booking_code):
        return self.appoitment.get_reservation_info(booking_code)
    #
    def save_reservation(self,day, srs_id, start_at, end_at, email):
        booking_code = self.random_booking_code()
        result_status = self.appoitment.save_reserve_appointment(
            day,
            srs_id,
            booking_code,
            start_at,
            end_at,
            email
        )
       
        message= "You have booked on" if not result_status else "You have booked on" 
        return {"status": result_status,
                    "email": email,
                    "booking_code": booking_code,
                    "message": f"{message} on {day} {start_at}-{end_at}"
                    }
    
    def random_booking_code(self):
        return ''.join(random.choices(string.ascii_lowercase, k=5))


    def request_reserve_times(self, staff_id, service_id): 

        reserve_time_slots = []

        if service_id == None: 
            return reserve_time_slots
        
        if staff_id == None: 
            return reserve_time_slots
        
        #Service info
        selected_service = None
        selected_staff = None
        service_items = self.request_all_services()
        for item in service_items:
            if int(item['id']) == int(service_id):
                selected_service = item 
                # get selected staff info
                for staff in item["staff"]:
                    if int(staff['id']) == int(staff_id):
                        selected_staff = staff
                break
        
        if selected_staff == None: 
            return reserve_time_slots 
        
        if selected_service == None: 
            return reserve_time_slots 

        #Reset needed values
        self.appoitment.reset_value()
        srs_id = selected_staff["srs_id"]
        self.appoitment.time_in_minutes = selected_service["time_in_minutes"]

  

        #1. get booking schedule
        schedule_items = self.appoitment.get_appointment_scheduling(staff_id)
        # 2. get daily time period depends for the service
        #get daily time slots
        daily_time_slots = self.appoitment.get_daily_time_slots()
        for _, daily_time_slot in enumerate(daily_time_slots):
            day = daily_time_slot["day"]
            time_slots = daily_time_slot["time_slot"]
 
            time_period = self.appoitment.get_reserve_time_peroid(time_slots) 
            reserve_time_slots.append({"day": day,
                                        "reserve_time": time_period}) 
       
        #3. set to true if reserve_time_slots has booked
        for schedule_item in schedule_items:
            # Find the item with the matching day
            matching_item = next((item for item in reserve_time_slots if item['day'] == schedule_item['booked_date']), None)

            # Check if the booked_date matches the day in the item
            if not matching_item == None:
                # Iterate over each reserve_time in the item
                for reserve_time in matching_item['reserve_time']:
                    # Check if start_at and end_at match the corresponding time in schedule_item
                    if (
                        schedule_item['start_at'] == reserve_time['from']
                        and schedule_item['end_at'] == reserve_time['to']
                    ):
                        # Set taken to True
                        reserve_time['taken'] = True
        
        #4. remove item if taken = true
        filtered_data = [
                {"day": item["day"],
                 "staff_name": selected_staff["staff_name"],
                                        "staff_code": selected_staff["staff_code"],
                                        "service_name": selected_service["service_name"],
                                        "service_code": selected_service["service_code"],
                                        "time_in_minutes": selected_service["time_in_minutes"],
                                        "price": selected_service["price"],
                                        "service_image": selected_service["image"],
                                        "srs_id": srs_id,
                "reserve_time": [time for time in item["reserve_time"] if not time["taken"]]}
                for item in reserve_time_slots]
        # #5. Convert the modified dictionary back to JSON and return
 
        return filtered_data

