import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# Load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "Profile Creation"

    # PostgreSQL Configuration
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER', 'localhost')
    POSTGRES_PORT: int = int(os.getenv('POSTGRES_PORT', 5433))  # Ensure it's int
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')

    # Database URL for SQLAlchemy
    DATABASE_URL: str = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

settings = Settings()
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)