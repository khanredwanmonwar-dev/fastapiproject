from fastapi import FastAPI
import user
from database import engine, base
import user_controller

base.metadata.create_all(bind=engine)
app=FastAPI(title="Test Project")
app.include_router(user_controller.router)