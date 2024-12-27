from datetime import datetime
import uuid
from pydantic import field_validator
from sqlmodel import SQLModel


class ClaimBase(SQLModel):
    name: str

class ClaimSchema(ClaimBase):
    uid: uuid.UUID

class ClaimCreateSchema(ClaimBase):
    pass


class ClaimProcessBase(SQLModel):
    service_date: datetime
    submitted_procedure: str
    quadrant: str | None = None
    plan: str
    subscriber: int
    provider_npi: int
    provider_fees: float
    allowed_fees: float
    member_coinsurance: float
    member_copay: float
    claim_uid: uuid.UUID
    net_fee: float


class ClaimProcess(ClaimProcessBase):

    @field_validator('service_date', mode='before') 
    def validate_service_date(cls, value): 
        if isinstance(value, str): 
            try: # Try parsing the date string 
                return datetime.strptime(value, "%m/%d/%y %H:%M") 
            except ValueError: 
                raise ValueError('service_date must be in the format MM/DD/YY HH:MM') 
        return value
    
    @field_validator('submitted_procedure', mode='before') 
    def validate_submitted_procedure(cls, value: str): 
        if not value.startswith('D'): 
            raise ValueError('submitted_procedure must begin with the letter D') 
        return value
    
    @field_validator('provider_npi', mode='before') 
    def validate_provider_npi(cls, value): 
        str_value = str(value) 
        if len(str_value) != 10: 
            raise ValueError('provider_npi must be exactly 10 digits long') 
        return value
    
class ClaimProcessSchema(ClaimProcessBase):
    uid: uuid.UUID
    # claim_uid: ClaimSchema

class ClaimProcessCreateSchema(SQLModel):
    cliam: list[ClaimProcess]
