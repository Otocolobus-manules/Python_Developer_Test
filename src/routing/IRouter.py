from abc import ABC, abstractmethod


class IRouter(ABC):
    @abstractmethod
    def get_router(self, *args):
        raise NotImplementedError()
