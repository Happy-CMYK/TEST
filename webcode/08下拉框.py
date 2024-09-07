from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
# webdriver 获取浏览器的对象
driver = webdriver.Chrome()

# 准备一个网址

# https://www.baidu.com/
# url = "https://www.baidu.com/"

url = "file:///C:/Users/ROY/Desktop/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/selenium/%E6%B3%A8%E5%86%8CA.html"

driver.get(url)

# driver.find_element("id","selectA").se

select = Select(driver.find_element("id","selectA"))
sleep(2)
select.select_by_index(3)
sleep(2)
select.select_by_value("bj")
sleep(2)
select.select_by_visible_text("A广州")


sleep(5)



# 回收资源
driver.quit()