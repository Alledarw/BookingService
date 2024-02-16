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
    dict = request.form.to_dict()
    return backend.request_reserve_times(dict)

@app.route("/backend/confirm_reservation", methods=["POST"], endpoint="confirm_reservation")
def confirm_reservation(): 
    dict = request.form.to_dict()
    return backend.confirm_reservation(dict)

@app.route("/backend/reservation_info/<booking_codde>", methods=["GET"], endpoint="reservation_info")
def reservation_info(booking_codde): 
    return backend.get_reservation_info(booking_codde)

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
    return render_template("confirmation.html")


@app.route('/accept_reservation', methods=['POST'], endpoint="accept_reservation")
def accept_reservation():
    email = request.form['email'] 
    #call frontend.random_booking_code()
    #print out the return value
    #show on the screen
    return f"email : {email}"

# -------- ERROR HANDLER  ------------
app.register_error_handler(404, utility.page_404)
app.register_error_handler(405, utility.page_405)
app.register_error_handler(401, utility.page_401)

# For testing in Pycharm IDE
# if __name__ == "__main__":
#  app.run(debug=True)
if __name__ == "__main__":
    app.run(port=8000)
