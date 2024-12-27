from fastapi import APIRouter, status
from sqlmodel import select

from src.models import Claim, ClaimItem
from src.schemas import ClaimItemSchema
from db import SessionDep

router = APIRouter()


# @router.get("/", status_code=status.HTTP_200_OK, response_model=list[ClaimProcess])
# async def list_claim(session: SessionDep):
#     return session.exec(select(ClaimProcess)).all()


@router.post("/", status_code=status.HTTP_201_CREATED)
def get_user(claim_items: list[ClaimItemSchema], session: SessionDep):

    claim = Claim()
    session.add(claim)
    session.commit()
    print(f"Created claim with id {claim.id}")

    for item in claim_items:
        item.claim_uid = claim.id
        item = ClaimItem.model_validate(item)
        session.add(item)
        session.commit()
    return {}
