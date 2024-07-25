from app.fastapi_app import fastapi_app
from factories.project_type_factory.IAppFactory import IAppFactory
from utils.IoC import IoC


class FastApiAppFactory(IAppFactory):
    def __init__(self, container: IoC):
        self.__container = container

    def create_app(self):
        return fastapi_app(container=self.__container)
