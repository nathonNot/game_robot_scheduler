
from app.api.models import CreateOrder
from app.db import OrderDb,database,TableUser
from app.util.json_util import DateEncoder,json,get_uuid
from sqlalchemy.sql import func


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
    insert_dc["phone_num"] = data.user_phone
    if data.recharge:
        insert_dc["is_zhichong"] = 1
    else:
        insert_dc["is_zhichong"] = 0
    query = OrderDb.insert().values(**insert_dc)
    query = await database.execute(query=query)

    return 200,{"url":"www.baidu.com"}
