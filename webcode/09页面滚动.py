from selenium import webdriver
from time import sleep

# webdriver 获取浏览器的对象
driver = webdriver.Chrome()

# 准备一个网址

# https://www.baidu.com/
url = "https://www.douyu.com/"

driver.get(url)
driver.maximize_window()
sleep(10)
# 界面滚动操作
js_str="window.scrollTo(0,10000)"

driver.execute_script(js_str)

sleep(5)
driver.find_element("xpath","//*[text()='直播']").click()
#
# sleep(2)
# driver.find_element("xpath","//*[text()='下一页']").click()

sleep(5)

# 回收资源
# driver.close()
driver.quit()



