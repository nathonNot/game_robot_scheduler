from logging import LogRecord
from typing import List

from fastapi import APIRouter
import app.config as cfg
from app.api.models import CreateOrder
from loguru import logger


router = APIRouter()

@router.get("/ceshi")
async def ceshi():
    return "order"


@router.get("/create")
async def generator_couponse(data:CreateOrder):
    logger.info(data.to_string())
    return data.to_json()
