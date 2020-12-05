import uiautomator2 as u2

d = u2.connect_adb_wifi("172.16.2.12")
print(d.info)
d.app_start("com.woniu.mobile9yin")

d(resourceId = 'com.woniu.mobile9yin:id/et_name').click()