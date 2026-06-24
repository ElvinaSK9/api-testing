
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

    # Send a GET request
    response = api_client.get_booking(booking_id)

    # Check that the request was successful
    assert response.status_code == 200

    # Check that the API returned JSON
    assert response.headers["Content-Type"].startswith("application/json")

    # Convert the JSON response to a Python dictionary
    actual_data = response.json()

    # Check that the returned data is correct
    assert actual_data == expected_data