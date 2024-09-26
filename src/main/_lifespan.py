from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.modules.base.repository import ContextRepository


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan events."""
    # Before startup
    await ContextRepository.create_all()

    yield

    # Before shutdown
    await ContextRepository.close_engine()
