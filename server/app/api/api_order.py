from typing import List

from app.modules import md_couponse
from fastapi import APIRouter
import app.config as cfg
from app.api.models import CouPonseAct

router = APIRouter()

@router.get("/ceshi")
async def ceshi():
    return "order"


@router.get("/create")
async def generator_couponse():
    pass
