# API Test Cases

## TC-API-001 — Create a booking

**Method:** POST  
**Endpoint:** `/booking`

**Preconditions:** The API is available.

**Steps:**
1. Send a POST request with all required booking fields.
2. Read the response status and JSON body.
3. Validate the returned booking against the JSON Schema.

**Expected result:**
- Status code is `200`.
- The response contains an integer `bookingid`.
- The returned booking data matches the request body.
- The response satisfies the booking JSON Schema.

---

## TC-API-002 — Get an existing booking

**Method:** GET  
**Endpoint:** `/booking/{bookingId}`

**Preconditions:** A booking has been created and its ID is known.

**Steps:**
1. Send a GET request using the created booking ID.
2. Check the response status and `Content-Type` header.
3. Compare the response body with the original booking data.
4. Validate the response against the JSON Schema.

**Expected result:**
- Status code is `200`.
- The response is JSON.
- The returned data matches the created booking.
- The response satisfies the booking JSON Schema.

---

## TC-API-003 — Fully update a booking

**Method:** PUT  
**Endpoint:** `/booking/{bookingId}`

**Preconditions:** A booking exists and a valid authentication token is available.

**Steps:**
1. Send a PUT request with a complete new booking body and the auth token.
2. Check the update response.
3. Send a GET request for the same booking.

**Expected result:**
- PUT status code is `200`.
- The PUT response contains all new values.
- A later GET request returns the same updated data.

---

## TC-API-004 — Partially update a booking

**Method:** PATCH  
**Endpoint:** `/booking/{bookingId}`

**Preconditions:** A booking exists and a valid authentication token is available.

**Steps:**
1. Send a PATCH request containing only `firstname` and `totalprice`.
2. Compare the response with the original booking.

**Expected result:**
- Status code is `200`.
- The selected fields contain the new values.
- All fields not included in the PATCH request remain unchanged.

---

## TC-API-005 — Delete a booking

**Method:** DELETE  
**Endpoint:** `/booking/{bookingId}`

**Preconditions:** A booking exists and a valid authentication token is available.

**Steps:**
1. Send an authenticated DELETE request.
2. Send a GET request for the deleted booking ID.

**Expected result:**
- DELETE status code is `201` according to this API contract.
- The following GET request returns `404`.
