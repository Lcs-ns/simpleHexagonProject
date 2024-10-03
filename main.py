from fastapi import FastAPI
from app.application.http import signupController
from app.infrastructure.db.session import engine
from app.infrastructure.db.models import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(signupController.router)