from fastapi import APIRouter
from app.util.rsa import return_respons
import json
from loguru import logger

router = APIRouter()


@router.get("/alipay_hook")
async def alipay_hook(*, out_trade_no: str = "", rade_no: str = ""):
    logger.info(out_trade_no)
    logger.info(rade_no)
    return "ok"

@router.post("/alipay_gatewey")
async def alipay_gatwey(*,a:str=""):
    return "ok"