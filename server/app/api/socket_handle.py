
from loguru import logger
from app.main import ws_manager


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


@function_manager(func_name = "hand_test")
async def hand_test(user_id,msg):
    print(msg)


@function_manager(func_name = "get_citan_task")
async def get_citan_task(user_id,msg):
    print(user_id)


@function_manager(func_name="update_citan_task")
async def update_citan_task(user_id,msg):
    print(msg)