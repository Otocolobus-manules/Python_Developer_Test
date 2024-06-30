from sqlalchemy.ext.asyncio import AsyncSession
from core.models import User
from sqlalchemy import select, update, delete
from core.schemas.user import UserCreate, UserUpdate, UserDelete
from core.exception.exceptions import UserNotFoundException


async def create_user(session: AsyncSession, user: UserCreate) -> User:
    stmt = User(**user.model_dump())
    session.add(stmt)
    await session.commit()
    return stmt


async def update_user(session: AsyncSession, user: UserUpdate) -> User:
    stmt = (
        update(User)
        .where(User.id == user.id)
        .values(username=user.username)
        .returning(User)
    )
    result = await session.execute(stmt)
    updated_user = result.scalar_one_or_none()

    if not updated_user:
        raise UserNotFoundException(user.id)

    await session.commit()
    return updated_user


async def get_user(session: AsyncSession, user_id: int) -> User:
    stmt = select(User).where(User.id == user_id)
    result = await session.scalars(stmt)
    user = result.first()
    if not user:
        raise UserNotFoundException(user_id)
    return user


async def delete_user(session: AsyncSession, user: UserDelete) -> User:
    stmt = (
        delete(User)
        .where(User.id == user.id)
        .returning(User)
    )
    result = await session.execute(stmt)
    deleted_user = result.scalar_one_or_none()

    if not deleted_user:
        raise UserNotFoundException(user.id)

    await session.commit()
    return deleted_user
