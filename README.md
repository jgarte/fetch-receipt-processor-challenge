# Fetch Receipt Processor Challenge

https://github.com/fetch-rewards/receipt-processor-challenge

# Docker

## Building

```sh
docker build -t fetch-receipts .
```

## Running

```sh
docker run -d --name fetch-container -p 8080:8080 fetch-receipts
```

A [justfile](https://just.systems/) is provided for the convenience of running the above commands.

# Submitting a receipt

Submit a receipt as follows:

```sh
curl -X POST http://0.0.0.0:8080/receipts/process -H "Content-Type: application/json" -d '{
    "retailer": "Walgreens",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "08:13",
    "total": "2.65",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
        {"shortDescription": "Dasani", "price": "1.40"}
    ]
}'
```

# Viewing points of a submitted receipt

Given that the id of your receipt is 7fb1377b-b223-49d9-a31a-5a02701dd310,
you can view that receipt's points as follows:

```sh
curl -X GET http://0.0.0.0:8080/receipts/7fb1377b-b223-49d9-a31a-5a02701dd310/points
```

# API docs

API docs can be found at the following endpoint:

http://0.0.0.0:8080/docs
