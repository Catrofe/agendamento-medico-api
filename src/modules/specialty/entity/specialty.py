from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from src.modules.base.entity_table import EntityTable


class Specialty(EntityTable):
    __tablename__ = "tb_specialty"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, sort_order=-1)
    name: Mapped[str] = mapped_column(
        __type_pos=String(155),
        nullable=False,
    )
    description: Mapped[str] = mapped_column(
        __type_pos=String(155),
        nullable=False,
    )
    is_visible: Mapped[bool] = mapped_column(
        __type_pos=Boolean,
        nullable=False,
        default=False,
    )

    def __init__(self, name: str, description: str) -> None:
        super().__init__()
        self.name = name
        self.description = description

    def set_name(self, name: str) -> None:
        self.name = name

    def set_is_visible(self) -> None:
        self.is_visible = not self.is_visible
