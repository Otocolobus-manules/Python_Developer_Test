from app.fastapi_app import fastapi_app
from factories.project_type_factory.IAppFactory import IAppFactory
from utils.IoC import IoC


class FastApiAppFactory(IAppFactory):
    """
    Фабрика для создания FastAPI приложения.

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
        Создает и возвращает FastAPI приложение.

        :return: Функция fastapi_app с переданным контейнером зависимостей.
        """
        return fastapi_app(container=self.__container)
