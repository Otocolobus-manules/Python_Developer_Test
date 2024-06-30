class UserNotFoundException(Exception):   # Пользователь к которому обращаются отсутствует
    def __init__(self, user_id):
        self.user_id = user_id
        self.message = f"User with id {user_id} not found."
        super().__init__(self.message)


class RepositoryTypeNotFoundError(Exception):    # Репозитория указанного в конфигурации не существует
    def __init__(self, repository_type):
        self.repository_type = repository_type
        self.message = f"repository {repository_type} not found."
        super().__init__(self.message)
