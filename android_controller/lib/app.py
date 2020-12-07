import config.config as cfg

class JiuYinApp():

    def __init__(self,app):
        self.config_dc = cfg.get_config()
        self.app = app.session(self.config_dc["jiuyin_pkg_name"]) # 启动应用并获取session

    def login(self,user,pass,server1,server2):
        self.app(resourceId = self.id_res('et_name')).click()
        self.app.send_keys(user)
        self.app(resourceId = self.id_res('et_pwd')).click()
        self.app.send_keys(pass)
        self.app(resourceId = self.id_res('signin_button')).click()
        text_str = "//*[@text='{server_name}']"
        server1_str = text_str.format(server_name = server1)
        self.app.xpath(server1_str).click()
        server2_str = text_str.format(server_name = server2)
        self.app.xpath(server2_str).click()
    
    def start_citan(self):
        self.app(resourceId = self.id_res('citan_btn')).click()
        self.app(resourceId = self.id_res('item_citan_btn')).click()

    def do_citan(self):
        pass

    
    def can_citan(self,button):
        jd = button+"_jd"
        jd = self.id_res(jd)
        ret_str = ""
        try:
            ret_str = self.app(resourceId = jd).get_text()
        except Exception as identifier:
            pass
        if ret_str == "":
            return 0
        # 进度:0/4
        num = ret_str.split(":")[1]
        num1 = num.split("/")[0]
        num2 = num.split("/")[1]
        return num2 - num1

    def id_res(self,id_name):
        return self.config_dc["jiuyin_pkg_name"] + ":id/" + id_name

    def close(self):
        self.app.close()
