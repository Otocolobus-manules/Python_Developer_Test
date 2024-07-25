from abc import ABC, abstractmethod
from repositories.IRepository import IRepository


class IFactory(ABC):
    @abstractmethod
    def create_repository(self, *args) -> IRepository:
        raise NotImplementedError()
