import uvicorn
from fastapi import FastAPI

from utils.IoC import IoC


async def fastapi_app(container: IoC):
    app = FastAPI()

    config = uvicorn.Config(
        app,
        reload=True,
        host="127.0.0.1",
        port=8000)
    server = uvicorn.Server(config=config)
    await server.serve()
