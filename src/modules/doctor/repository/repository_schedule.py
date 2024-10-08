from collections.abc import Sequence

from sqlalchemy.sql.expression import select

from src.modules.base.base_repository import BaseRepository
from src.modules.doctor.entity.doctor_schedule import DoctorSchedule


class DoctorScheduleRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    async def verify_schedule(self, doctor_schedule: DoctorSchedule) -> bool:
        async with self._connection() as session:
            query = await session.execute(
                select(DoctorSchedule)
                .where(DoctorSchedule.doctor_id == doctor_schedule.doctor_id)
                .where(DoctorSchedule.day_of_week == doctor_schedule.day_of_week)
                .where(
                    (DoctorSchedule.start_time < doctor_schedule.end_time)
                    & (DoctorSchedule.end_time > doctor_schedule.start_time),
                ),
            )
        existing_schedules = query.scalars().all()
        return bool(existing_schedules)

    async def get_schedule_by_id(self, schedule_id: int) -> DoctorSchedule:
        async with self._connection() as session:
            query = await session.execute(
                select(DoctorSchedule).where(DoctorSchedule.id == schedule_id),
            )
        return query.scalar()

    async def get_schedule_by_doctor_id(
        self,
        doctor_id: int,
    ) -> Sequence[DoctorSchedule]:
        async with self._connection() as session:
            query = await session.execute(
                select(DoctorSchedule).where(DoctorSchedule.doctor_id == doctor_id),
            )
        return query.scalars().all()
