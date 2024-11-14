from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class CreateTaskRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Task title")
    description: Optional[str] = Field(None, min_length=1, max_length=255, description="Task description")
    completed: Optional[bool] = Field(False, description="Whether the task is completed or not")


class UpdateTaskRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Task title")
    description: Optional[str] = Field(None, min_length=1, max_length=255, description="Task description")
    completed: bool = Field(False, description="Whether the task is completed or not")


class PartialUpdateTaskRequest(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255, description="Task title")
    description: Optional[str] = Field(None, min_length=1, max_length=255, description="Task description")
    completed: Optional[bool] = Field(None, description="Whether the task is completed or not")


class TaskResponse(BaseModel):
    id: int = Field(..., description="Task ID")
    title: str = Field(..., description="Task title")
    description: Optional[str] = Field(None, description="Task description")
    completed: bool = Field(False, description="Whether the task is completed or not")
