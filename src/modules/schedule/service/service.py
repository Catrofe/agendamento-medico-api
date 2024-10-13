from datetime import datetime, time
from typing import TYPE_CHECKING

from src.exceptions.BadRequestException import BadRequestException
from src.main.settings import ZONE_INFO

if TYPE_CHECKING:
    from collections.abc import Sequence

    from src.modules.doctor.entity.doctor_schedule import DoctorSchedule
from src.modules.schedule.entity.schedule import Schedule
from src.modules.schedule.models.models import (
    DayScheduleDoctor,
    RegisterSchedule,
    ScheduleModel,
)
from src.modules.schedule.repository.repository import ScheduleRepository
from src.modules.schedule.usecases.get_day_schedule_doctor import GetDayScheduleDoctor


class ScheduleService:
    def __init__(self) -> None:
        self.__repository = ScheduleRepository()

    async def get_schedule_by_doctor(
        self,
        doctor_id: int,
        days: int = 30,
    ) -> list[DayScheduleDoctor]:
        if not await self.__repository.doctor_exists(doctor_id):
            raise BadRequestException("Doctor not found")

        default_schedule: Sequence[
            DoctorSchedule
        ] = await self.__repository.get_default_schedule(doctor_id)
        future_schedules: Sequence[
            Schedule
        ] = await self.__repository.get_future_schedules(doctor_id)
        return await GetDayScheduleDoctor(
            days,
            future_schedules,
        ).generates_availability(default_schedule)

    async def create_schedule(self, schedule_model: RegisterSchedule) -> ScheduleModel:
        appointment = datetime.combine(
            schedule_model.schedule_date,
            time(hour=schedule_model.start_time),
        )
        await self.validate_schedule(schedule_model, appointment)

        schedule = Schedule(
            doctor_id=schedule_model.doctor_id,
            patient_id=schedule_model.patient_id,
            appointment=appointment,
        )

        schedule = await self.__repository.save_entity(schedule)
        return ScheduleModel(**schedule.__dict__)

    async def validate_schedule(
        self,
        schedule_model: RegisterSchedule,
        appointment: datetime,
    ) -> None:
        if not await self.__repository.doctor_exists(schedule_model.doctor_id):
            raise BadRequestException("Doctor not found")
        if not await self.__repository.patient_exists(schedule_model.patient_id):
            raise BadRequestException("Patient not found")
        if appointment < datetime.now(tz=ZONE_INFO):
            raise BadRequestException("Invalid appointment date")
        if await self.__repository.verify_schedule(
            schedule_model.doctor_id,
            appointment,
        ):
            raise BadRequestException("Time already booked")
        if not await self.__repository.verify_doctor_available(
            schedule_model.doctor_id,
            appointment.weekday(),
            time(hour=schedule_model.start_time),
        ):
            raise BadRequestException("Doctor not available at this time")
