from typing import Dict

from repositories.IRepository import IRepository
from models.UserModel import UserModel
from schemas.User import CreateUser, UpdateUser, DeleteUser
from exceptions.User.UserNotFoundException import UserNotFoundException


class InMemoryUserRepository(IRepository):
    """
    Репозиторий для управления пользователями в памяти.

    Этот класс реализует интерфейс IRepository для управления пользователями в памяти.
    """
    def __init__(self) -> None:
        """
        Инициализация репозитория.
        """
        self.__users: Dict[int, UserModel] = {}
        self.__current_id = 1

    async def create(self, user: CreateUser) -> UserModel:
        """
        Создает нового пользователя в памяти.

        :param user: Данные для создания пользователя
        :type user: CreateUser
        :return: Созданный пользователь
        :rtype: UserModel
        """
        new_user = UserModel(id=self.__current_id, name=user.name)
        self.__users[self.__current_id] = new_user
        self.__current_id += 1
        return new_user

    async def update(self, user: UpdateUser) -> UserModel:
        """
        Обновляет данные пользователя в памяти.

        :param user: Данные для обновления пользователя
        :type user: UpdateUser
        :return: Обновленный пользователь
        :rtype: UserModel
        :raises UserNotFoundException: Если пользователь не найден
        """
        if user.id not in self.__users:
            raise UserNotFoundException(user.id)
        updated_user = self.__users[user.id]
        updated_user.name = user.name
        return updated_user

    async def get(self, user_id: int) -> UserModel:
        """
        Получает пользователя по идентификатору из памяти.

        :param user_id: Идентификатор пользователя
        :type user_id: int
        :return: Пользователь с указанным идентификатором
        :rtype: UserModel
        :raises UserNotFoundException: Если пользователь не найден
        """
        if user_id not in self.__users:
            raise UserNotFoundException(user_id)
        return self.__users[user_id]

    async def delete(self, user: DeleteUser) -> UserModel:
        """
        Удаляет пользователя из памяти.

        :param user: Данные для удаления пользователя
        :type user: DeleteUser
        :return: Удаленный пользователь
        :rtype: UserModel
        :raises UserNotFoundException: Если пользователь не найден
        """
        if user.id not in self.__users:
            raise UserNotFoundException(user.id)
        deleted_user = self.__users.pop(user.id)
        return deleted_user
