 
import pytest
import json

from backend.connection import connection as db
from backend.service import service_db as Service
from backend.appoitment import appoitment_db as Appointment
from backend.backend import Backend

 

def test_filter_service():
    # Arrange
    backend = Backend()
    backend.service_items = backend.request_all_services()
     
    text_search = "Men" 
    content = backend.fillter_service(text_search)
    assert content != None
    assert "service_name" in content[0]
