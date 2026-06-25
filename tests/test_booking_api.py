
def test_create_booking(api_client, auth_token, booking_data):
    # Send a POST request to create a booking
    response = api_client.create_booking(booking_data)

    # Check that the request was successful
    assert response.status_code == 200

    # Convert the JSON response to a Python dictionary
    response_data = response.json()
    print(response_data)

    # Get the booking ID and booking data from the response
    booking_id = response_data["bookingid"]
    created_booking = response_data["booking"]

    # Check that the booking ID is a number
    assert isinstance(booking_id, int)

    # Check that the API returned the same booking data
    assert created_booking == booking_data

    # Delete the booking after the test
    api_client.delete_booking(booking_id, auth_token)


def test_get_booking(api_client, created_booking):
    # Get the ID and expected data from the fixture
    booking_id = created_booking["id"]
    expected_data = created_booking["data"]

    response = api_client.get_booking(booking_id)

    assert response.status_code == 200

    # Check that the API returned JSON
    assert response.headers["Content-Type"].startswith("application/json")

    actual_data = response.json()

    # Check that the returned data is correct
    assert actual_data == expected_data

def test_update_booking(api_client, auth_token, created_booking):
    # Get the booking ID from the fixture
    booking_id = created_booking["id"]

    updated_date = {
        "firstname": "Elvina_test",
        "lastname": "API-Test -update",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-07-11",
            "checkout": "2026-07-16",
        },
        "additionalneeds": "Breakfast and Lunch",
    }
    response = api_client.update_booking(booking_id, updated_date, auth_token)
    assert response.status_code == 200
    assert response.json() == updated_date

def test_partial_update_booking(api_client, auth_token, created_booking):
    booking_id = created_booking["id"]
    original_data = created_booking["data"]
    updated_partial_date = {
        "firstname": "Update my name test",
        "lastname": "It was updated",
    }

    response = api_client.partial_update_booking(booking_id, updated_partial_date,auth_token)
    assert response.status_code == 200

    # PATCH returns the complete booking, not only changed fields
    actual_data = response.json()
    assert actual_data["firstname"] == updated_partial_date["firstname"]
    assert actual_data["lastname"] == updated_partial_date["lastname"]

    # Check that another field was not changed
    assert actual_data["bookingdates"] == original_data["bookingdates"]


def test_delete_booking(api_client, auth_token, created_booking):
    # Get the booking ID from the fixture
    booking_id = created_booking["id"]

    deleted= api_client.delete_booking(booking_id, auth_token)

    assert deleted.status_code == 201

    get_deleted =api_client.get_booking(booking_id)

    assert get_deleted.status_code == 404