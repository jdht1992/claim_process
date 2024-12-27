from fastapi import APIRouter
from src.api.v1 import claim_process
from src.api.v1 import claim


v1_router = APIRouter()
v1_router.include_router(
    claim_process.router, prefix="/claim_process", tags=["claim_process"]
)
v1_router.include_router(
    claim.router, prefix="/claim", tags=["claim"]
)
