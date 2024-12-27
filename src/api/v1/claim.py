from fastapi import APIRouter, status
from sqlmodel import select

from src.models import Claim
from src.schemas import ClaimCreateSchema, ClaimSchema
from db import SessionDep


router = APIRouter()

@router.get("/", response_model=list[Claim])
async def list_customer(session: SessionDep):
    return session.exec(select(Claim)).all()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClaimSchema)
async def create_customer(claim_data: ClaimCreateSchema, session: SessionDep):
    customer = Claim.model_validate(claim_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer
