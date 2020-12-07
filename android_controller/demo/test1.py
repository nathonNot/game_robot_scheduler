import uiautomator2 as u2

d = u2.connect_adb_wifi("172.16.2.12")
print(d.info)
app = d.session("com.woniu.mobile9yin") # 启动应用并获取session
app(resourceId = 'com.woniu.mobile9yin:id/et_name').click()
app.send_keys("")
app(resourceId = 'com.woniu.mobile9yin:id/et_pwd').click()
app.send_keys("")
app(resourceId = 'com.woniu.mobile9yin:id/signin_button').click()
app.xpath("//*[@text='江湖六区']").click()
app.xpath("//*[@text='气贯长虹']").click()
app(resourceId = 'com.woniu.mobile9yin:id/citan_btn').click()
app(resourceId = 'com.woniu.mobile9yin:id/item_citan_btn').click()

app(resourceId = 'com.woniu.mobile9yin:id/citan_danci').click()
print(app(resourceId = 'com.woniu.mobile9yin:id/tangmen_jd').info)

app(resourceId = 'com.woniu.mobile9yin:id/citan_jingyewei').click()

app(resourceId = 'com.woniu.mobile9yin:id/citan_danci').click()

app(resourceId = 'com.woniu.mobile9yin:id/citan_item_start_btn').click()

app.xpath("//*[@text='确认']").click()

app(resourceId = 'com.woniu.mobile9yin:id/item_submit').click()

app.xpath("//*[@text='确认']").click()
# xml = app.dump_hierarchy()

def can_citan(app,button):
    pass