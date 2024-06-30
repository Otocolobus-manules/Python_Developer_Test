from core.config import settings
from core.repositories.repository_interface import UserRepositoryInterface
from crud.users_in_database import (
    create_user as db_create_user,
    update_user as db_update_user,
    get_user as db_get_user,
    delete_user as db_delete_user
)
from crud.users_in_memory import in_memory_repo
from core.models.db_helper import db_helper
from core.schemas import UserUpdate, UserDelete, UserCreate
from core.models import User
from core.exception.exceptions import RepositoryTypeNotFoundError


class DatabaseRepository(UserRepositoryInterface):  # Репозиторий для хранения в базе данных
    async def create_user(self, user: UserCreate) -> User:
        async with db_helper.session_getter() as session:
            return await db_create_user(session=session, user=user)

    async def update_user(self, user: UserUpdate) -> User:
        async with db_helper.session_getter() as session:
            return await db_update_user(session=session, user=user)

    async def get_user(self, user_id: int) -> User:
        async with db_helper.session_getter() as session:
            return await db_get_user(session=session, user_id=user_id)

    async def delete_user(self, user: UserDelete) -> User:
        async with db_helper.session_getter() as session:
            return await db_delete_user(session=session, user=user)


class InMemoryRepository(UserRepositoryInterface):   # Репозиторий для хранения в памяти
    async def create_user(self, user: UserCreate) -> User:
        return await in_memory_repo.create_user(user=user)

    async def update_user(self, user: UserUpdate) -> User:
        return await in_memory_repo.update_user(user=user)

    async def get_user(self, user_id: int) -> User:
        return await in_memory_repo.get_user(user_id=user_id)

    async def delete_user(self, user: UserDelete) -> User:
        return await in_memory_repo.delete_user(user=user)


def get_repository() -> UserRepositoryInterface:   # Функция возвращающая выбранный репозиторий
    if settings.repository_config.repository_type == 'in_database':
        return DatabaseRepository()
    elif settings.repository_config.repository_type == 'in_memory':
        return InMemoryRepository()
    else:
        raise RepositoryTypeNotFoundError(settings.repository_config.repository_type)
