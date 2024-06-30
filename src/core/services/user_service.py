from core.repositories import get_repository


repository = get_repository()


class UserService:
    @staticmethod
    async def create_user(user):
        return await repository.create_user(user=user)

    @staticmethod
    async def update_user(user):
        return await repository.update_user(user=user)

    @staticmethod
    async def get_user(user_id):
        return await repository.get_user(user_id=user_id)

    @staticmethod
    async def delete_user(user):
        return await repository.delete_user(user=user)


user_service = UserService()
