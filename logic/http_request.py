import requests
from flask import jsonify, request
 
class http_request:
    def request_all_services():
        request_url = request.url_root + "/backend/services"
        response = requests.get(request_url)
        if response.status_code == 200:  # Check for a successful HTTP status code
            return response.json()
        else:
            return {'services': []}
