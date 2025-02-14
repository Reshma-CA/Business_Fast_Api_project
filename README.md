
## Clone the Repository


 ```http
 https://github.com/Reshma-CA/Business_Fast_Api_project
```
## Activate Virtual Environment


 ```http
 venv\scripts\activate
```
## Install Dependencies


 ```http
 pip install -r requirements.txt
```

## Set Up PostgreSQL
1,Install PostgreSQL.

2, Create a new database, for example profile_db.

3, Update the database credentials in your .env file (if you're using one) or in the database.py file.

## API Reference

## Run the Application


 ```http
 uvicorn main:app --reload
```

## Open API Documentation
FastAPI automatically generates interactive API documentation at:

1, Swagger UI (for testing the API with UI)
2, ReDoc (for a detailed documentation view)

## API Endpoints

### 1. Create Profile

URL: /create_profile/
Method: POST


 ```http
URL: /create_profile/
Method: POST
```

## Request Body:
```http
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "1234567890",
  "password": "securepassword123"
}   
```
## Response:

### Success (200)

```http
{
    "message": "Profile created successfully.",
    "profile": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890"
    }
}
```
### Error (400):

```http
{
    "detail": "Validation error: Email is invalid"
}
```

## Testing
For unit testing or integration testing, you can use pytest or unittest. A simple test could look like:

### Example Test File (test_main.py):

```http
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_profile():
    response = client.post("/create_profile/", json={
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "password": "securepassword123"
    })
    assert response.status_code == 200
    assert "Profile created successfully." in response.json()["message"]

```

## Thank You


