from app.api.models import UserSchema
from app.db import TableUser, database
import datetime
from sqlalchemy.sql import func
import uuid


async def creat_user(user: UserSchema, ip: str):
    query = TableUser.select().where(TableUser.c.user_name == user.user_name)
    userdb = await database.fetch_one(query=query)
    if not userdb is None:
        return {"msg": "已存在此用户"}, 210
    query = TableUser.insert().values(id=get_user_id(), user_name=user.user_name,
                                      user_password=user.user_pass, user_last_ip=ip, user_creat_time=func.now())

    query = await database.execute(query=query)
    response_object = {
        "msg": "注册成功",
        "id": query,
        "user_name": user.user_name,
    }
    return response_object, 200


async def get_user(user: UserSchema, ip: str):
    query = TableUser.select().where(user.user_name == TableUser.c.user_name)
    userdb = await database.fetch_one(query=query)
    if userdb is None:
        return {"msg": "未找到此用户"}, 404
    if userdb.get("user_password") != user.user_pass:
        return {"msg": "用户密码不正确"}, 405
    # 更新用户登录时间和ip
    update = (
        TableUser
        .update()
        .where(userdb.get("id") == TableUser.c.id)
        .values(user_last_login_time=datetime.datetime.now(), user_last_ip=ip)
        .returning(TableUser.c.id)
    )
    await database.execute(query=update)
    return {"msg": "成功",
            "id": userdb.get("id"),
            "user_name": userdb.get("user_name"),
            "user_password": userdb.get("user_password")}, 200


def get_user_id():
    return str(uuid.uuid4())
