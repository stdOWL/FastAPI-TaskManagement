from fastapi import APIRouter, Depends, Path, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.task import TaskCore
from app.dependencies import get_async_db
from app.schemas import ResponseModel
from app.schemas.task import CreateTaskRequest, UpdateTaskRequest

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("", response_model=ResponseModel)
async def create(task_request: CreateTaskRequest, db: AsyncSession = Depends(get_async_db)):
    db_obj = await TaskCore.create(db, task_request)
    return ResponseModel(data=jsonable_encoder(db_obj))


@router.get("/", response_model=ResponseModel)
async def get_all(db: AsyncSession = Depends(get_async_db)):
    db_obj = await TaskCore.get_all(db)
    return ResponseModel(data=jsonable_encoder(db_obj))


@router.get("/{task_id}", response_model=ResponseModel)
async def get_by_id(task_id: int = Path(...), db: AsyncSession = Depends(get_async_db)):
    db_obj = await TaskCore.get_by_id(db, task_id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return ResponseModel(data=jsonable_encoder(db_obj))


@router.put("/{task_id}", response_model=ResponseModel)
async def update(task_request: UpdateTaskRequest, task_id: int = Path(...), db: AsyncSession = Depends(get_async_db)):
    db_obj = await TaskCore.update(db, task_id, task_request)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return ResponseModel(data=jsonable_encoder(db_obj))
