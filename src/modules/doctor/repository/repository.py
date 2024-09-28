from sqlalchemy.sql.expression import delete, select

from src.modules.base.context_repository import ContextRepository
from src.modules.doctor.entity.doctor import Doctor
from src.modules.doctor.models.models import CreateDoctor


class DoctorRepository:
    def __init__(self) -> None:
        self.__connection = ContextRepository.session_maker()

    async def get_doctor_already_exists(self, doctor: CreateDoctor) -> bool:
        async with self.__connection() as session:
            query = await session.execute(
                select(Doctor).where(
                    (Doctor.crm == doctor.crm)
                    | (Doctor.email == doctor.email)
                    | (Doctor.phone == doctor.phone),
                ),
            )
        return bool(query.first())

    async def create_doctor(self, doctor: Doctor) -> Doctor:
        async with self.__connection() as session:
            session.add(doctor)
            await session.commit()
            await session.refresh(doctor)
        return doctor

    async def get_doctor(self, doctor_id: int) -> Doctor | None:
        async with self.__connection() as session:
            query = await session.execute(select(Doctor).where(Doctor.id == doctor_id))
        return query.scalar()

    async def update_doctor(self, doctor: Doctor) -> Doctor:
        async with self.__connection() as session:
            session.add(doctor)
            await session.commit()
            await session.refresh(doctor)
        return doctor

    async def delete_doctor(self, doctor_id: int) -> None:
        async with self.__connection() as session:
            await session.execute(delete(Doctor).where(Doctor.id == doctor_id))
            await session.commit()
