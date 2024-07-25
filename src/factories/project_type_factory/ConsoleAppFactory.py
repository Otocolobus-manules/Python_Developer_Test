from app.console_app import console_app
from factories.project_type_factory.IAppFactory import IAppFactory
from utils.IoC import IoC


class ConsoleAppFactory(IAppFactory):
    def __init__(self, container: IoC):
        self.__container = container

    def create_app(self):
        return console_app(container=self.__container)
