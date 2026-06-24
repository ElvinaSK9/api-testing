# Restful Booker API Testing Project

This is a small API testing project created for practice and as part of my QA portfolio.

The project includes manual API requests in Postman and automated tests written in Python with Pytest.

## What this project covers

* REST API testing
* GET, POST, PUT, PATCH and DELETE requests
* Authentication with a token
* Request headers, JSON bodies and URL parameters
* Creating, reading, updating and deleting bookings
* Checking status codes and response data
* Pytest fixtures
* Test data cleanup
* HTML test reports
* Running tests with GitHub Actions

## API

The project uses the public Restful Booker API:

`https://restful-booker.herokuapp.com`

This API is made for learning and testing. It is shared between many users, and its data can be reset from time to time.

The automated tests create their own bookings and delete them after the tests when possible.

## Automated tests

The project will contain five main API tests:

1. Create a new booking with POST.
2. Get a booking by ID with GET.
3. Update the full booking with PUT.(in progress)
4. Update part of the booking with PATCH.(in progress)
5. Delete the booking with DELETE and check that it is no longer available.(in progress)

More detailed test cases are available in:

[`docs/TEST_CASES.md`](docs/TEST_CASES.md)

## How to run the tests

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

macOS or Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the tests

```bash
pytest
```

### 5. Create an HTML report

```bash
mkdir -p reports
pytest --html=reports/report.html --self-contained-html
```

## How to run the Postman collection

1. Open Postman.
2. Import the collection and environment files from the `postman` folder.
3. Select the Restful Booker environment.
4. Open the collection.
5. Click **Run collection**.

The Postman collection saves the authentication token and booking ID into environment variables.

## Configuration

The main settings are stored in `config.py`.

Example:

```python
BASE_URL = "https://restful-booker.herokuapp.com"
USERNAME = "admin"
PASSWORD = "password123"
REQUEST_TIMEOUT = 20
```

These credentials are public and are provided by the training API.

Real passwords, tokens and other private data should not be stored in GitHub.

## Important note

Restful Booker is a public test API. 
Sometimes a test can fail because the service is unavailable, the database was reset or another user changed the same data.

To reduce this problem the tests create their own booking data and remove it after the test.
