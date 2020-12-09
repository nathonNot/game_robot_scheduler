from typing import List

from app.modules import md_user
from app.api.models import UserDB, UserSchema
from fastapi import APIRouter, HTTPException, Path, Header
from app.util.rsa import return_respons
from app.main import ws_manager

router = APIRouter()


@router.get("/citan_t", status_code=200)
async def create_user(user_name: str, pas_word: str):
    data = await ws_manager.an_con_send_msg({
        "msg": "start_citan",
        "user_name": "asd",
        "pas_word": "22222"
    })
    return data


# @router.get("/an_status", status_code=200)
# async def get_an_status():
#     data = await ws_manager.an_con_send_msg({
#         "msg": "start_citan",
#         "user_name": "asd",
#         "pas_word": "22222"
#     })
#     return data


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
