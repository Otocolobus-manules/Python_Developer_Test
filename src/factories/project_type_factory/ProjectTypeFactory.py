from typing import overload, Literal, Any

from utils.IoC import IoC
from factories.project_type_factory.ConsoleAppFactory import ConsoleAppFactory
from factories.project_type_factory.FastapiAppFactory import FastApiAppFactory


class ProjectTypeFactory:
    def __init__(self):
        self.__project_types = {
            'console_app': ConsoleAppFactory,
            'fastapi_app': FastApiAppFactory,
        }

    @overload
    def create_app(self, project_type: Literal['console_app'], container: IoC):
        ...

    def create_app(self, project_type: str, *args: Any):
        app = self.__project_types.get(project_type)
        if not app:
            raise KeyError(f'Project type {project_type} not supported')

        try:
            return app(*args).create_app()
        except TypeError as e:
            raise ValueError(f'uncorrect parameter: {project_type}: {e}')
