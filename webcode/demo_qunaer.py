from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome ()
url = "https://www.qunar.com/"
driver.get ( url )
driver.maximize_window ()
driver.implicitly_wait ( 5 )
action = ActionChains ( driver )

# 进入“火车票”栏
driver.find_element_by_xpath ( "//*[@id='js_nva_cgy']/li[3]" ).click ()
time.sleep ( 2 )
# 始发站“北京”
driver.find_element_by_name ( "fromStation" ).send_keys ( "北京" )
time.sleep ( 1 )
# 点击空白处
action.move_by_offset ( 0, 0 )
action.click ()
action.perform ()
# 到达站“济南”
driver.find_element_by_name ( "toStation" ).send_keys ( "济南" )
time.sleep ( 2 )
# 点击空白处
action.move_by_offset ( 0, 0 )
action.click ()
action.perform ()
# 定位到“日期”
el_date = driver.find_element_by_name ( "date" )
# 两种删除方法：
# for i in "2022-05-22":
#     el_date.send_keys(Keys.BACKSPACE)
el_date.send_keys ( Keys.CONTROL, "a" )
el_date.send_keys ( Keys.BACKSPACE )

time.sleep ( 1 )
# 输入日期
el_date.send_keys ( "2022-05-22" )
time.sleep ( 2 )
# 点击空白处
action.move_by_offset ( 0, 0 )
action.click ()
action.perform ()
# 点击“查询”
time.sleep ( 2 )
driver.find_element_by_name ( "stsSearch" ).click ()

# 点击购买
driver.find_element_by_xpath ( "//*[@id='list_listInfo']/ul[2]/li[2]/div/div[7]/a[1]/span" ).click ()
driver.implicitly_wait ( 8 )

# 输入姓名，身份证
driver.find_element_by_name ( "contact_name" ).send_keys ( "张三" )
driver.find_element_by_name ( "contact_phone" ).send_keys ( "132809199806011427" )

time.sleep ( 4 )
driver.quit ()  # 退出



# 下一步的封装操作

from datetime import date, datetime, timedelta


# n是第几天，n=1 明天，n=2 后天
def date_n(n):
    # 今天的日期+偏移量
    return str ( date.today () + timedelta ( days=int ( n ) ) )


# 设置出发日期 n从今天往后的第几天
date_1 = date_n ( 2 )


# print(date_1)


# 封装
def name(element):
    return driver.find_element ( By.NAME, element )


def xpath(element):
    return driver.find_element ( By.XPATH, element )
