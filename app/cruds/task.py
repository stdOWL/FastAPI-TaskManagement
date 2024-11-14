from app.cruds.base import CRUDBase
from app.models.task import Task
from app.schemas.task import UpdateTaskRequest, CreateTaskRequest


class TaskCrud(CRUDBase[Task, CreateTaskRequest, UpdateTaskRequest]):
    pass


task_crud = TaskCrud(model=Task)
