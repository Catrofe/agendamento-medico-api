import logging

from src.exceptions.BadRequestException import BadRequestException
from src.modules.doctor.entity.doctor_schedule import DoctorSchedule
from src.modules.doctor.models.models_schedule import ScheduleCreate
from src.modules.doctor.repository.repository_schedule import DoctorScheduleRepository


class DoctorScheduleService:
    def __init__(self) -> None:
        self.__repository = DoctorScheduleRepository()

    async def create_schedule(self, schedule_model: ScheduleCreate) -> ScheduleCreate:
        """
        verificar se doutor já existe, verificar se schedule já existe.
        """
        schedule = DoctorSchedule(**schedule_model.model_dump())
        schedule_valid = await self.__repository.verify_schedule(schedule)
        if schedule_valid:
            logging.error("Schedule already exists")
            raise BadRequestException("Schedule already exists")
        schedule = await self.__repository.create_schedule(schedule)
        return ScheduleCreate(**schedule.__dict__)

    async def get_schedule_by_id(self, schedule_id: int) -> ScheduleCreate:
        schedule = await self.__repository.get_schedule_by_id(schedule_id)
        return ScheduleCreate(**schedule.__dict__)

    async def get_schedule_by_doctor_id(self, doctor_id: int) -> list[ScheduleCreate]:
        schedule = await self.__repository.get_schedule_by_doctor_id(doctor_id)
        return [ScheduleCreate(**s.__dict__) for s in schedule]

    async def delete_schedule_by_id(self, schedule_id: int) -> None:
        schedule = await self.__repository.get_schedule_by_id(schedule_id)
        if not schedule:
            logging.error("Schedule not found")
            raise BadRequestException("Schedule not found")
        await self.__repository.delete_schedule(schedule)
