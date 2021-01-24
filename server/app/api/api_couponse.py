from typing import List

from app.modules import md_couponse
from fastapi import APIRouter, HTTPException, Path, Header
from app.util.rsa import return_respons
from app.main import ws_manager
import app.config as cfg

router = APIRouter()

router.get("/generator")
async def generator_couponse(gm_key:str="",num:int=1):
    if gm_key != cfg.get_config_dc()["couponse_key"]:
        return "密钥不正确"
    return md_couponse.generate_conponse(num)
