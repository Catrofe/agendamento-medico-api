from src.exceptions.BadRequestException import BadRequestException
from src.modules.doctor.entity.doctor import Doctor
from src.modules.doctor.models.models import CreateDoctor, DoctorModel
from src.modules.doctor.repository.repository import DoctorRepository


class DoctorService:

    def __init__(self) -> None:
        self.__repository = DoctorRepository()

    async def create_doctor(self, doctor: CreateDoctor) -> DoctorModel:
        if await self.__repository.get_doctor_already_exists(doctor):
            raise BadRequestException("Doctor already exists.")
        new_doctor = await self.__repository.create_doctor(
            Doctor(**doctor.model_dump())
        )
        return DoctorModel(**new_doctor.__dict__)
