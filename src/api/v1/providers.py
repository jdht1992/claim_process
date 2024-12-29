from typing import List
from fastapi import APIRouter, status
from sqlmodel import select
from src.models import ProviderAverage
from db import SessionDep

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ProviderAverage])
def get_providers(session: SessionDep):
    statement = select(ProviderAverage).order_by(ProviderAverage.average).limit(10)
    providers = session.exec(statement).all()
    return providers
