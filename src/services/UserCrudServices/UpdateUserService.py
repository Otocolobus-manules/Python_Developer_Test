from schemas.User import UpdateUser
from repositories.IRepository import IRepository
from services.IService import IService


class UpdateUserService(IService):
    """
    Сервис для обновления информации о пользователе.

    Этот класс отвечает за выполнение логики обновления данных пользователя,
    используя переданный репозиторий.
    """

    def __init__(self, repository: IRepository):
        """
        Инициализация сервиса обновления пользователя.

        :param repository: Репозиторий для выполнения операций с пользователем
        :type repository: IRepository
        """
        self.__repository = repository

    async def __call__(self, user: UpdateUser):
        """
        Выполняет обновление пользователя.

        :param user: Данные для обновления пользователя
        :type user: UpdateUser
        :return: Обновленный объект пользователя, полученный из репозитория
        :rtype: UserModel
        :raises UserNotFoundException: Если пользователь не найден
        """
        return await self.__repository.update(user)
