from fastapi import APIRouter
from starlette.requests import Request
from app.util.rsa import return_respons
import json
from loguru import logger

router = APIRouter()


@router.get("/ali_pay")
async def alipay_hook(request: Request):
    logger.info(str(request.query_params))
    data = await request.body()
    logger.info(data)
    return "ok"

@router.post("/ali_pay")
async def alipay_gatwey(request: Request):
    logger.info(str(request.query_params))
    data = await request.body()
    logger.info(data)
    return "ok"