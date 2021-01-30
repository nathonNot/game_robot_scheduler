from fastapi import APIRouter
from starlette.requests import Request
from app.util.rsa import return_respons
import json
from loguru import logger
from app.modules import md_order

router = APIRouter()


@router.post("/ali_pay")
async def alipay_gatwey(request: Request):
    data = await request.form()
    query_data = request.query_params
    logger.info(query_data)
    order_id = data.get("out_trade_no","")
    if order_id == "":
        logger.error(data)
        return "error"
    md_order.inpay_order(data)
    logger.info(data)
    return "success"