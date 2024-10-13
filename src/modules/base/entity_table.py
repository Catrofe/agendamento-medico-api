from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import DateTime

from src.main.settings import ZONE_INFO


def current_time() -> datetime:
    return datetime.now(tz=ZONE_INFO)


class EntityTable(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        __type_pos=DateTime(timezone=True),
        default=current_time,
    )
    updated_at: Mapped[datetime] = mapped_column(
        __type_pos=DateTime(timezone=True),
        default=None,
        nullable=True,
        onupdate=current_time,
    )
