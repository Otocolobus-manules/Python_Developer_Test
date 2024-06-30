from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession, async_sessionmaker
from typing import AsyncGenerator, AsyncContextManager
from core.config import settings


class DatabaseHelper:   # вспомогательный класс для управления подключением к базе данных
    def __init__(
            self,
            url: str,
            echo: bool = False,
            echo_pool: bool = False,
            pool_size: int = 10,
            max_overflow: int = 10,
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:   # Метод для завершения соединения
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:   # метод для получения сессии
        async with self.async_session() as session:
            yield session


db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)
