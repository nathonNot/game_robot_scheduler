from starlette.websockets import WebSocket,WebSocketDisconnect
from fastapi import APIRouter,FastAPI,HTTPException
import base64
import json
from app.main import ws_manager
from typing import Optional
import app.config as cfg

router = APIRouter()

@router.websocket("/ws/{user_base64}")
async def websocket_endpoint(
    websocket: WebSocket,user_base64:str
):
    # 解码
    data = ""
    try:
        data = base64.b64decode(user_base64)
        data = json.loads(data)
    except Exception as identifier:
        await websocket.close()
    if data == "":
        return
    user_id = data["user_id"]
    await ws_manager.connect(websocket,user_id)

    try:
        while True:
            data = await websocket.receive_json()
            await ws_manager.call_back(user_id,data["call_back"],data["data"])
    except WebSocketDisconnect:
        ws_manager.disconnect(user_id)
        await ws_manager.broadcast(f"用户-{user_id}-离开")

@router.websocket("/ws/an/{key}")
async def websocket_endpoint(
    websocket: WebSocket,key:str
):
    key1 = key.split("__")[1]
    key2 = key.split("__")[0]
    if key2 != cfg.get_config_dc()["android_ws_key"]:
        return
    await ws_manager.android_connect(websocket,key1)
    try:
        while True:
            data = await websocket.receive_json()
    except WebSocketDisconnect:
        ws_manager.an_disconnect(key1)
