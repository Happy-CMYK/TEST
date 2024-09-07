from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# webdriver 获取浏览器的对象
driver = webdriver.Chrome()

# 准备一个网址

# https://www.baidu.com/
url = "https://www.baidu.com/"

driver.get(url)


# driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("美女")
# sleep(5)
#
# driver.find_element("xpath","//*[@id='su']").click()
#
#
# sleep(5)
#
# # 回收资源
# driver.quit()

# 查找 元素(标签,标记 节点)  通过id
# driver.find_element('id',"kw").send_keys("美女")
# driver.find_element('id',"su").click()

# 通过name查找元素
# driver.find_element('name',"wd").send_keys("美女")

# 通过class name,可以使用"class_name",也可以使用By.CLASS_NAME
driver.find_element("class name","s_ipt").send_keys("美女")
driver.find_element('id',"su").click()

# 定位a标签 link text  partial linktext

# driver.find_element(By.LINK_TEXT,"hao123").click()
#
# driver.find_element(By.LINK_TEXT,"hao123").click()

# 通过css 选择器的方式定位


driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("美女")

driver.find_element(By.CSS_SELECTOR, ".s_ipt").send_keys("美女")
driver.find_element(By.CSS_SELECTOR, "[name=wd]").send_keys("美女")
driver.find_element(By.CSS_SELECTOR, "[value=百度一下]").click()

# 3q  xpath  xxxxxxxl
# 通过xpath的方式进行定位



# find_element_by_xpath 此类方法被禁用了(即所谓的公共方法)

