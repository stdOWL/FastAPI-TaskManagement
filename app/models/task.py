import datetime

from sqlalchemy import String, Date
from sqlalchemy.orm import mapped_column, Mapped

from app.models.base import Base


class Task(Base):
    __tablename__ = "tasks"

    title: Mapped[str] = mapped_column(String(64), nullable=False)
    description: Mapped[str] = mapped_column(String(256), nullable=True)
    completed: Mapped[bool] = mapped_column(bool, default=False)





