from logging import INFO, basicConfig, getLogger
from typing import Annotated, Generator
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine

from config import get_settings

log = getLogger(__name__)
basicConfig(level=INFO)

settings = get_settings()

DB_URL = settings.DATABASE_URL

engine = create_engine(DB_URL)


def create_all_tables() -> None:
    """
    Creates the database and tables defined in the SQLModel metadata.
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """
    Generator for a database session to be used in routers.

    Return: Database session generator
    """
    log.info("Initialising database session...")
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
