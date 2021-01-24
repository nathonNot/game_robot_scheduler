from app.api.models import UserSchema
from app.db import VipCouponse,database,TableUser
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

async def activate_componse(user_id:str,componse_id:str):
    query = VipCouponse.select().where(VipCouponse.c.id == componse_id)
    compose = await database.fetch_one(query=query)
    if compose is None:
        return {"msg": "不存在此激活码"}
    if int(compose.get("status")) == 1:
        return {"msg":"此激活码已失效"}
    if not compose.get("activate_user_id") is None:
        return {"msg":"此激活码已失效"}
    query = TableUser.select().where(user_id == TableUser.c.id)
    userdb = await database.fetch_one(query=query)
    if userdb is None:
        return {"msg": "用户不存在"}
    user_vip_end_time = userdb.get("user_vip_end_time")
    if user_vip_end_time is None:
        user_vip_end_time = datetime.datetime.now()
    user_vip_end_time += datetime.timedelta(days=30)
    update = (
        TableUser
        .update()
        .where(userdb.get("id") == TableUser.c.id)
        .values(user_vip_end_time=user_vip_end_time)
        .returning(TableUser.c.id)
    )
    await database.execute(query=update)
    update = {
        VipCouponse.update()
        .where(VipCouponse.c.id == componse_id)
        .values(activate_time = datetime.datetime.now(),
                activate_user_id = user_id,
                status = 1
        )
        .returning(VipCouponse.c.id)
    }
    await database.execute(query=update)
    return {"msg":"激活成功"}