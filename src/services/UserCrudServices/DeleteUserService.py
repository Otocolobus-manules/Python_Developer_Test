from schemas.User import DeleteUser
from repositories.IRepository import IRepository
from services.IService import IService


class DeleteUserService(IService):
    """
    Сервис для удаления пользователя.

    Этот класс отвечает за выполнение логики удаления пользователя,
    используя переданный репозиторий.
    """

    def __init__(self, repository: IRepository):
        """
        Инициализация сервиса удаления пользователя.

        :param repository: Репозиторий для выполнения операций с пользователем
        :type repository: IRepository
        """
        self.__repository = repository

    async def __call__(self, user: DeleteUser):
        """
        Выполняет удаление пользователя.

        :param user: Данные для удаления пользователя
        :type user: DeleteUser
        :return: Удаленный объект пользователя, полученный из репозитория
        :rtype: UserModel
        :raises UserNotFoundException: Если пользователь не найден
        """
        return await self.__repository.delete(user=user)
