from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.User.UserNotFoundException import UserNotFoundException


def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": exc.message},
    )
