# HTTP Methods Covered

| Method | Purpose in this project | Endpoint example |
|---|---|---|
| GET | Read booking data | `/booking/{bookingId}` |
| POST | Create a token or booking | `/auth`, `/booking` |
| PUT | Replace all booking fields | `/booking/{bookingId}` |
| PATCH | Change selected booking fields | `/booking/{bookingId}` |
| DELETE | Remove a booking | `/booking/{bookingId}` |

## Other HTTP methods

`HEAD` requests return headers without a response body, while `OPTIONS` requests describe communication options supported by a resource. They are not part of the automated checks because Restful Booker documents and demonstrates the five CRUD-related methods above.
