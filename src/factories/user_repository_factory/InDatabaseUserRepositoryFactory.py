from repositories.InDatabaseUserRepository import InDatabaseUserRepository
from factories.user_repository_factory.IFactory import IFactory
from sqlalchemy.ext.asyncio import AsyncSession
from utils.DatabaseHelper import DatabaseHelper
from config import settings


class InDatabaseUserRepositoryFactory(IFactory):
    """
    Фабрика для создания репозитория пользователей, работающего с базой данных.

    :param db_session: Асинхронная сессия базы данных.
    """

    def __init__(self):
        """
        Инициализирует фабрику с предоставленной сессией базы данных.

        :param db_session: Асинхронная сессия базы данных.
        :type db_session: AsyncSession
        """
        self._db_session = DatabaseHelper(
            url=settings.user_repository_config.settings.url,
        ).session_getter()

    def create_repository(self) -> InDatabaseUserRepository:
        """
        Создает и возвращает репозиторий для управления пользователями в базе данных.

        :return: Экземпляр InDatabaseUserRepository.
        :rtype: InDatabaseUserRepository
        """
        return InDatabaseUserRepository(self._db_session)
