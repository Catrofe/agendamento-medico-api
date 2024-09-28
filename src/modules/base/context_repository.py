from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from src.main.settings import settings
from src.modules.base.entity_table import EntityTable


class ContextRepository:
    _engine: AsyncEngine | None = None

    @staticmethod
    def get_engine() -> AsyncEngine:
        """Get the engine."""
        if ContextRepository._engine is None:
            return ContextRepository.create_engine()
        return ContextRepository._engine

    @staticmethod
    async def close_engine() -> None:
        """Close the engine."""
        if ContextRepository._engine is not None:
            await ContextRepository._engine.dispose()
            ContextRepository._engine = None

    @staticmethod
    def create_engine() -> AsyncEngine:
        """Create the engine."""
        if ContextRepository._engine is not None:
            err_msg = (
                "AsyncEngine is already set. "
                "Use `BaseRepository.get_engine()` to get the engine."
            )
            raise ValueError(err_msg)

        ContextRepository._engine = create_async_engine(settings.database_url)
        return ContextRepository._engine

    @staticmethod
    async def create_all() -> None:
        """Create all tables."""
        engine = ContextRepository.get_engine()

        async with engine.begin() as async_conn:
            await async_conn.run_sync(EntityTable.metadata.create_all)

    @staticmethod
    def session_maker() -> async_sessionmaker[AsyncSession]:
        """Get the session maker."""
        return async_sessionmaker(
            ContextRepository.get_engine(),
            expire_on_commit=False,
        )
