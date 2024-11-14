from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.cruds.task import task_crud
from app.models.task import Task
from app.schemas.task import CreateTaskRequest, UpdateTaskRequest, PartialUpdateTaskRequest, TaskResponse


class TaskCore:
    @staticmethod
    async def create(db: AsyncSession, task_request: CreateTaskRequest) -> Task:
        task = await task_crud.create(db=db, obj_in=task_request)
        return task

    @staticmethod
    async def update(db: AsyncSession, task_id: int, task_request: UpdateTaskRequest) -> Optional[TaskResponse]:
        task = await task_crud.get(db=db, id=task_id)
        if not task:
            return None
        task = await task_crud.update(db=db, db_obj=task, obj_in=task_request)
        return TaskResponse(**task.__dict__) if task else None

    @staticmethod
    async def delete(db: AsyncSession, task_id: int) -> Optional[TaskResponse]:
        task = await task_crud.remove(db=db, id=task_id)
        return TaskResponse(**task.__dict__) if task else None

    @staticmethod
    async def get_all(db: AsyncSession) -> List[TaskResponse]:
        tasks = await task_crud.get_multi(db=db)
        return [TaskResponse(**task.__dict__) for task in tasks]

    @staticmethod
    async def get_by_id(db: AsyncSession, task_id: int) -> Optional[TaskResponse]:
        task = await task_crud.get(db=db, id=task_id)
        return TaskResponse(**task.__dict__) if task else None

    @staticmethod
    async def partial_update(db: AsyncSession, task_id: int, task_request: PartialUpdateTaskRequest) -> Optional[TaskResponse]:
        task = await task_crud.get(db=db, id=task_id)
        if not task:
            return None
        task = await task_crud.update(db=db, db_obj=task, obj_in=task_request)
        return TaskResponse(**task.__dict__) if task else None
