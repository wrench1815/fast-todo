from pydantic import BaseModel
from datetime import datetime


class TodoBase(BaseModel):
    task: str


class TaskUpdate(BaseModel):
    is_completed: bool

    class Config:
        orm_mode = True


class TaskCreate(TodoBase):

    class Config:
        orm_mode = True


class TaskFull(TodoBase):
    id: int
    is_completed: bool
    date_added: datetime

    class Config:
        orm_mode = True
