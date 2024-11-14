from sqlalchemy.ext.asyncio import AsyncSession

from app.cruds.task import task_crud
from app.models.task import Task
from app.schemas.task import CreateTaskRequest, UpdateTaskRequest


class TaskCore:
    @staticmethod
    async def create(db: AsyncSession, task_request: CreateTaskRequest) -> Task:
        task = task_crud.create(db=db, obj_in=task_request)
        return task

    @staticmethod
    async def update(db: AsyncSession, task_id: int, task_request: UpdateTaskRequest) -> Task:
        task = task_crud.update(db=db, db_obj_id=task_id, obj_in=task_request)
        return task

    @staticmethod
    async def delete(db: AsyncSession, task_id: int) -> Task:
        task = task_crud.remove(db=db, db_obj_id=task_id)
        return task

    @staticmethod
    async def get_all(db: AsyncSession):
        tasks = task_crud.get_multi(db=db)
        return tasks

    @staticmethod
    async def get_by_id(db: AsyncSession, task_id: int):
        task = task_crud.get(db=db, id=task_id)
        return task
