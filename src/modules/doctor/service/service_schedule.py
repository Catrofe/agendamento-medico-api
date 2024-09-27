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
