from selenium import webdriver
from time import sleep
import time

# 显示等待
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge ()
driver.maximize_window ()
driver.get ( 'http://www.baidu.com' )
driver.find_element ( 'id', 'kw' ).send_keys ( u'selenium 灰蓝' )
driver.find_element ( 'id', 'su' ).click ()
time.sleep ( 10 )
# print(driver.current_url)

# 显示等待
# WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.ID,"aging-total-page")))
# driver.find_element('id',"aging-total-page").click()
# driver.back()  # back
# print(driver.current_url)


# 隐式等待
driver.implicitly_wait ( 5 )
driver.find_element ( 'id', "1" ).click ()
# print(driver.current_url)

# driver.forward()  # forward
# print(driver.current_url)
# driver.refresh()  # refresh
# print(driver.current_url)
# driver.back()  # back
# print(driver.current_url)
# driver.forward()  # forward
# print(driver.current_url)

sleep ( 2 )
driver.quit ()
