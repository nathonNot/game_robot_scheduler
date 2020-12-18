from app.db import TableUser, database, CiTanTask


async def get_task(task_id:int):
    query = CiTanTask.select().where(task_id == CiTanTask.c.task_id)
    task_data = await database.fetch_one(query=query)
    if task_data is None:
        return {"msg": "未找到此任务"}, 404
    return {
            "task_id": task_data.get("task_id"),
            "user_name": task_data.get("account_number"),
            "user_password": task_data.get("account_password"),
            "server1":task_data.get("server1"),
            "server2":task_data.get("server2")
            }, 200