from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    model_config: dict = SettingsConfigDict(
        env_file=".env", 
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
