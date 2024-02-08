from flask import (Flask, render_template)
import json
from backend.service import service
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
    service_items = service.get_all_services()
    return render_template("home.html", service_items=service_items)


@app.route('/staff/<service_code>', methods=['GET'])
def staff(service_code):
    services = service.get_all_services()
    selected_service = None
    for service_item in services:
        if service_code == service_item.get("service_id"):
            print(service_item)
            selected_service = service_item
            break

    staff_items = []
    for service_item in services:
        staff_list = service_item.get("staffs", [])
        staff_items.extend(staff_list)

    print(staff_items)
    return render_template("staff.html", staff_items=staff_items, selected_service=selected_service)


# -------- ERROR HANDLER  ------------
app.register_error_handler(404, utility.page_404)
app.register_error_handler(405, utility.page_405)
app.register_error_handler(401, utility.page_401)

# For testing in Pycharm IDE
# if __name__ == "__main__":
#  app.run(debug=True)
