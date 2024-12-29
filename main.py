from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from db import create_all_tables
from src.api.router import v1_router


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    print("init lifespan")
    create_all_tables()
    yield
    print("clean up lifespan")

app = FastAPI(lifespan=app_lifespan)

app.include_router(v1_router, prefix="/api/v1")
