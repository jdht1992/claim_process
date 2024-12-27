from datetime import datetime
import uuid
from sqlalchemy import BigInteger, Column
from sqlmodel import Field, Relationship, SQLModel


class Claim(SQLModel, table=True):
    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    claims_process: list["ClaimProcess"] = Relationship(back_populates="claim")


class ClaimProcess(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    service_date: datetime
    submitted_procedure: str
    quadrant: str | None
    plan: str
    subscriber: int = Field(sa_column=Column(BigInteger))
    provider_npi: int = Field(sa_column=Column(BigInteger))
    provider_fees: float
    allowed_fees: float
    member_coinsurance: float
    member_copay: float
    claim: uuid.UUID
    net_fee: float
    claim_uid: uuid.UUID | None = Field(default=None, foreign_key="claim.uid")
    claim: Claim | None = Relationship(back_populates="claims_process")
