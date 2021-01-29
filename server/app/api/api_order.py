from logging import LogRecord
from typing import List

from fastapi import APIRouter
import app.config as cfg
from app.api.models import CreateOrder
from loguru import logger
from app.modules import md_order

router = APIRouter()

@router.get("/ceshi")
async def ceshi():
    return "order"


@router.post("/create")
async def generator_couponse(data:CreateOrder):
    logger.info(data.to_string())
    status,ret = await md_order.create_order(data)
    return {
        "status":status,
        "msg":ret
    }
