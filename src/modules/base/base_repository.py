from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.modules.base.context_repository import ContextRepository
from src.modules.base.entity_table import EntityTable


class BaseRepository:
    _instance = None
    __connection = ContextRepository.session_maker()

    def __new__(cls) -> "BaseRepository":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_connection(self) -> async_sessionmaker[AsyncSession]:
        return self.__connection

    async def save_entity(self, entity: EntityTable) -> EntityTable:
        async with self.__connection() as session:
            session.add(entity)
            await session.commit()
            await session.refresh(entity)

        return entity

    async def delete_entity(self, entity: EntityTable) -> None:
        async with self.__connection() as session:
            await session.delete(entity)
            await session.commit()
