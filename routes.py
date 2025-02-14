from fastapi import FastAPI, HTTPException, Depends,APIRouter
from sqlalchemy.orm import Session
from schema.schemas import ProfileCreateRequest
from db.database import SessionLocal, engine
from sqlalchemy import create_engine, Column, Integer, String
from model.models import StudentProfile
from pydantic import ValidationError

router = APIRouter()

# Dependency to get the SQLAlchemy session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Profile Creation endpoint to get the
@router.post("/create_profile/")
async def create_profile(profile: ProfileCreateRequest, db: Session = Depends(get_db)):
    # If the profile creation fails due to validation, it will raise an HTTPException with the error message.
    try:

        
        # Create the new profile
        new_profile = StudentProfile(
            name=profile.name,
            email=profile.email,
            phone=profile.phone,
            password=profile.password
        )
        db.add(new_profile)
        db.commit()
        db.refresh(new_profile)

        return {"message": "Profile created successfully.", "profile": new_profile}
    
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))

