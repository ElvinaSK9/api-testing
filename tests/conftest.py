from uuid import uuid4
import pytest
from api_client import BookingApiClient


@pytest.fixture(scope="session")
def api_client():
    # Create one reusable API client for the test session.
    client = BookingApiClient()
    yield client
    client.session.close()


@pytest.fixture(scope="session")
def auth_token(api_client):
    # Create one authentication token for protected requests.
    return api_client.create_token()


@pytest.fixture
def booking_data():
    # Return unique and valid booking test data
    unique_suffix = uuid4().hex[:8]

    return {
        "firstname": f"Elvina-{unique_suffix}",
        "lastname": "API-Test",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-07-10",
            "checkout": "2026-07-15",
        },
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def created_booking(api_client,auth_token,booking_data):
    # Create a booking before a test and remove it afterwards
    response = api_client.create_booking(booking_data)
    assert response.status_code == 200

    booking_id = response.json()["bookingid"]
    yield {"id": booking_id, "data": booking_data}

    current_booking = api_client.get_booking(booking_id)
    if current_booking.status_code == 200:
        api_client.delete_booking(booking_id, auth_token)
