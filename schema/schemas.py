from pydantic import BaseModel, EmailStr, field_validator, model_validator
from typing import Optional
import re

class ProfileCreateRequest(BaseModel):
    name: str
    email: EmailStr  # Pydantic will automatically validate the email format
    phone: Optional[str] = None
    password: str

    # Validate phone to ensure it's numeric
    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v):
        if v and not v.isnumeric():
            raise ValueError("Phone must be numeric.")
        return v

    # Validate password with custom rules
    @model_validator(mode='before')
    def validate_password(cls, values):
        password = values.get("password")
        if password:
            if len(password) < 8:
                raise ValueError("Password must be at least 8 characters long.")
            if not re.search(r'[A-Z]', password):
                raise ValueError("Password must contain at least one uppercase letter.")
            if not re.search(r'[a-z]', password):
                raise ValueError("Password must contain at least one lowercase letter.")
            if not re.search(r'[0-9]', password):
                raise ValueError("Password must contain at least one numeric digit.")
            if not re.search(r'[@#$%^&+=]', password):
                raise ValueError("Password must include at least one special character (@, #, $, %, etc.).")
        return values
