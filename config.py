import os

BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
USERNAME = os.getenv("API_USERNAME", "admin")
PASSWORD = os.getenv("API_PASSWORD", "password123")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "20"))
