from app.api.models import UserSchema
from app.db import VipCouponse,database
import datetime
from sqlalchemy.sql import func
import uuid
from app.main import ws_manager
from app.api import socket_msg
from app.util.json_util import DateEncoder,json,get_uuid
import app.config as cfg

async def generate_conponse(count:int):
    ret_list = []
    m_pone = cfg.get_config_dc()["admin_phone"]
    for _ in range(count):
        id = get_uuid()
        query = VipCouponse.insert().values(id = id, create_time = func.now(),creater_phone=m_pone,status=0)
        query = await database.execute(query=query)
        ret_list.append(id)
    response_object = {
        "msg": "生成成功",
        "couponse_list": ret_list
    }
    return response_object, 200