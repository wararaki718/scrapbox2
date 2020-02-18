from fastapi import APIRouter
from starlette.websockets import WebSocket


router = APIRouter()


@router.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        text = await websocket.receive_text()
        await websocket.send_text(text)
