from fastapi import FastAPI
from db.database import settings
from db.session import engine
# from db.base import Base
from routes import router

app = FastAPI(title=settings.PROJECT_TITLE)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE)
    return app

app = start_application()

# Include Router
app.include_router(router)




