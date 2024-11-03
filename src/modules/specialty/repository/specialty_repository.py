from collections.abc import Sequence

from sqlalchemy.sql.expression import select

from src.modules.base.base_repository import BaseRepository
from src.modules.specialty.entity.specialty import Specialty


class SpecialtyRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    async def verify_if_specialty_exists(self, name: str) -> bool:
        async with self._connection() as session:
            query = await session.execute(
                select(Specialty).where(Specialty.name == name),
            )
        query = query.scalar()
        return bool(query)

    async def get_entity_by_id(self, specialty_id: int) -> Specialty | None:
        async with self._connection() as session:
            query = await session.execute(
                select(Specialty).where(Specialty.id == specialty_id),
            )
        return query.scalar_one_or_none()

    async def get_all_entities(self) -> Sequence[Specialty]:
        async with self._connection() as session:
            query = await session.execute(select(Specialty))
        return query.scalars().all()

    async def update_visibility_specialty_with_lock(
        self,
        specialty_id: int,
    ) -> Specialty | None:
        async with self._connection() as session:
            query = await session.execute(
                select(Specialty).where(Specialty.id == specialty_id).with_for_update(),
            )
            specialty = query.scalar_one_or_none()

            if not specialty:
                return None

            specialty.change_visibility()
            session.add(specialty)
            await session.commit()
            await session.refresh(specialty)
        return specialty
