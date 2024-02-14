from flask import (Flask, render_template, request, redirect, url_for)
from backend.backend import Backend
from frontend.http_request import http_request
import frontend.utility as utility

app = Flask(__name__)

backend = Backend()


# #################### BACKEND ##########################
@app.route("/backend/services", methods=["GET"])
def all_service():
    services = backend.request_all_services()
    return services


# #################### FRONTEND ##########################
@app.route('/', methods=['GET'], endpoint="home")
def home(): 
    backend.reset_selected_value()

    backend.service_items = backend.request_all_services()
    if not (request.args.get('text_search') == None):
        text_search = request.args.get('text_search')
        show_service_items = backend.fillter_service(text_search)
    else:
        show_service_items = backend.request_all_services()

    return render_template("home.html", service_items=show_service_items)


@app.route('/staff/<service_code>', methods=['GET'], endpoint="staff")
def staff(service_code):
    backend.service_items = backend.request_all_services()
    backend.selected_service = next(
        (item for item in backend.service_items if item['service_code'] == service_code), None)

    return render_template("staff.html", 
                           staff_items=backend.selected_service["staff"], 
                           selected_service=backend.selected_service)

@app.route('/reserve_time/<staff_code>', methods=['GET'], endpoint="reserve_time")
def reserve_time(staff_code):
    if backend.selected_service == None:
        redirect(url_for('home')) 
   
    backend.selected_staff = next(
        (item for item in backend.selected_service["staff"] if item['staff_code'] == staff_code), None)
    
    if backend.selected_staff == None:
        redirect(url_for('home'))

    if backend.selected_staff == None:
        service_code = backend.selected_service["service_code"]
        redirect(url_for('staff', service_code=service_code))
    
    return render_template("reserve_time.html", 
                           selected_service=backend.selected_service, 
                           selected_staff=backend.selected_staff)
    



    





# -------- ERROR HANDLER  ------------
app.register_error_handler(404, utility.page_404)
app.register_error_handler(405, utility.page_405)
app.register_error_handler(401, utility.page_401)

# For testing in Pycharm IDE
# if __name__ == "__main__":
#  app.run(debug=True)
if __name__ == "__main__":
    app.run(port=8000)
