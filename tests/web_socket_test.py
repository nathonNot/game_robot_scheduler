import asyncio
import websockets
import base64
import json


# 客户端主逻辑
async def main_logic():
    user_info = {
        "user_id":5,
        "user_name":"abc",
        "user_pass":"1111"
    }
    user_data = json.dumps(user_info)
    user_data = base64.b64encode(user_data.encode('utf-8'))
    url = 'ws://127.0.0.1:8000/ws/'+user_data.decode('utf-8')

    async with websockets.connect(url) as websocket:
        cred_text = "i have a connection"
        await websocket.send(cred_text)
        while True:
            response_str = await websocket.recv()
            print(response_str)

asyncio.get_event_loop().run_until_complete(main_logic())