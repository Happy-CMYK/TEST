from selenium import webdriver
import time


driver = webdriver.Chrome()

url = "http://127.0.0.1/"
driver.get(url)
driver.maximize_window()

driver.find_element_by_class_name("red").click()

driver.implicitly_wait(5)
driver.find_element_by_id("username").send_keys("13705221753")
driver.find_element_by_id("password").send_keys("123123")
driver.find_element_by_id("verify_code").send_keys("8888")

driver.find_element_by_name("sbtbutton").click()


time.sleep(2)

driver.close()
driver.quit()

# 1.如果测试代码报错会倒是程序失败
# 2.不能让所有的测试脚本 自动运行
# 3.测试完成以后需要测试的结果 pass fail



