from typing import List

from fastapi import APIRouter, status

from db import SessionDep
from src.api.v1.calculator import Calculator
from src.models import Claim, ClaimItem
from src.schemas import ClaimItemSchema

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Claim)
def create_claim(claim_items: List[ClaimItemSchema], session: SessionDep):
    calculator = Calculator(session=session)

    claim = Claim()
    session.add(claim)
    session.commit()
    print(f"Created claim with id {claim.id}")

    for item in claim_items:        
        item.claim_uid = claim.id
        item = ClaimItem.model_validate(item)
        session.add(item)
        session.commit()

    # TODO This call needs to be move to a background process for avoid block the request.
    calculator.calculate_net_fee(claim=claim)
    
    session.refresh(claim)
    return claim
