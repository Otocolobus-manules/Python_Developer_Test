from repositories.InMemoryUserRepository import InMemoryUserRepository
from factories.user_repository_factory.IFactory import IFactory


class InMemoryUserRepositoryFactory(IFactory):
    def __init__(self, *args):
        ...

    def create_repository(self) -> InMemoryUserRepository:
        """
        Создает и возвращает репозиторий для управления пользователями в памяти.

        :return: Экземпляр InMemoryUserRepository
        :rtype: InMemoryUserRepository
        """
        return InMemoryUserRepository()
