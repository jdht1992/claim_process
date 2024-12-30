import json
from uuid import UUID

import redis
from fastapi import APIRouter, Depends, status
from fastapi_limiter.depends import RateLimiter
from sqlmodel import select

from db import SessionDep
from src.models import ProviderAverage

redis_client = redis.Redis(host='redis', port=6379, db=0)

router = APIRouter()

# Custom JSON encoder to handle UUIDs
class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)  # Convert UUID to string
        return super().default(obj)


@router.get("/", status_code=status.HTTP_200_OK, dependencies=[Depends(RateLimiter(times=10, seconds=60))])
def get_providers(session: SessionDep):
    cached_providers = redis_client.get("providers")

    if cached_providers:
        return json.loads(cached_providers)

    statement = select(ProviderAverage).order_by(ProviderAverage.average).limit(10)
    providers = session.exec(statement).all()
    

    providers = json.dumps([row.model_dump() for row in providers], cls=UUIDEncoder)

    redis_client.set(f"providers", 60, providers)

    return providers
