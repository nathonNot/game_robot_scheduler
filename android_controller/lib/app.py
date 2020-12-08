import config.config as cfg
import time
from loguru import logger


class JiuYinApp():

    def __init__(self, app):
        self.config_dc = cfg.get_config()
        self.app = app.session(
            self.config_dc["jiuyin_pkg_name"])  # 启动应用并获取session

    def login(self, user_name, pas_word, server1, server2):
        self.app(resourceId=self.id_res('et_name')).click()
        self.app.send_keys(user_name)
        self.app(resourceId=self.id_res('et_pwd')).click()
        self.app.send_keys(pas_word)
        self.app(resourceId=self.id_res('signin_button')).click()
        text_str = "//*[@text='{server_name}']"
        server1_str = text_str.format(server_name=server1)
        self.app.xpath(server1_str).click()
        server2_str = text_str.format(server_name=server2)
        self.app.xpath(server2_str).click()

    def start_citan(self):
        self.app(resourceId=self.id_res('citan_btn')).click()
        self.app(resourceId=self.id_res('item_citan_btn')).click()
        time.sleep(5)

    def do_citan(self):
        self.start_citan()
        # 防止数据加载不出来
        self.app.press("back")
        self.start_citan()
        citan_num = self.get_citan_cishu()
        need_citan_num = citan_num
        logger.debug("此账号需要刺探次数："+str(citan_num))
        if citan_num <= 0:
            return
        school = self.config_dc["menpai_list"]
        for s in school:
            if self.citan_btn_check(s):
                break
        citan_num -= 1
        # 这个时候会回退到最开始界面
        if citan_num <= 0:
            logger.info("刺探结束")
            return
        for _ in range(0, citan_num):
            time.sleep(1)
            self.start_citan()
            logger.debug("开始剩余刺探:"+str(citan_num))
            for s in school:
                if self.citan_btn_check(s):
                    # 跳出第一层
                    break
        logger.info("本次刺探结束，刺探完成次数:"+need_citan_num)

    def citan_btn_check(self, btn):
        btn_res = "citan_"+btn
        if self.can_citan(btn) > 0:
            logger.debug("开始刺探，刺探门派："+btn)
            self.app(resourceId=self.id_res(btn_res)).click()
            self.check_citan()
            return True
        return False

    def can_citan(self, button):
        jd = button+"_jd"
        jd = self.id_res(jd)
        ret_str = ""
        self.app.implicitly_wait(3)
        try:
            ret_str = self.app(resourceId=jd).get_text()
        except Exception as identifier:
            pass
        self.app.implicitly_wait(20)
        if ret_str == "":
            return 0
        # 进度:0/4
        num = ret_str.split(":")[1]
        num1 = num.split("/")[0]
        num2 = num.split("/")[1]
        return int(num2) - int(num1)

    def check_citan(self):
        self.app(resourceId=self.id_res('citan_danci')).click()

        self.app(resourceId=self.id_res('citan_item_start_btn')).click()
        self.app.xpath("//*[@text='确认']").click()

        self.app(resourceId=self.id_res('item_submit')).click()
        self.app.xpath("//*[@text='确认']").click()

    def get_citan_cishu(self):
        shengyu = self.app(resourceId=self.id_res(
            'citan_shengyu_cishu')).get_text()
        zong = self.app(resourceId=self.id_res('citan_zong_cishu')).get_text()
        return int(zong) - int(shengyu)

    def id_res(self, id_name):
        return self.config_dc["jiuyin_pkg_name"] + ":id/" + id_name

    def close(self):
        self.app.close()
