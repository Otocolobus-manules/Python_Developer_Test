from fastapi import APIRouter
from .api_v1 import router as user_router_v1
from core.config import settings

user_router = APIRouter(
    prefix=settings.api.prefix,
)
user_router.include_router(user_router_v1)
