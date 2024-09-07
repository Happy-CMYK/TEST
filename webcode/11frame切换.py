

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# webdriver 获取浏览器的对象
driver = webdriver.Chrome()
# 准备一个网址
# https://www.baidu.com/
url = "https://mail.qq.com/"
driver.maximize_window ()
driver.get ( url )
sleep ( 2 )
# 切换frame界面
frame1=driver.find_element_by_css_selector('#QQMailSdkTool_login_loginBox_qq > iframe')
driver.switch_to.frame(frame1)
sleep ( 2)

frame2=driver.find_element_by_id('ptlogin_iframe')
driver.switch_to.frame(frame2)

sleep ( 2)
driver.find_element_by_id('img_out_1835863496').click()
sleep(8)


driver.switch_to.default_content ()
driver.quit()

