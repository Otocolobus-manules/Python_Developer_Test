class UserNotFoundException(Exception):
    """
    Исключение, выбрасываемое, когда пользователь не найден.

    :param user_id: Идентификатор пользователя, который не был найден
    :type user_id: int
    """
    def __init__(self, user_id: int):
        """
        Инициализация исключения.

        :param user_id: Идентификатор пользователя, который не был найден
        :type user_id: int
        """
        self.user_id = user_id
        self.message = f"User with id {user_id} not found."
        super().__init__(self.message)
