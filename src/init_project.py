from utils.IoC import IoC
from utils.DatabaseHelper import DatabaseHelper

from factories.user_repository_factory.RepositoryFactory import RepositoryFactory

from services.UserCrudServices.CreateUserService import CreateUserService
from services.UserCrudServices.UpdateUserService import UpdateUserService
from services.UserCrudServices.DeleteUserService import DeleteUserService
from services.UserCrudServices.GetUserService import GetUserService

from config import settings


def init_project() -> IoC:
    container = IoC()

    db_session = DatabaseHelper(
        settings.user_repository_config.settings.url,
    ).session_getter()

    repository_factory = RepositoryFactory()
    repository = repository_factory.create_repository(settings.user_repository_config.repository_type,
                                                      db_session)

    container.register('Services.CreateUserService', CreateUserService(repository=repository))
    container.register('Services.GetUserService', GetUserService(repository=repository))
    container.register('Services.UpdateUserService', UpdateUserService(repository=repository))
    container.register('Services.DeleteUserService', DeleteUserService(repository=repository))

    return container
    