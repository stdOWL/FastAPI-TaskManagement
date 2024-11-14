from fastapi import APIRouter, Depends, Path, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.task import TaskCore
from app.dependencies import get_async_db
from app.schemas import ResponseModel
from app.schemas.task import CreateTaskRequest, UpdateTaskRequest, PartialUpdateTaskRequest

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("", response_model=ResponseModel)
async def create(task_request: CreateTaskRequest, db: AsyncSession = Depends(get_async_db)):
    """
    Create a new task
    :param task_request: CreateTaskRequest model
    :param db: AsyncSession from get_async_db dependency
    :return: ResponseModel with the created task data
    """
    db_obj = await TaskCore.create(db, task_request)
    return ResponseModel(data=jsonable_encoder(db_obj))


@router.get("", response_model=ResponseModel)
async def get_all(db: AsyncSession = Depends(get_async_db)):
    """
    Get all tasks from the database with pagination
    :param db: AsyncSession from get_async_db dependency
    :return: ResponseModel with the list of tasks
    """
    db_obj = await TaskCore.get_all(db)
    return ResponseModel(data=db_obj)


@router.get("/{task_id}", response_model=ResponseModel)
async def get_by_id(task_id: int = Path(...), db: AsyncSession = Depends(get_async_db)):
    """
    Get a task by its ID
    :param task_id: ID of the task to retrieve
    :param db: AsyncSession from get_async_db dependency
    :return: ResponseModel with the task data if found, else raise a 404 HTTPException
    """
    db_obj = await TaskCore.get_by_id(db, task_id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return ResponseModel(data=jsonable_encoder(db_obj))


@router.put("/{task_id}", response_model=ResponseModel)
async def update(task_request: UpdateTaskRequest, task_id: int = Path(...), db: AsyncSession = Depends(get_async_db)):
    """
    Update a task by its ID
    :param task_request: UpdateTaskRequest model with the updated task data
    :param task_id: ID of the task to update
    :param db: AsyncSession from get_async_db dependency
    :return: ResponseModel with the updated task data if found, else raise a 404 HTTPException
    """
    db_obj = await TaskCore.update(db, task_id, task_request)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return ResponseModel(data=jsonable_encoder(db_obj))


@router.delete("/{task_id}", response_model=ResponseModel)
async def delete(task_id: int = Path(...), db: AsyncSession = Depends(get_async_db)):
    """
    Delete a task by its ID
    :param task_id: ID of the task to delete
    :param db: AsyncSession from get_async_db dependency
    :return: ResponseModel with the deleted task data if found, else raise a 404 HTTPException
    """
    db_obj = await TaskCore.delete(db, task_id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return ResponseModel(data=jsonable_encoder(db_obj))


@router.patch("/{task_id}", response_model=ResponseModel)
async def patch(task_request: PartialUpdateTaskRequest, task_id: int = Path(...),
                db: AsyncSession = Depends(get_async_db)):
    """
    Partially update a task by its ID
    :param task_request: PartialUpdateTaskRequest model with the updated task data
    :param task_id: ID of the task to partially update
    :param db: AsyncSession from get_async_db dependency
    :return: ResponseModel with the partially updated task data if found, else raise a 404 HTTPException
    """
    db_obj = await TaskCore.partial_update(db, task_id, task_request)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return ResponseModel(data=jsonable_encoder(db_obj))
