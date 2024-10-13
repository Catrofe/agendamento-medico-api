from collections.abc import Sequence
from datetime import datetime, time

from sqlalchemy import select

from src.modules.base.base_repository import BaseRepository
from src.modules.doctor.entity.doctor import Doctor
from src.modules.doctor.entity.doctor_schedule import DoctorSchedule
from src.modules.patient.entity.patient import Patient
from src.modules.schedule.entity.schedule import Schedule


class ScheduleRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    async def doctor_exists(self, doctor_id: int) -> bool:
        async with self._connection() as session:
            query = await session.execute(
                select(Doctor).where(Doctor.id == doctor_id),
            )
        return bool(query.scalars().first())

    async def get_default_schedule(self, doctor_id: int) -> Sequence[DoctorSchedule]:
        async with self._connection() as session:
            query = await session.execute(
                select(DoctorSchedule).where(
                    (DoctorSchedule.doctor_id == doctor_id),
                ),
            )
            return query.scalars().all()

    async def get_future_schedules(
        self,
        doctor_id: int,
        actual_date: datetime,
        limit_date: datetime,
    ) -> Sequence[Schedule]:
        async with self._connection() as session:
            query = await session.execute(
                select(Schedule).where(
                    Schedule.doctor_id == doctor_id,
                    Schedule.appointment >= actual_date,
                    Schedule.appointment <= limit_date,
                ),
            )
            return query.scalars().all()

    async def patient_exists(self, patient_id: int) -> bool:
        async with self._connection() as session:
            query = await session.execute(
                select(Patient).where(Patient.id == patient_id),
            )
        return bool(query.scalars().first())

    async def verify_schedule(self, doctor_id: int, appointment: datetime) -> bool:
        async with self._connection() as session:
            query = await session.execute(
                select(Schedule).where(
                    (Schedule.doctor_id == doctor_id)
                    & (Schedule.appointment == appointment),
                ),
            )
        return bool(query.scalars().first())

    async def verify_doctor_available(
        self,
        doctor_id: int,
        day_of_week: int,
        start_time: time,
    ) -> bool:
        async with self._connection() as session:
            query = await session.execute(
                select(DoctorSchedule)
                .where(DoctorSchedule.doctor_id == doctor_id)
                .where(DoctorSchedule.day_of_week == day_of_week)
                .where(
                    DoctorSchedule.start_time <= start_time,
                    DoctorSchedule.end_time > start_time,
                ),
            )
        return query.scalars().first() is not None
