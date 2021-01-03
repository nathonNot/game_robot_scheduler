
from loguru import logger
import os
import uiautomator2 as u2
import global_variable
from lib import msg_state
from module.thread_class import JiuYinCiTanThread


class FunctionManager:

    def __init__(self):
        logger.info("初始化websocket回调")
        self.func_dc = {}

    def __call__(self, func_name, *args, **kwargs):
        def register(cls):
            self.func_dc[func_name] = cls
            return cls
        return register


function_manager = FunctionManager()


@function_manager(func_name="hand_test")
def hand_test(data):
    print(data)


@function_manager(func_name="get_an_status")
def get_an_status(data):
    if global_variable.app == None:
        return "ready"
    return "running"


@function_manager(func_name="cmd_line")
def cmd_line(data):
    d = os.popen(data)
    f = d.read()
    return f


@function_manager(func_name="device_con")
def device_con(data):
    try:
        global_variable.an_conn = u2.connect(data)
    except Exception as identifier:
        return str(identifier)
    return "conn success"


@function_manager(func_name="start_citan")
def start_citan(data):
    if global_variable.app != None:
        return {
            "status": msg_state.an_not_ready,
            "msg": "设备正在运行任务"
        }
    task_id = data.get("task_id",1)
    jyct = JiuYinCiTanThread(task_id,
        data["user_name"], data["user_password"], data["server1"], data["server2"])
    jyct.start()
    return {
            "status": msg_state.citan_start_succes,
            "msg": "任务创建成功"
        }
