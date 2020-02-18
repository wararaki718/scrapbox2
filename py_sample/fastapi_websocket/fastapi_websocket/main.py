from fastapi import Cookie, Depends, FastAPI, Header
from starlette.staticfiles import StaticFiles

from .routers import index
from .routers import socket


api = FastAPI()
api.mount('/static', StaticFiles(directory='fastapi_websocket/static'), name='static')

api.include_router(index.router)
api.include_router(socket.router)
