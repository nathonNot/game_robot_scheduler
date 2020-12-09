
from loguru import logger



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
def hand_test(data):
    print(data)

@function_manager(func_name = "get_an_status")
def get_an_status(data):
    from global_variable import app
    if app == None:
        return "ready"
    return "running"        