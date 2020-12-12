from app.api.models import UserSchema
from app.db import TableUser, database, CiTanTask
import datetime
from sqlalchemy.sql import func
import uuid
from app.main import ws_manager
from app.api import socket_msg
from app.util.json_util import DateEncoder,json

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


async def update_user_citan_task(user_id, msg_data):
    # 全删
    query = CiTanTask.delete().where(user_id == CiTanTask.c.user_id)
    await database.execute(query=query)
    for task_data in msg_data:
        if task_data["acc"] == "":
            continue
        if task_data["acc"] == '000000':
            continue
        if task_data["acc_pas"] == '000000':
            continue
        if task_data["acc_pas"] == "":
            continue
        start_hour = -1
        if task_data["start_time"] != "立刻":
            start_hour = int(task_data["start_time"])
        query = CiTanTask.insert().values(user_id=user_id,
                                          account_number=task_data["acc"],
                                          account_password=task_data["acc_pas"],
                                          server1=task_data["acc_server1"],
                                          server2=task_data["acc_server2"],
                                          task_change_time=func.now(),
                                          task_start_time=start_hour
                                          )
        await database.execute(query=query)


async def syn_user_task_data(user_id):
    query = CiTanTask.select().where(user_id == CiTanTask.c.user_id)
    all_task = await database.fetch_all(query=query)
    data = []
    for task in all_task:
        data.append(dict(task))
    data = {
        "func":socket_msg.citan_table_syn,
        "data":data
    }
    data = json.dumps(data,cls = DateEncoder)
    await ws_manager.send_personal_message(user_id,data,isjson=False)