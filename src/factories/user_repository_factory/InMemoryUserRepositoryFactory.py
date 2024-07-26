from repositories.InMemoryUserRepository import InMemoryUserRepository
from factories.user_repository_factory.IFactory import IFactory


class InMemoryUserRepositoryFactory(IFactory):
    """
    Фабрика для создания репозитория пользователей, работающего в памяти.
    """

    def __init__(self, *args):
        """
        Инициализирует фабрику. Здесь параметры конструктора не используются.
        """
        ...

    def create_repository(self) -> InMemoryUserRepository:
        """
        Создает и возвращает репозиторий для управления пользователями в памяти.

        :return: Экземпляр InMemoryUserRepository.
        :rtype: InMemoryUserRepository.
        """
        return InMemoryUserRepository()
