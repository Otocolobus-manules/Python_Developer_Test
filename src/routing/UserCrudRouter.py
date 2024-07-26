from fastapi import APIRouter

from routing.IRouter import IRouter
from schemas.User import CreateUser, UpdateUser, DeleteUser, BaseUser
from utils.IoC import IoC


class UserCrudRouter(IRouter):
    """
    Маршрутизатор для CRUD операций с пользователями.

    Этот класс регистрирует маршруты для создания, обновления, получения и удаления пользователей.
    """

    def __init__(self, container: IoC):
        """
        Инициализирует маршрутизатор с предоставленным IoC контейнером.

        :param container: IoC контейнер для управления зависимостями сервисов.
        """
        self.__container = container
        self.router = APIRouter(
            tags=['Users'],
            prefix='/user_crud',
        )
        self._register_routes()

    def _register_routes(self):
        """
        Регистрирует маршруты для CRUD операций с пользователями.
        """
        @self.router.post('/create_user', response_model=BaseUser)
        async def create_user_api(user: CreateUser):
            """
            Создает нового пользователя.

            :param user: Данные для создания пользователя.
            :return: Созданный пользователь.
            """
            result = await self.__container.resolve('Services.CreateUserService', user)
            return result

        @self.router.put('/update_user', response_model=BaseUser)
        async def update_user_api(user: UpdateUser):
            """
            Обновляет данные существующего пользователя.

            :param user: Данные для обновления пользователя.
            :return: Обновленный пользователь.
            """
            result = await self.__container.resolve('Services.UpdateUserService', user)
            return result

        @self.router.get('/get_user', response_model=BaseUser)
        async def get_user_api(user_id: int):
            """
            Получает данные пользователя по его ID.

            :param user_id: ID пользователя.
            :return: Данные пользователя.
            """
            result = await self.__container.resolve('Services.GetUserService', user_id)
            return result

        @self.router.delete('/delete_user', response_model=BaseUser)
        async def delete_user_api(user: DeleteUser):
            """
            Удаляет пользователя.

            :param user: Данные для удаления пользователя.
            :return: Удаленный пользователь.
            """
            result = await self.__container.resolve('Services.DeleteUserService', user)
            return result

    def get_router(self) -> APIRouter:
        """
        Возвращает экземпляр APIRouter с зарегистрированными маршрутами.

        :return: Экземпляр APIRouter.
        """
        return self.router
