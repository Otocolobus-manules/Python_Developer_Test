from app.console_app import console_app
from factories.project_type_factory.IAppFactory import IAppFactory
from utils.IoC import IoC


class ConsoleAppFactory(IAppFactory):
    """
    Фабрика для создания консольного приложения.

    :param container: IoC контейнер для управления зависимостями сервисов.
    """

    def __init__(self, container: IoC):
        """
        Инициализирует фабрику с предоставленным IoC контейнером.

        :param container: IoC контейнер для управления зависимостями сервисов.
        """
        self.__container = container

    def create_app(self):
        """
        Создает и возвращает консольное приложение.

        :return: Функция console_app с переданным контейнером зависимостей.
        """
        return console_app(container=self.__container)
