from repositories.InDatabaseUserRepository import InDatabaseUserRepository
from factories.user_repository_factory.IFactory import IFactory
from sqlalchemy.ext.asyncio import AsyncSession


class InDatabaseUserRepositoryFactory(IFactory):
    @staticmethod
    def create_repository(db_session: AsyncSession) -> InDatabaseUserRepository:
        """
        Создает и возвращает репозиторий для управления пользователями в базе данных.

        :param db_session: Сессия базы данных
        :type db_session: AsyncSession
        :return: Экземпляр InDatabaseUserRepository
        :rtype: InDatabaseUserRepository
        """
        return InDatabaseUserRepository(db_session)
