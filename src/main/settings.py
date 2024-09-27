import logging
from zoneinfo import ZoneInfo

from pydantic_settings import BaseSettings

ZONE_INFO = ZoneInfo("America/Sao_Paulo")


class Settings(BaseSettings):
    env: str
    database_url: str
    logging_level: int = logging.INFO


settings = Settings()
