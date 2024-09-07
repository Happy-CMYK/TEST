"""Fiddler 的手机抓包过程
1）启动 Fiddler，打开菜单栏中的 Tools > Fiddler Options，打开“Fiddler
 Options”对话框：
2）在 Fiddler Options”对话框切换到“Connections”选项卡，然后勾选“Allow
romote computers to connect”后面的复选框，然后点击“OK”按钮
3）在本机命令行输入：ipconfig，找到本机的 ip 地址。
4）打开 android 设备的“设置”->“WLAN”，找到你要连接的网络，在上面长
按，然后选择“修改网络”，弹出网络设置对话框，然后勾选“显示高级选项”
5）在“代理”后面的输入框选择“手动”，在“代理服务器主机名”后面的输入框
输入电脑的 ip 地址，在“代理服务器端口”后面的输入框输入 8888，然后点击“保存”
按钮。
6）然后启动 android 设备中的浏览器，访问百度的首页，在 fiddler 中可以看到完成
的请求和响应数据。"""


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

print(driver.device_time)
print(driver.network_connection)

# driver.set_network_connection(6)
# 休息时间不能超过3秒
time.sleep(2)

driver.open_notifications()

driver.close_app()
driver.quit()


