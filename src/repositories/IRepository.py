from abc import ABC, abstractmethod

from schemas.User import CreateUser, UpdateUser, DeleteUser


class IRepository(ABC):   # Общий интерфейс для репозиториев
    @abstractmethod
    def get(self, user_id: int):
        raise NotImplementedError()

    @abstractmethod
    def create(self, user: CreateUser):
        raise NotImplementedError()

    @abstractmethod
    def update(self, user: UpdateUser):
        raise NotImplementedError()

    @abstractmethod
    def delete(self, user: DeleteUser):
        raise NotImplementedError()
