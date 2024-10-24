from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.modules.base.entity_table import EntityTable


class Schedule(EntityTable):
    __tablename__ = "tb_schedule"

    doctor_id: Mapped[int] = Column(
        ForeignKey("tb_doctor.id"),
        nullable=False,
        primary_key=True,
    )
    patient_id: Mapped[int] = Column(
        ForeignKey("tb_patient.id"),
        nullable=False,
        primary_key=True,
    )
    appointment: Mapped[datetime] = mapped_column(nullable=False, primary_key=True)

    def __init__(self, doctor_id: int, patient_id: int, appointment: datetime) -> None:
        super().__init__()
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.appointment = appointment

    def update(self, **kwargs: dict) -> None:
        allowed_fields = {"doctor_id", "appointment"}
        for key, value in kwargs.items():
            if key in allowed_fields:
                setattr(self, key, value)
