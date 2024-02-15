from app import app
import pytest
from datetime import datetime, timedelta

@pytest.fixture
def client():
    # Create a test client for the Flask app
    with app.test_client() as client:
        yield client


def test_get_all_services(client):
    response = client.get("/backend/services")
    assert response.status_code == 200

def test_daily_reserve_time(client):
    staff_id = 3
    service_id = 2
    response = client.get(f"/backend/daily_reserve_time/{str(staff_id)}/{str(service_id)}")
    assert response.status_code == 200
    response_data = response.get_json()
    assert isinstance(response_data, list)

    # Calculate the current date and the date 7 days ago
    current_date = datetime.now().strftime("%Y-%m-%d")
    # 7 days  = 7-1  
    seven_days_ago = (datetime.now() + timedelta(days=6)).strftime("%Y-%m-%d")
    assert response_data[0]["day"] == current_date
    # Check the "day" tag in the response
    assert response_data[0]["day"] == current_date
    assert response_data[-1]["day"] == seven_days_ago

   