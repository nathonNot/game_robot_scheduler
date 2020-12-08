import uiautomator2 as u2
from lib.app import JiuYinApp
import os
from loguru import logger
import time
from lib.socket import WebSocketClient

def init_log():
    if not os.path.exists("log"):
        os.mkdir("log")

    log_path_error = os.path.join("log", f'{time.strftime("%Y-%m-%d")}_error.log')

    # 日志简单配置
    # 具体其他配置 可自行参考 https://github.com/Delgan/loguru
    logger.add(log_path_error, rotation="12:00", retention="5 days", enqueue=True)

def main():
    ws = WebSocketClient()
    ws.do_con()
    # d = u2.connect("emulator-5554")
    # app = JiuYinApp(d)
    # app.login("11111","11111","江湖七区","醉江湖")
    # app.do_citan()

if __name__ == "__main__":
    init_log()
    main()