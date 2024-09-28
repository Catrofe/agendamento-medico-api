from sqlalchemy.sql.expression import select

from src.modules.base.base_repository import BaseRepository
from src.modules.doctor.entity.doctor import Doctor
from src.modules.doctor.models.models import CreateDoctor


class DoctorRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__()

    async def get_doctor_already_exists(self, doctor: CreateDoctor) -> bool:
        async with self._connection() as session:
            query = await session.execute(
                select(Doctor).where(
                    (Doctor.crm == doctor.crm)
                    | (Doctor.email == doctor.email)
                    | (Doctor.phone == doctor.phone),
                ),
            )
        return bool(query.first())

    async def get_doctor(self, doctor_id: int) -> Doctor | None:
        async with self._connection() as session:
            query = await session.execute(select(Doctor).where(Doctor.id == doctor_id))
        return query.scalar()
