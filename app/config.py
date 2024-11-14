import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # POSTGRESQL
    SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL",
                                             "postgresql+psycopg://postgres:postgres@localhost:5445/taskmanager")


configuration = Settings()
