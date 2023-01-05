# PALAEMON Logger Service

Used to test the PALAEMON ecosystem's various components' speed and responsiveness.

## Install

```bash
docker compose up -d --build
```

## Usage:

### Creating a Log event (without a Category):

```bash
curl --location --request POST 'http://localhost:8000/entry/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "contents": "Something has happened",
}'
```

The service will then attach a UTC Timestamp on the event.

### Creating a Log Event Category:

```bash
curl --location --request POST 'http://localhost:8000/category/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "TEST"
}'
```

### Creating a Log Event (with a Category):

(Notice that the category title is case in-sensitive.)

```bash
curl --location --request POST 'http://localhost:8000/entry/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "contents": "Something has happened",
    "category": "test"
}'
```

### Viewing Events:

```bash
curl --location --request GET 'http://localhost:8000/entry/'
```
Result:
```json
[
    {
        "id": 7,
        "timestamp": "2023-01-05T11:39:27.636648Z",
        "contents": "Something has happened",
        "category": "TEST"
    },
    {
        "id": 6,
        "timestamp": "2023-01-05T11:21:17.189700Z",
        "contents": "test",
        "category": "TEST"
    },
    {
        "id": 5,
        "timestamp": "2023-01-05T11:19:34.778844Z",
        "contents": "test",
        "category": "TEST"
    },
]
```

### Searching Events:

The Search term matches either the contents or the title of the attached category.

```bash
curl --location --request GET 'http://localhost:8000/entry/search/?q=Something has happened'
```