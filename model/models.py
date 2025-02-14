from sqlalchemy import Column, Integer, String
from db.base_class import Base  # Import the Base class from base_class.py

class StudentProfile(Base):
    __tablename__ = 'student_profiles'  

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
    password = Column(String)

