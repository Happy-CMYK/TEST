
from appium import webdriver
import time

desired_caps = {}

# 系统的名称
desired_caps["platformName"] = "Android"
# 系统的版本
desired_caps["platformVersion"] = "7.1"

# 设备的名称
desired_caps["deviceName"] ="127.0.0.1:62001"

# 要测试那个app
desired_caps["appPackage"] = "com.android.settings"

# 要测试app的界面的id
desired_caps["appActivity"]= ".Settings"


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
print(r"你好\n世界")

if driver.is_app_installed("com.anneng.watchproject"):
    driver.remove_app("com.anneng.watchproject")
else:
    driver.install_app(r"C:\Users\ROY\PycharmProjects\appcode\WatchAppKt_v1.0.2.0_release.apk")
driver.install_app(r"C:\Users\ROY\PycharmProjects\appcode\WatchAppKt_v1.0.2.1_release.apk")

# driver.remove_app("tv.danmaku.bili")

# with open("aaa.xml","w",encoding="utf8") as f:
#     f.write(driver.page_source)
time.sleep(2)
driver.find_element_by_xpath("//*[@text='ACVOR']").click()

# <a name="哈哈哈"/>
# 休息时间不能超过3秒
time.sleep(10)

driver.close_app()
driver.quit()