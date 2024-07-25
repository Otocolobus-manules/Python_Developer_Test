from abc import ABC, abstractmethod


class IAppFactory(ABC):
    @abstractmethod
    def create_app(self, *args):
        raise NotImplementedError()
