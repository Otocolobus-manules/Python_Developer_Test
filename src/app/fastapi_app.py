import uvicorn
from fastapi import FastAPI

from utils.IoC import IoC
from routing.UserCrudRouter import UserCrudRouter
from exceptions.User.UserNotFoundExceptionHandler import user_not_found_exception_handler
from exceptions.User.UserNotFoundException import UserNotFoundException


async def fastapi_app(container: IoC):
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
