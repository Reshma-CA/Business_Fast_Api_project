from fastapi.testclient import TestClient
from main import app  # Import FastAPI app instance
from pydantic import ValidationError

client = TestClient(app)

def test_create_profile_success():
    # Prepare valid input data for the test
    valid_payload = {
        "name": "Rahul",
        "email": "Rahul@gmail.com",
        "phone": "9234567890",  # Make sure the phone is numeric as per validation
        "password": "Rahulertg1@"  # Valid password that meets the criteria
    }
    
    # Send a POST request to the /create_profile endpoint
    response = client.post("/create_profile/", json=valid_payload)
    
    # Check if the response is successful (status code 200 or 201)
    assert response.status_code == 200
    
    # Check if the response contains the success message
    assert response.json() == {"message": "Profile created successfully.", "profile": response.json()['profile']}

def test_create_profile_validation_error():
    # Prepare invalid input data to test validation
    invalid_payload = {
        "name": "Rahul",
        "email": "Rahul@example",  # Invalid email format
        "phone": "123abc",  # Non-numeric phone
        "password": "short"  # Password does not meet the length requirement
    }
    
    # Send a POST request to the /create_profile endpoint with invalid data
    response = client.post("/create_profile/", json=invalid_payload)
    
    # Check if the response status code is 422 (Unprocessable Entity)
    assert response.status_code == 422  # Update to 422
    
    # Check if the response contains the appropriate error messages
    error_messages = response.json()['detail']
    assert "Phone must be numeric." in error_messages
    assert "Password must be at least 8 characters long." in error_messages
    assert "Invalid email address" in error_messages


def test_create_profile_missing_field():
    # Prepare payload with a missing required field (name)
    missing_name_payload = {
        "email": "missing.name@example.com",
        "phone": "9876543210",
        "password": "ValidPassword@123"
    }
    
    # Send a POST request to the /create_profile endpoint
    response = client.post("/create_profile/", json=missing_name_payload)
    
    # Check if the response status code is 422 (Unprocessable Entity)
    assert response.status_code == 422
    
    # Check if the response contains the appropriate error message
    error_messages = response.json()['detail']
    assert "Field required" in error_messages[0]['msg']  # Update the message to 'Field required'



