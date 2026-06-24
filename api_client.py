import requests

from config import BASE_URL, PASSWORD, REQUEST_TIMEOUT, USERNAME


class BookingApiClient:
    def __init__(self):
        self.session = requests.Session()

    def create_token(self):
        # Send a request to get an authentication token
        response = requests.post(
            BASE_URL + "/auth",
            json={
                "username": USERNAME,
                "password": PASSWORD,
            },
            timeout=REQUEST_TIMEOUT,
        )

        # Convert the response to a dictionary and return the token
        response_data = response.json()
        return response_data["token"]

    def create_booking(self, booking_data):
        # Send a POST request to create a booking
        response = self.session.post(
            BASE_URL + "/booking",
            json=booking_data,
            timeout=REQUEST_TIMEOUT,
        )

        return response

    def get_booking(self, booking_id):
        # Send a GET request to get a booking by ID
        response = self.session.get(
            BASE_URL + "/booking/" + str(booking_id),
            timeout=REQUEST_TIMEOUT,
        )

        return response

    def delete_booking(self, booking_id, token):
        headers = {
            "Cookie": f"token={token}",
            "Content-Type": "application/json",
        }

        response = self.session.delete(
            BASE_URL + f"/booking/{booking_id}",
            headers=headers,
            timeout=REQUEST_TIMEOUT,
        )

        return response