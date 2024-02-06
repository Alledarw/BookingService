from flask import (Flask, render_template)
import json

from backend.backend import Backend
from frontend.http_request import http_request
import frontend.utility as utility

app = Flask(__name__)

backend = Backend()


# #################### BACKEND ##########################
@app.route("/backend/services", methods=["GET"])
def all_service():
    services = backend.request_all_services()
    print(services)
    return services


# #################### FRONTEND ##########################
@app.route('/', methods=['GET'], endpoint="home")
def home():
    service_items = http_request.request_all_services()
    print(service_items)
    return render_template("home.html", service_items=service_items)


@app.route('/staff', methods=['GET'], endpoint="staff")
def staff():
    staff_items = [
        {"staff_code": "S001", "staff_name": "John Doe", "image": "john.jpg"},
        {"staff_code": "S002", "staff_name": "Alice Smith", "image": "alice.jpg"},
        {"staff_code": "S003", "staff_name": "Bob Johnson", "image": "bob.jpg"}
    ]

    print(staff_items)
    return render_template("staff.html", staff_items=staff_items)


# -------- ERROR HANDLER  ------------
app.register_error_handler(404, utility.page_404)
app.register_error_handler(405, utility.page_405)
app.register_error_handler(401, utility.page_401)

# For testing in Pycharm IDE
#if __name__ == "__main__":
#    app.run(debug=True)
