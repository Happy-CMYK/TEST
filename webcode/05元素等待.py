from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# webdriver 获取浏览器的对象
driver = webdriver.Chrome()

# 准备一个网址

# https://www.baidu.com/
url = "https://www.baidu.com/"

driver.get(url)

# 输入框输入要搜索的内容 美女
driver.find_element("id","kw").send_keys("美女")
# 点击百度一下
driver.find_element("id","su").click()
# 点击一个搜索到的条目

# 代码的执行速度 远远快与页面的加载速度的
# 在翻页的时候 或者是在加载我们新的页面的时候 需要进行页面等待
# 页面等待的方式有三种
# 强制等待
# 显式等待
# 隐式等待

# 强制等待
# sleep(3)
# 显式等待
# 等待某个元素加载完成  每个0.5秒去检查一次 最多等待5秒时间
# WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"1")))

# 隐式等待
driver.implicitly_wait(5)
driver.find_element("id","1").click()

sleep(5)

# 回收资源
driver.quit( )