from pydantic import BaseModel


class BaseUser(BaseModel):
    id: int
    name: str


class CreateUser(BaseModel):
    name: str


class DeleteUser(BaseModel):
    id: int


class UpdateUser(BaseModel):
    id: int
    name: str
