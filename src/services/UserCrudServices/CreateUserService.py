from schemas.User import CreateUser
from services.IService import IService
from repositories.IRepository import IRepository


class CreateUserService(IService):
    """
    Сервис для создания нового пользователя.

    Этот класс отвечает за выполнение логики создания нового пользователя, используя переданный репозиторий.
    """

    def __init__(self, repository: IRepository) -> None:
        """
        Инициализация сервиса создания пользователя.

        :param repository: Репозиторий для выполнения операций с пользователем
        :type repository: IRepository
        """
        self.__repository = repository

    async def __call__(self, user: CreateUser):
        """
        Выполняет создание пользователя.

        :param user: Данные для создания пользователя
        :type user: CreateUser
        """
        return await self.__repository.create(user)
