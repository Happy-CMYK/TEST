from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# webdriver 获取浏览器的对象
driver = webdriver.Chrome()

# 准备一个网址

# https://www.baidu.com/
url = "https://www.baidu.com/"

driver.get(url)

el = driver.find_element("id","kw")
# 输入python

el.send_keys("python")
sleep(2)
# 全选
el.send_keys(Keys.CONTROL,"a")
sleep(2)
# 删除
el.send_keys(Keys.BACKSPACE)
sleep(2)
# 输入美女
el.send_keys("美女")
sleep(5)
# 全选
el.send_keys(Keys.CONTROL,"a")
sleep(5)
# 复制
el.send_keys(Keys.CONTROL,"c")
sleep(5)

el.send_keys(Keys.CONTROL,"v")
sleep(5)



# 回收资源
driver.quit()