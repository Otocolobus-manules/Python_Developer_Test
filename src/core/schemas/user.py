from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


class UserCreate(BaseModel):
    username: str


class UserRead(User):
    id: int
    username: str


class UserUpdate(BaseModel):
    id: int
    username: str


class UserDelete(BaseModel):
    id: int
