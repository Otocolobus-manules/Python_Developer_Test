from typing import Dict
from core.schemas.user import UserCreate, UserUpdate, UserDelete
from core.models import User
from core.exception.exceptions import UserNotFoundException


class InMemoryRepository:
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.current_id = 1

    async def create_user(self, user: UserCreate) -> User:
        new_user = User(id=self.current_id, username=user.username)
        self.users[self.current_id] = new_user
        self.current_id += 1
        return new_user

    async def update_user(self, user: UserUpdate) -> User:
        if user.id not in self.users:
            raise UserNotFoundException(user.id)
        updated_user = self.users[user.id]
        updated_user.username = user.username
        return updated_user

    async def get_user(self, user_id: int) -> User:
        if user_id not in self.users:
            raise UserNotFoundException(user_id)
        return self.users[user_id]

    async def delete_user(self, user: UserDelete) -> User:
        if user.id not in self.users:
            raise UserNotFoundException(user.id)
        deleted_user = self.users.pop(user.id)
        return deleted_user


in_memory_repo = InMemoryRepository()
