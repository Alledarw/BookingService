from app import app
import pytest

@pytest.fixture
def client():
    # Create a test client for the Flask app
    with app.test_client() as client:
        yield client


def test_get_all_services(client):
    response = client.get('/backend/services')
    assert response.status_code == 200