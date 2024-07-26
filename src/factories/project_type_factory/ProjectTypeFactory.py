from typing import overload, Literal, Any

from utils.IoC import IoC
from factories.project_type_factory.ConsoleAppFactory import ConsoleAppFactory
from factories.project_type_factory.FastapiAppFactory import FastApiAppFactory


class ProjectTypeFactory:
    """
    Фабрика для создания приложений различных типов (консольное приложение или FastAPI приложение).

    :ivar __project_types: Словарь, сопоставляющий строки с соответствующими классами фабрик приложений.
    """

    def __init__(self):
        """
        Инициализирует фабрику с доступными типами проектов.
        """
        self.__project_types = {
            'console_app': ConsoleAppFactory,
            'fastapi_app': FastApiAppFactory,
        }

    @overload
    def create_app(self, project_type: Literal['console_app'], container: IoC):
        """
        Создает консольное приложение.

        :param project_type: Тип проекта (должен быть 'console_app').
        :param container: IoC контейнер для управления зависимостями.
        """
        ...

    @overload
    def create_app(self, project_type: Literal['fastapi_app'], container: IoC):
        """
        Создает FastAPI приложение.

        :param project_type: Тип проекта (должен быть 'fastapi_app').
        :param container: IoC контейнер для управления зависимостями.
        """
        ...

    def create_app(self, project_type: str, *args: Any):
        """
        Создает приложение указанного типа.

        :param project_type: Тип проекта ('console_app' или 'fastapi_app').
        :param args: Дополнительные аргументы, передаваемые в конструктор фабрики.
        :return: Созданное приложение.
        :raises KeyError: Если указанный тип проекта не поддерживается.
        :raises ValueError: Если параметры, переданные в фабрику, некорректны.
        """
        app_factory_class = self.__project_types.get(project_type)
        if not app_factory_class:
            raise KeyError(f'Project type {project_type} not supported')

        try:
            return app_factory_class(*args).create_app()
        except TypeError as e:
            raise ValueError(f'Incorrect parameter for {project_type}: {e}')
