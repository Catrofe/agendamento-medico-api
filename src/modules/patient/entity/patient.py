from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.modules.base.entity_table import EntityTable


class Patient(EntityTable):
    __tablename__ = "tb_patient"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, sort_order=-1)
    name: Mapped[str] = mapped_column(__type_pos=String(155), nullable=False)
    cpf: Mapped[str] = mapped_column(__type_pos=String(11), nullable=False, unique=True)
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

    def __init__(self, name: str, cpf: str, email: str, phone: str) -> None:
        super().__init__()
        self.name = name
        self.cpf = cpf
        self.email = email
        self.phone = phone

    def update(self, **kwargs: dict) -> None:
        allowed_fields = {"name", "cpf", "email", "phone"}
        for key, value in kwargs.items():
            if key in allowed_fields:
                setattr(self, key, value)
