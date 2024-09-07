import time
from appium import webdriver
# server 启动参数
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

desired_caps = {}
# 1.安卓系统
desired_caps['platformName'] = 'Android'
# 2.系统的版本号
desired_caps['platformVersion'] = '7.1'
# 3.手机名称，可通过命令：adb devices获取
desired_caps['deviceName'] = '127.0.0.1:62001'
# 4.应用程序的包名，也是app的包名，在手机中，包名是app的唯一标识
# 获取手机当前运行的程序和界面的名称
# adb shell dumpsys window windows | findstr mFocusedApp
desired_caps['appPackage'] = 'com.android.launcher3'
# 5.当前app里面的界面内容
desired_caps['appActivity'] = '.launcher3.Launcher'
# 从appium库里面导入driver对象
# driver = webdriver.Remote('appium程序的地址','一个字典，要获取设置的要求')
driver = webdriver.Remote ( 'http://127.0.0.1:4723/wd/hub', desired_caps )
time.sleep ( 10 )

# 点击抖音
driver.find_element ( "xpath", "//*[@text='抖音']" ).click ()
size = driver.get_window_size ()
print ( size )
width = size["width"]
height = size["height"]
time.sleep ( 5 )
for i in range(100):
    # 模拟向上滑动
    start_x = width // 2
    start_y = height // 4 * 3
    end_x = width // 2
    end_y = height // 4
    driver.swipe(start_x, start_y, end_x, end_y, 1000)
    time.sleep ( 4 )
    try:
        WebDriverWait ( driver, 10 ).until ( EC.presence_of_element_located ( ("xpath", '//*[@text="同意"]') ) )
        driver.find_element ( "xpath", "//*[@text='同意']" ).click ()

    except:
        pass
time.sleep ( 2 )
# el1 = driver.find_element("xpath","//*[@text='通知']")
# el2 = driver.find_element("xpath","//*[@text='WLAN']")
# time.sleep(2)
# driver.drag_and_drop(el1,el2)


time.sleep ( 2 )

driver.quit ()





