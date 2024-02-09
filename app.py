from flask import (Flask, render_template)
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
    backend.service_items = backend.request_all_services()
    return render_template("home.html", service_items=backend.service_items)


@app.route('/staff/<service_code>', methods=['GET'])
def staff(service_code):
    backend.service_items = backend.request_all_services() 
    outcome = next((item for item in backend.service_items if item['service_code'] == service_code), None)
 
    return render_template("staff.html", staff_items=outcome["staff"], selected_service=outcome)


# -------- ERROR HANDLER  ------------
app.register_error_handler(404, utility.page_404)
app.register_error_handler(405, utility.page_405)
app.register_error_handler(401, utility.page_401)

# For testing in Pycharm IDE
# if __name__ == "__main__":
#  app.run(debug=True)
