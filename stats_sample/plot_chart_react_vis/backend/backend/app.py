from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .routers import aggs


api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

api.include_router(aggs.router)
