import asyncio
import base64
import json
import config.config as cfg
from loguru import logger
import websocket
import time
try:
    import thread
except ImportError:
    import _thread as thread
import random

class WebSocketClient():

    client = None
    
    def do_con(self):
        confg_dc = cfg.get_config()
        key = confg_dc["ws_con_key"]+"__"+str(random.randint(100,10000))
        url = confg_dc["ws_url"] + "/ws/an/"+key
        try:
            websocket.enableTrace(True)
            self.client = websocket.WebSocketApp(url,
                              on_message = WebSocketClient.on_message,
                              on_error = WebSocketClient.on_error,
                              on_close = WebSocketClient.on_close)
            self.client.on_open = WebSocketClient.on_open
            self.client.run_forever()
        except Exception as identifier:
            logger.info("socket 连接断开 "+str(identifier))

    @staticmethod
    def on_message(ws, message):
        # 防止依赖崩
        from module.msg_hand import function_manager as func_man

        logger.debug(message)
        data = ""
        res = None
        try:
            data = json.loads(message)
            res = {}
            res["call_back"] = data["func"]
            res["data"] = func_man.func_dc[data["func"]](data=data["data"])
        except Exception as identifier:
            logger.error(str(identifier))
            logger.error(message)
            if data != "":
                res = {
                    "call_back":data["func"],
                    "data":str(identifier)
                }
        
        if res != None:
            ws.send(json.dumps(res))

    @staticmethod
    def on_error(ws, error):
        logger.error(error)

    @staticmethod
    def on_close(ws):
        logger.info("### closed ###")

    @staticmethod
    def on_open(ws):
        def run(*args):
            logger.info("con to server")
        thread.start_new_thread(run, ())

    @classmethod
    def send_json(cls,data):
        cls.client.send(json.dump(data))