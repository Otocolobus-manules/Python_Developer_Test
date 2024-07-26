from fastapi import APIRouter

from routing.IRouter import IRouter
from schemas.User import CreateUser, UpdateUser, DeleteUser, BaseUser
from utils.IoC import IoC


class UserCrudRouter(IRouter):
    def __init__(self, container: IoC):
        self.__container = container
        self.router = APIRouter(
            tags=['Users'],
            prefix='/user_crud',
        )
        self._register_routes()

    def _register_routes(self):
        @self.router.post('/create_user', response_model=BaseUser)
        async def create_user_api(user: CreateUser):
            result = await self.__container.resolve('Services.CreateUserService', user)
            return result

        @self.router.put('/update_user', response_model=BaseUser)
        async def update_user_api(user: UpdateUser):
            result = await self.__container.resolve('Services.UpdateUserService', user)
            return result

        @self.router.get('/get_user', response_model=BaseUser)
        async def get_user_api(user_id: int):
            result = await self.__container.resolve('Services.GetUserService', user_id)
            return result

        @self.router.delete('/delete_user', response_model=BaseUser)
        async def delete_user_api(user: DeleteUser):
            result = await self.__container.resolve('Services.DeleteUserService', user)
            return result

    def get_router(self) -> APIRouter:
        return self.router
