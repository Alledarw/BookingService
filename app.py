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
    """
    Retrieve all services.
    This endpoint returns a list of all available services.

    Returns:
    - JSON: A list of dictionaries containing service information.
    """
    services = backend.request_all_services()
    return services


@app.route("/backend/daily_reserve_time", methods=["POST"], endpoint="daily_reserve_time")
def daily_reserve_time():
    """
    Endpoint to retrieve daily reserve times with status.
    This endpoint accepts a POST request with form data containing parameters like 'staff_id' and 'service_id'.
    
    Args:
    - request.form['staff_id'] (str): The ID of the staff.
    - request.form['service_id'] (str): The ID of the service.

    Returns:
    - JSON: A response containing daily reserve times based on the provided parameters.
    """
    service_id = request.form["service_id"]
    staff_id = request.form["staff_id"]
    return backend.request_reserve_times(service_id, staff_id)


@app.route("/backend/save_reservation", methods=["POST"], endpoint="confirm_reservation")
def save_reservation():
    """
    Endpoint to save a reservation.
    This endpoint accepts a POST request with form data containing necessary parameters.

    Args:
    - request.form['day'] (str): Day of the reservation.
    - request.form['srs_id'] (str): Bundle id for selected service and staff.
    - request.form['start_at'] (str): Start time.
    - request.form['end_at'] (str): End time.
    - request.form['email'] (str): Email.

    Returns:
    - JSON: A response confirming the reservation or providing relevant information.
    """
    day = request.form["day"]
    srs_id = request.form["srs_id"]
    start_at = request.form["start_at"]
    end_at = request.form["end_at"]
    email = request.form["email"]
    return backend.save_reservation(day, srs_id, start_at, end_at, email)


@app.route("/backend/reservation_info/<booking_code>", methods=["GET"], endpoint="reservation_info")
def reservation_info(booking_code):
    """
    Endpoint to retrieve reservation information.
    This endpoint accepts a GET request with the booking code as part of the URL.

    Args:
    - booking_code (str): The unique booking code associated with the reservation.

    Returns:
    - JSON: A response containing information about the reservation corresponding to the booking code.
    """
    return backend.get_reservation_info(booking_code)

# #################### FRONTEND ##########################


@app.route('/', methods=['GET'], endpoint="home")
def home():
    """
    Endpoint for the home page.
    This endpoint handles a GET request and retrieves all services. Optionally, it filters services based on a search query.

    Args:
    - request.args.get('text_search') (str, optional): The search query to filter services by name.

    Returns:
    - HTML template: Renders the home.html template with the list of services to display.
    """
    # get all services
    frontend.service_items = frontend.request_all_services()

    # if search service name
    if not (request.args.get('text_search') == None):
        text_search = request.args.get('text_search')
        show_service_items = frontend.fillter_service(text_search)
    else:
        show_service_items = frontend.request_all_services()

    return render_template("home.html", service_items=show_service_items)


@app.route('/staff/<service_code>', methods=['GET'], endpoint="staff")
def staff(service_code):
    """
    Endpoint to display staff associated with a selected service.

    This endpoint handles a GET request and redirects to the home page if no service is selected.
    It retrieves the selected service based on the provided service code and renders the staff.html template.

    Args:
    - service_code (str): The service code associated with the selected service.

    Returns:
    - HTML template: Renders the staff.html template with the list of staff members for the selected service.
    """
    # Redirect to home if selected_service == None
    if not frontend.service_items:
        return redirect(url_for('home'))

    # get the selected service
    frontend.selected_service = next(
        (item for item in frontend.service_items if item['service_code'] == service_code), None)

    return render_template("staff.html",
                           staff_items=frontend.selected_service["staff"],
                           selected_service=frontend.selected_service)


@app.route('/reserve_time/<staff_code>', methods=['GET'], endpoint="reserve_time")
def reserve_time(staff_code):
    """
    Endpoint to display available reservation times for a selected staff member.

    This endpoint handles a GET request and redirects to the home page if no service is selected.
    It retrieves the selected staff member based on the provided staff code and renders the reserve_time.html template.

    Args:
    - staff_code (str): The staff code associated with the selected staff member.

    Returns:
    - HTML template: Renders the reserve_time.html template with the available reservation times for the selected staff.
    """

    # Redirect to home if selected_service == None
    if frontend.selected_service == None:
        return redirect(url_for('home'))

    # get selected staff
    if not frontend.selected_service["staff"] == None:
        frontend.selected_staff = next(
            (item for item in frontend.selected_service["staff"] if item['staff_code'] == staff_code), None)

    # Redirect to home if selected_staff == None
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
    """
    Endpoint to display the confirmation page for a booked reservation.

    This endpoint handles a GET request and redirects to the home page if no reservation information is available.
    It retrieves reservation details based on the provided 'slot_id' and 'book_type', and renders the confirmation.html template.

    Args:
    - book_type (str): The type of booking, either "member" or "guest".
    - slot_id (str): The unique identifier for the selected reservation time slot.

    Returns:
    - HTML template: Renders the confirmation.html template with reservation details.
    """
    #TODO
    # find  slot_id  form frontend.time_slots
    # show on the frontend
    return render_template("confirmation.html")


@app.route('/complete_reservation', methods=['POST'], endpoint="complete_reservation")
def accept_reservation():
    """
    Endpoint to accept a reservation and display the status.

    This endpoint handles a POST request with the reservation acceptance details.
    It retrieves the reservation information from the frontend, including the email and reservation details.
    The reservation acceptance is then processed by the 'accept_reservation' method, and the status is rendered in accept_reservation.html.

    Returns:
    - HTML template: Renders the accept_reservation.html template with the booking status.
    """
    


    email = request.form['email']
    """ TODO: 
    **Optional => check if email is right format 
    1.call booking_status = frontend.accept_reservation(email,json_string)
    2.feel free to change the way you get request_reserve values in frontend.accept_reservation
     ** but I need format 

    request_reserve = {"day": '2024-02-22',
            "srs_id": 13,
            "start_at": '15:00',
            "end_at": '15:59',
            "email": 'email@mail.com'}


    3.print out the return value
    4.show on the screen"""
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
