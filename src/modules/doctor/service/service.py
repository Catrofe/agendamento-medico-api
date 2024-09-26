from src.exceptions.BadRequestException import BadRequestException
from src.exceptions.NotFoundException import NotFoundException
from src.modules.doctor.entity.doctor import Doctor
from src.modules.doctor.models.models import CreateDoctor, DoctorModel, UpdateDoctor
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

    async def get_doctor_model(self, doctor_id: int) -> DoctorModel:
        doctor = await self.__repository.get_doctor(doctor_id)
        if not doctor:
            raise NotFoundException("Doctor not found.")
        return DoctorModel(**doctor.__dict__)

    async def get_doctor(self, doctor_id: int) -> Doctor:
        doctor = await self.__repository.get_doctor(doctor_id)
        if not doctor:
            raise NotFoundException("Doctor not found.")
        return doctor

    async def update_doctor(self, doctor_update: UpdateDoctor) -> DoctorModel:
        doctor = await self.get_doctor(doctor_update.id)
        doctor.update(**doctor_update.model_dump(exclude_defaults=True))
        doctor = await self.__repository.update_doctor(doctor)
        return DoctorModel(**doctor.__dict__)

    async def delete_doctor(self, doctor_id: int) -> None:
        await self.get_doctor(doctor_id)
        await self.__repository.delete_doctor(doctor_id)
        return None
