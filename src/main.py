import uvicorn
from fastapi import FastAPI
from api import user_router
from core.config import settings
from fastapi.responses import ORJSONResponse
from core.exception import UserNotFoundException
from core.exception import user_not_found_exception_handler


main_app = FastAPI(
    title="Project",
    default_response_class=ORJSONResponse,
)

main_app.include_router(user_router)

main_app.add_exception_handler(UserNotFoundException, user_not_found_exception_handler)


if __name__ == "__main__":
    uvicorn.run(
        'main:main_app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
