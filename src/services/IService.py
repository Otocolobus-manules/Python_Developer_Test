from abc import ABC, abstractmethod


class IService(ABC):
    @abstractmethod
    def __call__(self, *args):
        raise NotImplementedError()
