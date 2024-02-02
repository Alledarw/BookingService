from flask import (Flask,render_template)

import logic.utility as utility

app = Flask(__name__)


# #################### BACKEND ##########################
@app.route("/backend/services", methods=["GET"])
def all_task():
    return "all_task"



# #################### FRONTEND ##########################
@app.route('/', methods=['GET'], endpoint="home")
def home():
    return render_template("home.html")


# -------- ERROR HANDLER  ------------
app.register_error_handler(404, utility.page_404)
app.register_error_handler(405, utility.page_405)
app.register_error_handler(401, utility.page_401)
