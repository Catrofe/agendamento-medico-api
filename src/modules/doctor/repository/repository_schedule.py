from sqlalchemy.sql.expression import select

from src.modules.base.repository import ContextRepository
from src.modules.doctor.entity.doctor_schedule import DoctorSchedule


class DoctorScheduleRepository:
    def __init__(self) -> None:
        self.__connection = ContextRepository.session_maker()

    async def create_schedule(self, schedule: DoctorSchedule) -> DoctorSchedule:
        async with self.__connection() as session:
            session.add(schedule)
            await session.commit()
            await session.refresh(schedule)
        return schedule

    async def verify_schedule(self, doctor_schedule: DoctorSchedule) -> bool:
        async with self.__connection() as session:
            query = await session.execute(
                select(DoctorSchedule)
                .where(DoctorSchedule.doctor_id == doctor_schedule.doctor_id)
                .where(DoctorSchedule.day_of_week == doctor_schedule.day_of_week)
                .where(
                    DoctorSchedule.start_time.between(
                        doctor_schedule.start_time,
                        doctor_schedule.end_time,
                    ),
                )
                .where(
                    DoctorSchedule.end_time.between(
                        doctor_schedule.start_time,
                        doctor_schedule.end_time,
                    ),
                ),
            )

        return bool(query.scalar())
