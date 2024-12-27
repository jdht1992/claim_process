from fastapi import APIRouter, status
from sqlmodel import select

from src.models import ClaimProcess
from src.schemas import ClaimProcessCreateSchema, ClaimProcessSchema
from db import SessionDep

router = APIRouter()


"""
@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ClaimProcessSchema])
async def list_claim(session: SessionDep):
    return session.exec(select(ClaimProcess)).all()
"""

@router.get("/", status_code=status.HTTP_200_OK)
async def list_claim(session: SessionDep):
    return session.exec(select(ClaimProcess)).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
def get_user(claims_create: ClaimProcessCreateSchema, session: SessionDep):
    cliams = claims_create.model_dump().get("cliam")

    for claim in cliams:
        print(claim)
        claim = ClaimProcess.model_validate(claim)
        session.add(claim)
        session.commit()
        #session.refresh(claim)

        print(claim)

    return cliams
