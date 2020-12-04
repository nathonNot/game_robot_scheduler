import os
import time
from loguru import logger

def init_log():

    # print(f"log basedir{basedir}")  # /xxx/python_code/FastAdmin/backend/app
    # 定位到log日志文件

    if not os.path.exists("log"):
        os.mkdir("log")

    log_path_error = os.path.join("log", f'{time.strftime("%Y-%m-%d")}_error.log')

    # 日志简单配置
    # 具体其他配置 可自行参考 https://github.com/Delgan/loguru
    logger.add(log_path_error, rotation="12:00", retention="5 days", enqueue=True)