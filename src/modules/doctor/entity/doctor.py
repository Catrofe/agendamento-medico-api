from typing import Literal, Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.modules.base.entity_table import EntityTable


class Doctor(EntityTable):
    __tablename__ = "tb_doctor"

    name: Mapped[str] = mapped_column(
        __type_pos=String(155), nullable=False, unique=True
    )
    crm: Mapped[str] = mapped_column(__type_pos=String(10), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(
        __type_pos=String(155), nullable=False, unique=True
    )
    phone: Mapped[str] = mapped_column(
        __type_pos=String(15), nullable=False, unique=True
    )

    def __init__(self, name: str, crm: str, email: str, phone: str) -> None:
        super().__init__()
        self.name = name
        self.crm = crm
        self.email = email
        self.phone = phone

    def update(
        self, **kwargs: Optional[dict[Literal["name", "crm", "email", "phone"], str]]
    ) -> None:
        allowed_fields = {"name", "crm", "email", "phone"}
        for key, value in kwargs.items():
            if key in allowed_fields:
                setattr(self, key, value)
