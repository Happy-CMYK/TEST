from appium import webdriver
import time

desired_caps = {}

# 系统的名称
desired_caps["platformName"] = "Android"

# 系统的版本   获取手机android版本 adb shell getprop ro.build.version.release
desired_caps["platformVersion"] = "7.1"

# 设备的名称   获取设备的名称 adb devices
desired_caps["deviceName"] = "127.0.0.1:62001"

# 要测试那个app  获取手机当前运行的程序(包名)和界面的名称 adb shell dumpsys window windows | findstr mFocusedApp
desired_caps["appPackage"] = "com.android.settings"

# 要测试app的界面的id
desired_caps["appActivity"] = ".Settings"

driver = webdriver.Remote ( "http://127.0.0.1:4723/wd/hub", desired_caps )

# 休息时间不能超过3秒!!! 要不然就有可能断开连接
time.sleep ( 2 )

driver.close_app ()
driver.quit ()
