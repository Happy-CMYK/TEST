from selenium import webdriver
from time import sleep

# webdriver 获取浏览器的对象
driver = webdriver.Chrome()

# 准备一个网址

# https://www.baidu.com/
url = "https://www.baidu.com/"

driver.get(url)

# 最大化浏览器
# driver.maximize_window()
#
# # 设置浏览器 1920* 1080
# # sleep(1)
# # driver.set_window_size(800,600)
# # sleep(2)
# # driver.set_window_position(200,200)
# print(driver.title)
# print(driver.current_url)
# driver.find_element_by_id("kw").send_keys("美女")
# driver.find_element_by_id("su").click()
#
# sleep(2)
# print(driver.title)
# print(driver.current_url)
# # 浏览器后退
# driver.back()
# sleep(2)
# print(driver.title)
# print(driver.current_url)
# # 浏览器 前进
# driver.forward()
#
# sleep(2)
# print(driver.title)
# print(driver.current_url)
#
# # 刷新浏览器
# driver.refresh()
#
# sleep(2)
#
# driver.back()
#
# driver.find_element_by_id("//*[text()='hao123']").click()
#
# sleep(2)
# driver.close()
#
# sleep(5)
#
# # 回收资源
# driver.quit()