from flask import (Flask, render_template, request, redirect, url_for, json)
from backend.backend import Backend
from frontend.frontend import Frontend
import frontend.utility as utility

app = Flask(__name__)

backend = Backend()
frontend = Frontend()

# #################### BACKEND ##########################
@app.route("/backend/services", methods=["GET"])
def all_service():
    services = backend.request_all_services()
    return services

@app.route("/backend/daily_reserve_time", methods=["POST"], endpoint="daily_reserve_time")
def daily_reserve_time(): 
    staff_id = request.form['staff_id']
    service_id = request.form['service_id']
    # return only avaliable time slots 
    return backend.request_reserve_times(service_id, staff_id) 

# #################### FRONTEND ##########################
@app.route('/', methods=['GET'], endpoint="home")
def home():
    #get all services
    frontend.service_items = frontend.request_all_services()

    #if search service name
    if not (request.args.get('text_search') == None):
        text_search = request.args.get('text_search')
        show_service_items = frontend.fillter_service(text_search)
    else:
        show_service_items = frontend.request_all_services()

    return render_template("home.html", service_items=show_service_items)

@app.route('/staff/<service_code>', methods=['GET'], endpoint="staff")
def staff(service_code):
    #Redirect to home if selected_service == None
    # if frontend.selected_service == None:
    #     return redirect(url_for('home'))
    
    #get the selected service
    frontend.selected_service = next(
        (item for item in frontend.service_items if item['service_code'] == service_code), None)

    return render_template("staff.html",
                           staff_items=frontend.selected_service["staff"],
                           selected_service=frontend.selected_service)

@app.route('/reserve_time/<staff_code>', methods=['GET'], endpoint="reserve_time")
def reserve_time(staff_code):
    #Redirect to home if selected_service == None
    if frontend.selected_service == None:
        return redirect(url_for('home'))

    # get selected staff
    if not frontend.selected_service["staff"] == None:
        frontend.selected_staff = next(
            (item for item in frontend.selected_service["staff"] if item['staff_code'] == staff_code), None)
    
    #Redirect to home if selected_staff == None
    if frontend.selected_staff == None:
        service_code = frontend.selected_service["service_code"]
        return redirect(url_for('staff', service_code=service_code)) 

    frontend.time_slots = frontend.request_reserve_times()
    
    return render_template("reserve_time.html", 
                           selected_service=frontend.selected_service, 
                           selected_staff=frontend.selected_staff,
                           time_slots=frontend.time_slots)
    

@app.route('/confirmation/<book_type>/<slot_id>', methods=['GET'], endpoint="confirmation")
def confirmation(book_type, slot_id):
    if frontend.time_slots == None:
        return redirect(url_for('home'))
    
    # Find the dictionary with the specified 'slot_id' and retrieve 'day' as well
    frontend.reserve_info = next(({'reserve_info': item, 'reserve_time': slot} 
                       for item in frontend.time_slots for slot in item.get('reserve_time', []) 
                       if slot['slot_id'] == slot_id), None)
    if frontend.reserve_info:
        frontend.reserve_info['reserve_info'].pop('reserve_time', None)
    else: 
        return redirect(url_for('home'))
    
    #confirmation_page = "confirmation_member.html" if book_type == "member" else "confirmation_guest.html"
    confirmation_page = "confirmation.html"
    return render_template(confirmation_page, 
                           reserve_info=frontend.reserve_info['reserve_info'],
                           reserve_time=frontend.reserve_info['reserve_time']
                           )

@app.route('/accept_reservation', methods=['POST'], endpoint="accept_reservation")
def accept_reservation():
    email = request.form['email']
    booking_code = frontend.random_booking_code() 

    return f"email : {email} booking code: {booking_code}"


# -------- ERROR HANDLER  ------------
app.register_error_handler(404, utility.page_404)
app.register_error_handler(405, utility.page_405)
app.register_error_handler(401, utility.page_401)

# For testing in Pycharm IDE
# if __name__ == "__main__":
#  app.run(debug=True)
if __name__ == "__main__":
    app.run(port=8000)
