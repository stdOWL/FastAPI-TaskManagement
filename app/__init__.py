from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.database import engine
from app.enums.exception import ExceptionStatus
from app.models import *
from app.models.base import Base
from app.routers import api_router
from app.schemas import ResponseModel, ResponseStatus

app = FastAPI(title="Task Management API",
              description="A FastAPI-based Task Management API for creating, updating, retrieving, and deleting "
                          "tasks. This API supports PostgreSQL for database management.",
              openapi_tags=[
                    {
                        "name": "Tasks",
                        "description": "Operations related to tasks"
                    }
                ])
app.include_router(router=api_router)

Base.metadata.create_all(engine)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error = exc.errors()[0]["msg"].replace("Value error, ", "") if exc.errors()[0].get("type",
                                                                                       None) == "value_error" else \
        exc.errors()[0].get("msg", None)
    return JSONResponse(ResponseModel(status=ResponseStatus.FAIL, message=error, error_code="VLDN-1000").model_dump(),
                        status_code=400)
