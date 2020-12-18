from typing import List

from starlette.types import Message

from app.modules import md_task
from app.api.models import UserDB, UserSchema
from fastapi import APIRouter, HTTPException, Path, Header
from app.util.rsa import return_respons
from app.main import ws_manager

router = APIRouter()


@router.get("/citan_t", status_code=200)
async def citan_test(user_name: str, pas_word: str):
    data = await ws_manager.an_con_send_msg({
        "msg": "start_citan",
        "user_name": "asd",
        "pas_word": "22222"
    },"citan_test")
    return data

@router.get("/all_an")
async def get_all_an_con():
    data = await ws_manager.get_all_an_con()
    return data


@router.get("/an/status")
async def get_an_status(an_key: str):
    call_back = "get_an_status"
    message = {
        "func": call_back,
        "data": 1
    }
    data = await ws_manager.an_con_send_msg_one(an_key, message, call_back)
    return data


@router.get("/an/cmd")
async def get_command(an_key: str):
    call_back = "cmd_line"
    message = {
        "func": call_back,
        "data": "adb devices"
    }
    data = await ws_manager.an_con_send_msg_one(an_key, message, call_back)
    return data


@router.get("/an/device_con")
async def device_con(an_key:str):
    call_back = "device_con"
    message = {
        "func": call_back,
        "data": "emulator-5554"
    }
    data = await ws_manager.an_con_send_msg_one(an_key, message, call_back)
    return data

@router.get("/start_citan")
async def device_con(an_key:str):
    call_back = "start_citan"
    message = {
        "func": call_back,
        "data": {
            "user_name":"aaaaa",
            "user_password":"sssss",
            "server1":"江湖七区",
            "server2":"醉江湖"
        }
    }
    data = await ws_manager.an_con_send_msg_one(an_key, message, call_back)
    return data

@router.get("/start_citan2")
async def device_con(task_id:int):
    call_back = "start_citan2"
    # 先查，再推送
    task_data,status = await md_task.get_task(task_id)
    if status != 200:
        return task_data
    message = {
        "func": call_back,
        "data": task_data
    }
    data = await ws_manager.an_con_send_msg(message, call_back)
    return data