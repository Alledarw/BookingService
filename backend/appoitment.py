from datetime import datetime, timedelta
import uuid

class appoitment_db: 
    def __init__(self, db):
        self.db = db
       
        self.time_period = 15
        self.reserve_in_advance = 7
 
        self.current_date = datetime.now() 
        self.start_time = datetime.strptime("09:00", "%H:%M")
        self.end_time = datetime.strptime("18:00", "%H:%M")
        self.time_increment = timedelta(minutes=self.time_period) 
  

    def save_reserve_appointment():
        print("save") 


    def get_appointment_scheduling(self, staff_id):
        query = """SELECT JSON_BUILD_OBJECT(
                        'srs_id', srs_id
                        ) AS json_data
                        FROM staff_relate_service where staff_id = %s 
                    """  % (staff_id)
       
        srs_info = self.db.execute_return_attributed(query, fetchall=True)

        if not srs_info == None : 
            srs_ids = [item["srs_id"] for item in srs_info]
            result_string = ', '.join(str(srs_id) for srs_id in srs_ids)
            query = """SELECT JSON_BUILD_OBJECT(
                            'id', id,
                            'srs_id', srs_id,
                            'booking_code', booking_code,
                            'start_at', start_at,
                            'end_at', end_at,
                            'booked_date', booked_date,
                            'email', email,
                            'is_booked', is_booked
                            ) AS json_data
                            FROM appointment_scheduling where srs_id IN (%s);
                    """   % (result_string)

            schedule_info = self.db.execute_return_attributed(query, fetchall=True)
            if not schedule_info == None : 
                return schedule_info
       
        return None 


    def get_reserve_time_peroid(self, time_slots):
        if time_slots == None:
            return []
          
        #get first time slot
        first_item = time_slots[0]
        amount_of_slot_of_service = self.time_in_minutes/self.time_period
       
        time_from = None
        outcome = []

        is_no_time_slot = True
        while is_no_time_slot:
            
            if time_from is None:
                time_from = first_item["from"] 
      
            time_to = datetime.strptime(time_from, '%H:%M') + timedelta(minutes=self.time_in_minutes) 
            
            time_slots,service_slots = self.get_slots_period(time_slots, time_to)
            
            if type(time_slots) == list:
                if len(time_slots) > 0:
                    time_from = time_slots[0]["from"]
   
            if len(service_slots) == amount_of_slot_of_service: 
                outcome.append(self.get_service_time_period(service_slots))

            is_no_time_slot = len(time_slots) > 0
 
        return outcome
 

    # get slot for each period 
    # outcome [{'day': '2024-02-11', 'avaliable_time': [{'from': '09:00', 'to': '10:30'}, ...]
    def get_slots_period(self, time_slots, time_servie_end):
        last_index = 0
        service_slots = []
        time_slot_left = []
        for index , time_slot in enumerate(time_slots):
            time_servie_end_obj = time_servie_end
            time_in_slot_obj = datetime.strptime(time_slot["to"], '%H:%M') - timedelta(minutes=1)
            
            if time_in_slot_obj < time_servie_end_obj:
                last_index = index
                service_slots.append(time_slot)
                time_slot_left = time_slots[last_index+1:]

            if time_in_slot_obj > time_servie_end_obj:
                return time_slot_left, service_slots  
           
        return time_slot_left, service_slots 
    
    #Get time dayily slots for reserve in advance
    def get_daily_time_slots(self): 
        outcome = []
        # Print the next 7 days with time slots
        for _ in range(self.reserve_in_advance):
            # Format the date
            formatted_date = self.current_date.strftime("%Y-%m-%d")

            # Initialize time slot list
            time_slots = []

            # Generate time slots
            current_time = self.start_time
            while current_time < self.end_time:
                time_slot = {
                    'day': formatted_date,
                    'from': current_time.strftime("%H:%M"),
                    'to': (current_time + self.time_increment).strftime("%H:%M")}
                time_slots.append(time_slot)
                current_time += self.time_increment

            # Print the outcome for the day
            outcome.append({"day": formatted_date, "time_slot": time_slots}) 
            # Move to the next day
            self.current_date += timedelta(days=1)
        return outcome

    # get time period 
    # 1 period can have many time slots 
    # outcome : {'from': "09:00", 'to': "10:30", "taken":False}
    def get_service_time_period(self, service_time_slot):
        #get first time slot
        first_item = service_time_slot[0]["from"]
        #last_item = service_time_slot[-1]
        last_item = (datetime.strptime(service_time_slot[-1]["to"], '%H:%M') - timedelta(minutes=1)).strftime("%H:%M")
        unique_id = uuid.uuid4()
        return {"slot_id": unique_id, 'from': first_item, 'to': last_item, "taken":False}
    
    # reset value when call endpoint /backend/reserve_time/<staff_id>/<service_id>
    def reset_value(self):
        self.time_in_minutes = None
        self.srs_id = None

        self.current_date = datetime.now() 
        self.start_time = datetime.strptime("09:00", "%H:%M")
        self.end_time = datetime.strptime("18:00", "%H:%M")
        self.time_increment = timedelta(minutes=self.time_period) 