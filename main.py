from fastapi import FastAPI, Request
from db import create_all_tables
from src.api.router import v1_router

app = FastAPI()

app.include_router(v1_router, prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    create_all_tables()
