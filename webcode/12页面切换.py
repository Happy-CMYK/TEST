from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# webdriver 获取浏览器的对象
driver = webdriver.Chrome()

# 准备一个网址

# https://www.baidu.com/
url = "https://www.baidu.com/"
driver.get(url)
driver.maximize_window()
sleep(1)

print(driver.window_handles)
print(driver.current_window_handle)

driver.find_element("id","kw").send_keys("美女")
sleep(2)
driver.find_element("id","su").click()
sleep(2)
driver.find_element("xpath","//*[@id='1']/div/div[1]/div/div[1]/a[1]/img").click()

sleep(1)
print(driver.window_handles)
print(driver.current_window_handle)

sleep(1)
# driver.close()


# 索引从0开始，所以第一个窗口的索引是0，第二个窗口的索引是1，以此类推
driver.switch_to.window(driver.window_handles[1])
# By XPATH = "xpath"
sleep(3)
driver.find_element("xpath",'//*[@id="currentImg"]').click()

sleep(5)
driver.get_screenshot_as_file("img.png")
print(driver.title)
print ( driver.current_url )

sleep(2)

# 回收资源
driver.quit()





