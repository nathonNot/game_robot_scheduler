
from loguru import logger
from app.main import ws_manager
from app.modules import md_user


class FunctionManager:

    login_func = []
    func_dc = {}

    def __init__(self):
        logger.info("初始化websocket回调")
        self.func_dc = {}
        self.login_func = []

    def __call__(self, func_name, login_func = False, *args, **kwargs):
        def register(cls):
            self.func_dc[func_name] = cls
            if login_func == True:
                self.login_func.append(cls)
            return cls
        return register


function_manager = FunctionManager()


@function_manager(func_name="hand_test")
async def hand_test(user_id, msg):
    print(msg)


@function_manager(func_name="get_citan_task")
async def get_citan_task(user_id, msg):
    print(user_id)


@function_manager(func_name="update_citan_task")
async def update_citan_task(user_id, msg):
    await md_user.update_user_citan_task(user_id, msg)
    await syn_user_task_data(user_id, "")


@function_manager(func_name="syn_user_task_data", login_func=True)
async def syn_user_task_data(user_id, msg):
    await md_user.syn_user_task_data(user_id)
