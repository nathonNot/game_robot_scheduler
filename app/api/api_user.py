from typing import List

from app.modules import md_user
from app.api.models import UserDB, UserSchema
from fastapi import APIRouter, HTTPException, Path, Header
from app.util.rsa import return_respons
from app.main import ws_manager

router = APIRouter()


@router.post("/create_user", status_code=201)
async def create_user(payload: UserSchema, X_Forwarded_For: str = Header(None)):
    note,code = await md_user.creat_user(payload, X_Forwarded_For)
    return return_respons(code,note)


@router.post("/get_user", status_code=200)
async def create_user(payload: UserSchema, X_Forwarded_For: str = Header(None)):
    data,code = await md_user.get_user(payload,X_Forwarded_For)
    return return_respons(code,data)

@router.get("/{id}")
async def user_data(id: int = Path(..., gt=0),):
    data = await ws_manager.send_user_msg(id,{"msg":"asdasdasdasd"})
    return data
