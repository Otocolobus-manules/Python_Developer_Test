from fastapi import APIRouter

from core.config import settings
from .users import user_router

router = APIRouter(
    prefix=settings.api_v1.prefix,
)

router.include_router(
    user_router,
    prefix=settings.api_v1.users,
)
