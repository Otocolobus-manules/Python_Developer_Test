from typing import Dict, Callable, Any, Union, overload, Literal, Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from repositories.IRepository import IRepository
from repositories.InDatabaseUserRepository import InDatabaseUserRepository
from repositories.InMemoryUserRepository import InMemoryUserRepository


class RepositoryFactory:
    """
    Фабрика для создания репозиториев пользователей.

    Этот класс позволяет создавать их экземпляры разных репозиториев с нужными параметрами.
    """

    def __init__(self):
        """
        Инициализация фабрики репозиториев.
        """
        self._repository_types: Dict[str, Type] = {
            'in_memory': InMemoryUserRepository,
            'in_database': InDatabaseUserRepository
        }

    @overload
    def create_repository(self, repo_type: Literal['in_memory']) -> InMemoryUserRepository:
        ...

    @overload
    def create_repository(self, repo_type: Literal['in_database'],
                          db_session: Union[AsyncSession, Session]) -> InDatabaseUserRepository:
        ...

    def create_repository(self, repo_type: str, *args: Any) -> IRepository:
        """
        Создает и возвращает репозиторий в зависимости от типа.

        :param repo_type: Тип репозитория
        :type repo_type: str
        :param args: Параметры для создания репозитория
        :return: Экземпляр репозитория
        :rtype: Union[InMemoryUserRepository, InDatabaseUserRepository]
        :raises ValueError: Если передан неизвестный тип репозитория или некорректные параметры
        """
        repo_class = self._repository_types.get(repo_type)
        if not repo_class:
            raise ValueError(f"Неизвестный тип репозитория: {repo_type}")

        try:
            return repo_class(*args)
        except TypeError as e:
            raise ValueError(f"Некорректные параметры для репозитория типа '{repo_type}': {e}")
