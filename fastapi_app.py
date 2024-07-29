import uvicorn
import asyncio
from fastapi import FastAPI

from utils.IoC import IoC
from routing.UserCrudRouter import UserCrudRouter
from exceptions.User.UserNotFoundExceptionHandler import user_not_found_exception_handler
from exceptions.User.UserNotFoundException import UserNotFoundException

from init_project import init_project


async def fastapi_app(container: IoC):
    """
        Создает и настраивает приложение FastAPI с маршрутизаторами и обработчиками исключений.

        :param container: IoC контейнер для управления зависимостями сервисов.
        """
    app = FastAPI()

    user_crud_router = UserCrudRouter(container=container).get_router()

    app.include_router(user_crud_router)
    app.add_exception_handler(UserNotFoundException, user_not_found_exception_handler)

    config = uvicorn.Config(
        app,
        reload=True,
        host="127.0.0.1",
        port=8000)
    server = uvicorn.Server(config=config)
    await server.serve()


if __name__ == '__main__':
    container = init_project()
    asyncio.run(fastapi_app(container=container))
