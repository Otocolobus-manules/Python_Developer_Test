from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.User.UserNotFoundException import UserNotFoundException


def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    """
        Обработчик исключений для UserNotFoundException.

        :param request: Объект запроса FastAPI.
        :param exc: Исключение UserNotFoundException.
        :return: JSON-ответ с кодом состояния 404 и сообщением об ошибке.
        """
    return JSONResponse(
        status_code=404,
        content={"message": exc.message},
    )
