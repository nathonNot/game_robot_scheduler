
from app.api.models import CreateOrder
from app.db import OrderDb,database,TableUser
from app.util.json_util import DateEncoder,json,get_uuid
from sqlalchemy.sql import func
from app.lib import alipay
from loguru import logger
import datetime

async def create_order(data:CreateOrder):
    insert_dc = {}
    if data.user_name != "" or data.recharge:
        query = TableUser.select().where(data.user_name == TableUser.c.user_name)
        userdb = await database.fetch_one(query=query)
        if userdb is None:
            return 440,"用户账户不存在"
        insert_dc["user_id"] = userdb.get("id")
    if data.user_phone != 0 and len(str(data.user_phone)) < 11:
        return 440,"手机号格式不正确"
    if data.buyer_num <= 0:
        return 400,"购买数量不能小于0"
    order_id = get_uuid()
    insert_dc["id"] = order_id
    insert_dc["create_time"]=func.now()
    insert_dc["buy_num"] = data.buyer_num
    insert_dc["status"] = 0
    insert_dc["phone_num"] = str(data.user_phone)
    if data.recharge:
        insert_dc["is_zhichong"] = 1
    else:
        insert_dc["is_zhichong"] = 0
    query = OrderDb.insert().values(**insert_dc)
    query = await database.execute(query=query)
    url = alipay.get_pay_url(order_id,0.1)
    return 200,{"url":url}

async def inpay_order(data:dict):
    order_id = data["out_trade_no"]
    trade_no = data["trade_no"]
    trade_status = data["trade_status"]
    if trade_status != "TRADE_SUCCESS":
        logger.info("标识未成功")
        return
    query = OrderDb.select().where(order_id == OrderDb.c.id)
    order = await database.fetch_one(query=query)
    if order is None:
        logger.error("未找到订单相关数据")
        return
    # 修改状态为支付成功
    update = (
        OrderDb.update()
        .where(OrderDb.c.id == order_id)
        .values(pay_time = datetime.datetime.now(),
                status = 1,
                order_id = trade_no
        )
        .returning(OrderDb.c.id)
    )
    await database.execute(query=update)
    return