from sqlalchemy.orm import Mapped, mapped_column

from models.BaseCustomModel import BaseCustomModel


class UserModel(BaseCustomModel):   # Модель пользователь
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
