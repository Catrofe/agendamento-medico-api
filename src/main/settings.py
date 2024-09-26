import logging

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str
    database_url: str
    logging_level: int = logging.INFO


settings = Settings()  # type:ignore
