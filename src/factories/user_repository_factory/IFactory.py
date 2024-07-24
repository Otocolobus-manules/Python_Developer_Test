from abc import ABC, abstractmethod
from repositories.IRepository import IRepository


class IFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_repository(*args) -> IRepository:
        raise NotImplementedError()
