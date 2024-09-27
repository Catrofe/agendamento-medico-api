from datetime import time

from sqlalchemy import (
    Column,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.exceptions.BadRequestException import BadRequestException
from src.modules.base.entity_table import EntityTable


class DoctorSchedule(EntityTable):
    __tablename__ = "tb_doctor_schedule"

    doctor_id: Mapped[int] = Column(
        ForeignKey("tb_doctor.id"),
        nullable=False,
    )
    day_of_week: Mapped[int] = mapped_column(nullable=False)
    start_time: Mapped[time] = mapped_column(nullable=False)
    end_time: Mapped[time] = mapped_column(nullable=False)

    def __init__(
        self,
        doctor_id: int,
        day_of_week: int,
        start_time: int,
        end_time: int,
    ) -> None:
        super().__init__()
        self.doctor_id = doctor_id
        self.day_of_week = day_of_week
        self.start_time = self.create_fix_hour(start_time)
        self.end_time = self.create_fix_hour(end_time)

    @staticmethod
    def create_fix_hour(hour: int) -> time:
        if not (0 <= hour <= 23):  # noqa: PLR2004
            raise BadRequestException("Invalid hour")
        return time(hour=hour, minute=0, second=0)
