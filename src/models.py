import uuid
from datetime import datetime

from sqlalchemy import BigInteger, Column
from sqlmodel import Field, Relationship, SQLModel


class Claim(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    claims_process: list["ClaimItem"] = Relationship(back_populates="claim")


class ClaimItemBase(SQLModel):
    service_date: datetime
    submitted_procedure: str
    quadrant: str | None = None
    # quadrant: str | None = Field(default=None)
    plan: str
    subscriber: int = Field(sa_column=Column(BigInteger))
    provider_npi: int = Field(sa_column=Column(BigInteger))
    provider_fees: float
    allowed_fees: float
    member_coinsurance: float
    member_copay: float
    net_fee: float | None = None


class ClaimItem(ClaimItemBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    claim_uid: uuid.UUID = Field(foreign_key="claim.id")
    claim: Claim = Relationship(back_populates="claims_process")


class ProviderAverage(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    provider_npi: int = Field(sa_column=Column(BigInteger, unique=True))
    items: int = 0
    total: float = 0
    average: float = 0
