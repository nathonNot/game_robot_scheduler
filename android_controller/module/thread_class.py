import threading
import global_variable
from lib.app import JiuYinApp
from loguru import logger

class JiuYinCiTanThread(threading.Thread):

    def __init__(self,user_name,user_password,server1,server2):
        super().__init__()
        self.user_name = user_name
        self.user_password = user_password
        self.server1 = server1
        self.server2 = server2

    def run(self):
        global_variable.app = 1
        citan = JiuYinApp(global_variable.an_conn)
        try:
            citan.login(self.user_name,self.user_password,self.server1,self.server2)
            citan.do_citan()
        except Exception as identifier:
            logger.error(str(identifier))
        finally:
            citan.close()
            global_variable.app = None
    
    def stop(self):
        pass

    @staticmethod
    def class_name():
        return "JiuYinCiTanThread"