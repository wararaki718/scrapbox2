from fastapi import APIRouter
from starlette.templating import Jinja2Templates
from starlette.requests import Request


router = APIRouter()
templates = Jinja2Templates(directory='fastapi_websocket/static')


@router.get("/")
async def get(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
