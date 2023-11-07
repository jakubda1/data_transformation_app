#!/usr/bin/sh
curl -X POST http://127.0.0.1:8080/api/v1/parse-me/ \
-H "Content-Type: application/json" \
-H "Authorization: YouShallNotPass!" \
-d '{"json_data": [
  {
    "country": "US",
    "city": "Boston",
    "currency": "USD",
    "amount": 100
  },
  {
    "country": "FR",
    "city": "Paris",
    "currency": "EUR",
    "amount": 20
  },
  {
    "country": "FR",
    "city": "Lyon",
    "currency": "EUR",
    "amount": 12.3
  },
  {
    "country": "ES",
    "city": "Madrid",
    "currency": "EUR",
    "amount": 9.1
  },
  {
    "country": "UK",
    "city": "London",
    "currency": "GBP",
    "amount": 22.33
  },
  {
    "country": "UK",
    "city": "London",
    "currency": "FBP",
    "amount": 11.99
  }
],
"args": ["country", "city"]
}
' > curl_output.json
