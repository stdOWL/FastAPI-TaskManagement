from typing import Optional

from pydantic import BaseModel, EmailStr

class CreateTaskRequest(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False


class UpdateTaskRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None