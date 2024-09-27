from datetime import datetime
from typing import TypedDict

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.modules.base.entity_table import EntityTable, current_time


class DoctorUpdateParams(TypedDict, total=False):
    name: str
    crm: str
    email: str
    phone: str


class Doctor(EntityTable):
    __tablename__ = "tb_doctor"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, sort_order=-1)
    name: Mapped[str] = mapped_column(
        __type_pos=String(155),
        nullable=False,
    )
    crm: Mapped[str] = mapped_column(__type_pos=String(10), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(
        __type_pos=String(155),
        nullable=False,
        unique=True,
    )
    phone: Mapped[str] = mapped_column(
        __type_pos=String(15),
        nullable=False,
        unique=True,
    )
    created_at: Mapped[datetime] = mapped_column(default=current_time)
    updated_at: Mapped[datetime] = mapped_column(
        default=None,
        nullable=True,
        onupdate=current_time,
    )

    def __init__(self, name: str, crm: str, email: str, phone: str) -> None:
        super().__init__()
        self.name = name
        self.crm = crm
        self.email = email
        self.phone = phone

    def update(self, **kwargs: DoctorUpdateParams) -> None:
        allowed_fields = {"name", "crm", "email", "phone"}
        for key, value in kwargs.items():
            if key in allowed_fields:
                setattr(self, key, value)
