import os
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")


class RunConfig(BaseModel):
    host: str = '127.0.0.1'
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = '/api'


class ApiV1Prefix(BaseModel):
    prefix: str = '/v1'
    users: str = '/users'


class DatabaseConfig(BaseModel):
    url: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 20
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class RepositoryConfig(BaseModel):
    repository_type: str = 'in_database'


class Settings(BaseSettings):
    repository_config: RepositoryConfig = RepositoryConfig()
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    api_v1: ApiV1Prefix = ApiV1Prefix()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
