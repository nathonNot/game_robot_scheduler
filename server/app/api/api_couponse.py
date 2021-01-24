from typing import List

from app.modules import md_couponse
from fastapi import APIRouter
import app.config as cfg
from app.api.models import CouPonseAct

router = APIRouter()

@router.get("/ceshi")
async def ceshi():
    return "couponse"


@router.get("/generator")
async def generator_couponse(gm_key:str="",num:int=1):
    key = cfg.get_config_dc()["couponse_key"]
    if gm_key != key:
        return "密钥不正确"
    return await md_couponse.generate_conponse(num)

@router.post("/activate")
async def activate_couponse(data:CouPonseAct):
    return await md_couponse.activate_componse(data.user_id,data.couponse_id)

