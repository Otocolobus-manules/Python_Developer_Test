from repositories.InDatabaseUserRepository import InDatabaseUserRepository
from factories.user_repository_factory.IFactory import IFactory
from sqlalchemy.ext.asyncio import AsyncSession


class InDatabaseUserRepositoryFactory(IFactory):
    def __init__(self, db_session: AsyncSession):
        self._db_session = db_session

    def create_repository(self) -> InDatabaseUserRepository:
        """
        Создает и возвращает репозиторий для управления пользователями в базе данных.

        :param db_session: Сессия базы данных
        :type db_session: AsyncSession
        :return: Экземпляр InDatabaseUserRepository
        :rtype: InDatabaseUserRepository
        """
        return InDatabaseUserRepository(self._db_session)
