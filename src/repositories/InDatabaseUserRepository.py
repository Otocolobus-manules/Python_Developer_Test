from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from schemas.User import CreateUser, UpdateUser, DeleteUser
from repositories.IRepository import IRepository
from models.UserModel import UserModel
from exceptions.User.UserNotFoundException import UserNotFoundException


class InDatabaseUserRepository(IRepository):
    """
    Репозиторий для управления пользователями в базе данных.

    :param db_session: Сессия базы данных (асинхронная или синхронная)
    :type db_session: AsyncSession
    """
    def __init__(self, db_session: AsyncSession) -> None:
        """
        Инициализация репозитория

        :param db_session: Сессия базы данных (асинхронная или синхронная)
        :type db_session: AsyncSession | Session
        """
        self.__db_session = db_session

    async def create(self, user: CreateUser) -> UserModel:
        """
        Создает нового пользователя в базе данных.

        :param user: Данные для создания пользователя
        :type user: CreateUser
        :return: Созданный пользователь
        :rtype: UserModel
        """
        stmt = UserModel(**user.model_dump())
        self.__db_session.add(stmt)
        await self.__db_session.commit()
        return stmt

    async def get(self, user_id: int) -> UserModel:
        """
        Получает пользователя по идентификатору.

        :param user_id: Идентификатор пользователя
        :type user_id: int
        :return: Пользователь с указанным идентификатором
        :rtype: UserModel
        :raises UserNotFoundException: Если пользователь не найден
        """
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await self.__db_session.scalars(stmt)
        user = result.first()
        if not user:
            raise UserNotFoundException(user_id)
        return user

    async def update(self, user: UpdateUser) -> UserModel:
        """
        Обновляет данные пользователя.

        :param user: Данные для обновления пользователя
        :type user: UpdateUser
        :return: Обновленный пользователь
        :rtype: UserModel
        :raises UserNotFoundException: Если пользователь не найден
        """
        stmt = (
            update(UserModel)
            .where(UserModel.id == user.id)
            .values(name=user.name)
            .returning(UserModel)
        )
        result = await self.__db_session.execute(stmt)
        updated_user = result.scalar_one_or_none()

        if not updated_user:
            raise UserNotFoundException(user.id)

        await self.__db_session.commit()
        return updated_user

    async def delete(self, user: DeleteUser) -> UserModel:
        """
        Удаляет пользователя из базы данных.

        :param user: Данные для удаления пользователя
        :type user: DeleteUser
        :return: Удаленный пользователь
        :rtype: UserModel
        :raises UserNotFoundException: Если пользователь не найден
        """
        stmt = (
            delete(UserModel)
            .where(UserModel.id == user.id)
            .returning(UserModel)
        )
        result = await self.__db_session.execute(stmt)
        deleted_user = result.scalar_one_or_none()

        if not deleted_user:
            raise UserNotFoundException(user.id)

        await self.__db_session.commit()
        return deleted_user
