import uvicorn
from fastapi import FastAPI
from api import user_router
from core.config import settings
from fastapi.responses import ORJSONResponse


main_app = FastAPI(
    title="Project",
    default_response_class=ORJSONResponse,
)

main_app.include_router(user_router)


if __name__ == "__main__":
    uvicorn.run(
        'main:main_app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
