from sqlalchemy import select

from src.modules.base.repository import ContextRepository
from src.modules.patient.entity.patient import Patient


class PatientRepository:
    def __init__(self) -> None:
        self.__connection = ContextRepository.session_maker()

    async def patient_exists(self, cpf: str, email: str, phone: str) -> bool:
        async with self.__connection() as session:
            query = await session.execute(
                select(Patient).where(
                    (Patient.cpf == cpf)
                    | (Patient.email == email)
                    | (Patient.phone == phone),
                ),
            )
        return bool(query.scalar())

    async def save_patient(self, patient: Patient) -> Patient:
        async with self.__connection() as session:
            session.add(patient)
            await session.commit()
            await session.refresh(patient)

        return patient

    async def get_patient_by_id(self, patient_id: int) -> Patient:
        async with self.__connection() as session:
            query = await session.execute(
                select(Patient).where(Patient.id == patient_id),
            )
        return query.scalars().first()

    async def delete_patient(self, patient: Patient) -> None:
        async with self.__connection() as session:
            await session.delete(patient)
            await session.commit()
