from selenium import webdriver
from time import sleep

# webdriver 获取浏览器的对象
driver = webdriver.Chrome()

# 准备一个网址

# https://www.baidu.com/
# url = "https://www.baidu.com/"

url = "file:///C:/Users/ROY/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/selenium/css_example.html"

driver.get(url)

sleep(2)
driver.find_element("xpath","/html/body/input[1]").click()

# 警告框 切换到警告框 然后操作警告框

alert = driver.switch_to.alert

print(alert.text)
alert.dismiss()

sleep(5)

# 回收资源
driver.quit()
driver.close()