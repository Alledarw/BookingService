from flask import (Flask,render_template)

from logic.service import service
from logic.http_request import http_request
import logic.utility as utility
 

app = Flask(__name__)


# #################### BACKEND ##########################
@app.route("/backend/services", methods=["GET"])
def all_task():
    return service.get_all_services()


# #################### FRONTEND ##########################
@app.route('/', methods=['GET'], endpoint="home")
def home():
    filter_items = http_request.request_all_services()
    print(filter_items)
    return render_template("home.html")


# -------- ERROR HANDLER  ------------
app.register_error_handler(404, utility.page_404)
app.register_error_handler(405, utility.page_405)
app.register_error_handler(401, utility.page_401)
