
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

# el1 = driver.find_element_by_xpath("//*[@text='声音']")
# el2 = driver.find_element_by_xpath("//*[@text='蓝牙']")
# driver.scroll(el1,el2)

size = driver.get_window_size()
# print(size)
width = size["width"]
height = size["height"]
time.sleep(2)

x = width//2
y = int(height/4)

driver.swipe(start_x=x,start_y=y*3,end_x=x,end_y=y,duration=1500)
# 休息时间不能超过3秒
time.sleep(3)

driver.close_app()
driver.quit()