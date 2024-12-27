from fastapi import APIRouter
from src.api.v1 import claim_process


v1_router = APIRouter()


v1_router.include_router(
    claim_process.router, prefix="/claim", tags=["claim"]
)
