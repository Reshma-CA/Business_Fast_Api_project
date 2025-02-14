from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from db.database import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database url is", SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SESSIONLOCAL = sessionmaker(autoflush=False,autocommit=False,bind=engine)