from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def current_time() -> datetime:
    return datetime.now()


class EntityTable(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, sort_order=-1)
    created_at: Mapped[datetime] = mapped_column(default=current_time)
    updated_at: Mapped[datetime] = mapped_column(
        default=None, nullable=True, onupdate=current_time
    )
