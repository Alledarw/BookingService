from flask import request,render_template

 
def is_access_from_postman():
    user_agent = request.headers.get('User-Agent') 
    substring = "Postman"
    return substring in user_agent 

def get_error_tag(status, msg):
    return {"status": status,
            "msg": msg}

def page_404(e):
    if is_access_from_postman():
        return "404: Page Not Found"
    else:
        return render_template("errors/404.html")

def page_405(e):
    if is_access_from_postman():
        return "405: Method Not Allowed"
    else:
        return render_template("errors/405.html")

def page_401(e):
    if is_access_from_postman():
        return "401: Unauthorized Error"
    else:
        return render_template("errors/401.html")