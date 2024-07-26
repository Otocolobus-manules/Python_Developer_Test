import os
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()


class RepositorySettings(BaseModel):
    url: str = (f"postgresql+asyncpg://{os.getenv("DB_USER")}:"
                f"{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}")


class UserRepositoryConfig(BaseModel):
    repository_type: str = 'in_database'
    settings: RepositorySettings = RepositorySettings()


class EmailUserAutorization(BaseModel):
    address: str = os.getenv("EMAIL_ADDRESS")
    password: str = os.getenv("EMAIL_PASS")
    host_name: str = os.getenv("EMAIL_HOST")
    port: int = int(os.getenv("EMAIL_PORT"))


class InitProgramConfig(BaseModel):
    program_type: str = 'fastapi_app'


class Settings(BaseSettings):
    user_repository_config: UserRepositoryConfig = UserRepositoryConfig()
    user_email_config: EmailUserAutorization = EmailUserAutorization()
    init_program_config: InitProgramConfig = InitProgramConfig()


settings = Settings()
