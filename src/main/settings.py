import logging

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str
    database_url: str
    logging_level: int = logging.INFO
    timezone: str = "America/Sao_Paulo"


settings = Settings()
