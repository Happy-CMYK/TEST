from selenium import webdriver
from time import sleep

# webdriver 获取浏览器的对象
driver = webdriver.Chrome()

# 准备一个网址

# https://www.baidu.com/
url = "https://www.baidu.com/"

driver.get(url)


sleep(5)

# 回收资源
driver.quit()