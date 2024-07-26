import asyncio

from utils.IoC import IoC
from factories.user_repository_factory.RepositoryFactory import RepositoryFactory
from factories.project_type_factory.ProjectTypeFactory import ProjectTypeFactory

from services.UserCrudServices.CreateUserService import CreateUserService
from services.UserCrudServices.UpdateUserService import UpdateUserService
from services.UserCrudServices.DeleteUserService import DeleteUserService
from services.UserCrudServices.GetUserService import GetUserService


from config import settings


async def start_project():
    container = IoC()
    repository_factory = RepositoryFactory()
    repository = repository_factory.create_repository(repo_type=settings.user_repository_config.repository_type)

    container.register('Services.CreateUserService', CreateUserService(repository=repository))
    container.register('Services.GetUserService', GetUserService(repository=repository))
    container.register('Services.UpdateUserService', UpdateUserService(repository=repository))
    container.register('Services.DeleteUserService', DeleteUserService(repository=repository))

    app_factory = ProjectTypeFactory()
    app = await app_factory.create_app(settings.init_program_config.program_type, container)
    asyncio.run(app)


if __name__ == "__main__":
    asyncio.run(start_project())
    