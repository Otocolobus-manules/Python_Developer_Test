from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from core.config import settings


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )
