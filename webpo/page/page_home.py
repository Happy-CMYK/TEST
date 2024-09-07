from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import UtilsDriver
from base.base_page import PageBase


# 对象库层
# 找到页面要使用所有的元素

class PageHome ( PageBase ):

    # def __init__(self):
    #     # self.driver = webdriver.Chrome("./chomedriver.exe")
    #     # utils = UtilsDriver()
    #     # self.driver = utils.get_driver()
    #     self.driver = UtilsDriver.get_driver()

    def find_login_btn(self):
        return self.find_element ( By.CLASS_NAME, "red" )


# 操作层
# 把上面的元素的操作封装起来

class HandleHome:
    def __init__(self):
        self.page = PageHome ()

    def click_login_btn(self):
        self.page.find_login_btn ().click ()


# 业务层
# 上面元素的操作的组合

class ProxyHome:

    def __init__(self):
        self.handle = HandleHome ()

    def goto_login_page(self):
        self.handle.click_login_btn ()
