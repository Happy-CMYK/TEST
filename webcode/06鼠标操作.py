from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# 'by import' 后首字母要大写
# webdriver 获取浏览器的对象
driver = webdriver.Chrome()

url=r"file:///C:/Users/ROY/OneDrive/Study/web-test/selenium/drag.html"
driver.get(url)

sleep(2)



action = ActionChains(driver)
# 点击右键
action.context_click(driver.find_element("id","div1"))

# 拖拽
action.drag_and_drop(driver.find_element("id","div1"),driver.find_element("id","div2"))

# 事件操作必须要执行!!!!!!!!!!!!!!!!
action.perform()

sleep(5)

# 回收资源
driver.quit()


