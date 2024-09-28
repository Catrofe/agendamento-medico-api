from sqlalchemy import select

from src.modules.base.base_repository import BaseRepository
from src.modules.patient.entity.patient import Patient


class PatientRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    async def patient_exists(self, cpf: str, email: str, phone: str) -> bool:
        async with self._connection() as session:
            query = await session.execute(
                select(Patient).where(
                    (Patient.cpf == cpf)
                    | (Patient.email == email)
                    | (Patient.phone == phone),
                ),
            )
        return bool(query.scalar())

    async def get_patient_by_id(self, patient_id: int) -> Patient:
        async with self._connection() as session:
            query = await session.execute(
                select(Patient).where(Patient.id == patient_id),
            )
        return query.scalars().first()
