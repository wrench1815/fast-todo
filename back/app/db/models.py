from sqlalchemy import Boolean, Column, Integer, String, DateTime
import datetime

from .database import Base


class Todo(Base):
    __tablename__ = 'todo'

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    task = Column(String)
    is_completed = Column(
        Boolean,
        default=False,
    )
    date_added = Column(
        DateTime,
        default=datetime.datetime.utcnow,
    )
