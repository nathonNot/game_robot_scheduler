from typing import List

from app.modules import md_user
from app.api.models import UserDB, UserSchema
from fastapi import APIRouter, HTTPException, Path, Header
from app.util.rsa import return_respons
from app.main import ws_manager

router = APIRouter()


@router.get("/citan_t", status_code=200)
async def create_user(user_name: str, pas_word:str):
    data = await ws_manager.an_con_send_msg({
        "msg":"start_citan",
        "user_name":"asd",
        "pas_word":"22222"
        })
    return data