import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # POSTGRESQL
    SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL", "sqlite:///./app.db")


configuration = Settings()
