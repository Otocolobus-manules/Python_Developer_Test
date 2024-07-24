from services.IService import IService
from repositories.IRepository import IRepository


class GetUserService(IService):
    """
    Сервис для получения информации о пользователе.

    Этот класс отвечает за выполнение логики получения данных пользователя по его идентификатору,
    используя переданный репозиторий.
    """

    def __init__(self, repository: IRepository):
        """
        Инициализация сервиса получения пользователя.

        :param repository: Репозиторий для выполнения операций с пользователем
        :type repository: IRepository
        """
        self.__repository = repository

    async def __call__(self, user_id: int):
        """
        Выполняет получение пользователя по его идентификатору.

        :param user_id: Идентификатор пользователя
        :type user_id: int
        :return: Объект пользователя, полученный из репозитория
        :rtype: UserModel
        :raises UserNotFoundException: Если пользователь не найден
        """
        return await self.__repository.get(user_id=user_id)
