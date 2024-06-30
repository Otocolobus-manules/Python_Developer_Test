from fastapi import APIRouter
from core.schemas.user import UserRead, UserCreate, UserUpdate, UserDelete
from core.services.user_service import user_service

user_router = APIRouter(tags=['Users'])


@user_router.post('/create_user', response_model=UserRead)
async def create_user_api(user: UserCreate):
    result = await user_service.create_user(user=user)
    return result


@user_router.put('/update_user', response_model=UserRead)
async def update_user_api(user: UserUpdate):
    result = await user_service.update_user(user=user)
    return result


@user_router.get('/get_user', response_model=UserRead)
async def get_user_api(user_id: int):
    result = await user_service.get_user(user_id=user_id)
    return result


@user_router.delete('/delete_user', response_model=UserRead)
async def delete_user_api(user: UserDelete):
    result = await user_service.delete_user(user=user)
    return result
