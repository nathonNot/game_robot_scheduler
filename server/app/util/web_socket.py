from starlette.endpoints import WebSocketEndpoint
from typing import Optional, List, Dict
from starlette.websockets import WebSocket, WebSocketDisconnect
from loguru import logger
import asyncio


class ConnectionManager:

    # 存放激活的ws连接对象
    active_connections: Dict[int, WebSocket] = {}

    async_callback_data = {}

    # 安卓端ws对象
    android_connections: Dict[int, WebSocket] = {}
    android_connections_status: Dict[int, dict] = {}

    def __init__(self):
        pass

    async def connect(self, ws: WebSocket, user_id: int):
        # 等待连接
        await ws.accept()
        # 存储ws连接对象
        if user_id in self.active_connections:
            await self.active_connections[user_id].send_json({"msg": "被其他用户t下线"})
            await self.active_connections[user_id].close()
        self.active_connections[user_id] = ws

    async def android_connect(self, ws: WebSocket,key1):
        # 等待连接
        await ws.accept()
        # 存储ws连接对象
        self.android_connections[key1] = ws
        self.android_connections_status[key1] = {"status":"ready"}

    def disconnect(self, user_id):
        # 关闭时 移除ws对象
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    def an_disconnect(self, key):
        # 关闭时 移除ws对象
        if key in self.android_connections:
            del self.android_connections[key]

        if key in self.android_connections_status:
            del self.android_connections_status[key]

    @staticmethod
    async def send_personal_message(message: dict, ws: WebSocket):
        # 发送个人消息
        await ws.send_json(message)

    @classmethod
    async def send_user_msg(cls, user_id, message):
        if not user_id in cls.active_connections:
            return {"msg": "错误，客户端未连接"}
        if user_id in cls.active_connections:
            await cls.active_connections[user_id].send_json(message)
            data = await cls.get_res_data(user_id,"send_user_msg")
            return data
        return "okokokok"
    
    @classmethod
    async def an_con_send_msg(cls,message):
        for k,v in cls.android_connections_status.items():
            if v["status"] == "ready":
                ws = cls.android_connections.get(k,None)
                if ws != None:
                    await ws.send_json(message)
                    return "任务提交完成"
        return "未找到可用"

    async def broadcast(self, message: str):
        # 广播消息
        for connection in self.active_connections.values():
            await connection.send_text(message)

    @classmethod
    async def call_back(cls,user_id,call_back_func_name,data):
        if user_id not in cls.async_callback_data:
            cls.async_callback_data[user_id] = {}
        if call_back_func_name not in cls.async_callback_data[user_id]:
            cls.async_callback_data[user_id][call_back_func_name] = ""
        cls.async_callback_data[user_id][call_back_func_name] = data

    @classmethod
    async def get_res_data(cls,user_id,func_name):
        n = 0.5
        while n < 2:
            await asyncio.sleep(0.5)
            func_dc = cls.async_callback_data.get(user_id,{})
            if func_dc == {}:
                continue
            if func_name in func_dc:
                return func_dc[func_name]
        return "未知错误"