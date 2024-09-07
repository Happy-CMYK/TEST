from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}

# 系统的名称
desired_caps["platformName"] = "Android"
# 系统的版本
desired_caps["platformVersion"] = "7.1"

# 设备的名称
desired_caps["deviceName"] = "127.0.0.1:62001"

# 要测试那个app
desired_caps["appPackage"] = "com.android.settings"

# 要测试app的界面的id
desired_caps["appActivity"] = ".Settings"

driver = webdriver.Remote ( "http://127.0.0.1:4723/wd/hub", desired_caps )

el1 = driver.find_element_by_xpath ( "//*[@text='声音']" )
el2 = driver.find_element_by_xpath ( "//*[@text='蓝牙']" )
driver.scroll ( el1, el2 )

time.sleep ( 1 )
driver.find_element_by_xpath ( "//*[@text='安全']" ).click ()
time.sleep ( 1 )
driver.find_element_by_xpath ( "//*[@text='屏幕锁定']" ).click ()
time.sleep ( 1 )
driver.find_element_by_xpath ( "//*[@text='图案']" ).click ()
# 休息时间不能超过3秒
time.sleep ( 2 )
# print(driver.network_connection)
# driver.set_network_connection(6)
x = 180
y = 774
delta = 272

action = TouchAction ( driver )
action.press ( x=x, y=y ).wait ( 1000 )
action.move_to ( x=x + 2 * delta, y=y )
action.move_to ( x=x, y=y + 2 * delta )
action.move_to ( x=x + 2 * delta, y=y + 2 * delta )
action.release ()

# 必须要加上perform
action.perform ()

time.sleep ( 2 )

driver.close_app ()
driver.quit ()
