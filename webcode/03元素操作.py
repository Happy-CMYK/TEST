from selenium import webdriver
from time import sleep

# webdriver 获取浏览器的对象
driver = webdriver.Chrome()

# 准备一个网址

# https://www.baidu.com/
url = "https://www.baidu.com/"

driver.get(url)

# driver.find_element("id","kw").send_keys("python")

# sleep(3)
# 清除输入的文字
# driver.find_element("id","kw").clear()
#
# driver.find_element("id","kw").send_keys("美女")
#
# driver.find_element("id","su").click()
print(driver.find_element("id","kw").size)
print(driver.find_element("id","kw").text)
print(driver.find_element("id","kw").is_enabled())
print(driver.find_element("id","kw").is_displayed())

print(driver.find_element("xpath","//*[text()='新闻']").get_attribute("href"))

sleep(5)

# 回收资源
driver.quit()