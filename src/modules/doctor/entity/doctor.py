from zoneinfo import ZoneInfo

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Column
from src.modules.base.entity_table import EntityTable
from datetime import datetime


class Doctor(EntityTable):
    __tablename__ = "tb_doctor"

    name: Mapped[str] = Column(String(155), nullable=False)
    crm: Mapped[str] = Column(String(10), nullable=False)
    email: Mapped[str] = Column(String(155), nullable=False)
    phone: Mapped[str] = Column(String(20), nullable=False)

    def __init__(self, name: str, crm: str, email: str, phone: str) -> None:
        super().__init__()
        self.name = name
        self.crm = crm
        self.email = email
        self.phone = phone

