from sqlalchemy import Column, ForeignKey, Time
from sqlalchemy.orm import Mapped, mapped_column

from src.modules.base.entity_table import EntityTable


class DoctorSchedule(EntityTable):
    __tablename__ = "tb_doctor_schedule"

    doctor_id: Mapped[int] = Column(
        ForeignKey("tb_doctor.id"), nullable=False
    )  # type:ignore
    day_of_week: Mapped[int] = mapped_column(nullable=False)
    start_time: Mapped[Time] = mapped_column(__type_pos=Time, nullable=False)
    end_time: Mapped[Time] = mapped_column(__type_pos=Time, nullable=False)

    def __init__(self, name: str, crm: str, email: str, phone: str) -> None:
        super().__init__()  # type:ignore
        self.name = name
        self.crm = crm
        self.email = email
        self.phone = phone
