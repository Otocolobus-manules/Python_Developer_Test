from abc import ABC, abstractmethod
from core.schemas.user import UserCreate, UserUpdate, UserDelete
from core.models import User


class UserRepositoryInterface(ABC):   # Абстрактный класс для представления репозиториев
    @abstractmethod
    async def create_user(self, user: UserCreate) -> User:
        pass

    @abstractmethod
    async def update_user(self, user: UserUpdate) -> User:
        pass

    @abstractmethod
    async def get_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    async def delete_user(self, user: UserDelete) -> User:
        pass
