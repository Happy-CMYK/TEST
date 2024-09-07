from selenium import webdriver


from selenium.webdriver.common.by import By

from base.base_page import PageBase
from utils import UtilsDriver



# 对象库层
# 找到页面要使用所有的元素
class PageLogin ( PageBase ):

    # def __init__(self):
    #     # self.driver = webdriver.Chrome("./chomedriver.exe")
    #     # utils = UtilsDriver()
    #     # self.driver = utils.get_driver()
    #     self.driver = UtilsDriver.get_driver()

    def find_login_btn(self):
        # return self.driver.find_element_by_name("sbtbutton")
        return self.find_element( By.NAME, "sbtbutton" )

    def find_username(self):
        # return self.driver.find_element_by_id("username")
        return self.find_element ( By.ID, "username" )

    def find_pwd(self):
        # return self.driver.find_element_by_id("password")
        return self.find_element ( By.ID, 'password' )

    def find_code(self):
        # return self.driver.find_element_by_id("verify_code")
        return self.find_element ( By.ID, "verify_code" )


# 操作层
# 把上面的元素的操作封装起来

class HandleLogin:
    def __init__(self):
        self.page = PageLogin ()

    def click_login_btn(self):
        self.page.find_login_btn ().click ()

    def input_username(self, username):
        self.page.find_username ().send_keys ( username )

    def input_pwd(self, pwd):
        self.page.find_pwd ().send_keys ( pwd )

    def input_code(self, code):
        self.page.find_code ().send_keys ( code )


# 业务层
# 上面元素的操作的组合

class ProxyLogin:

    def __init__(self):
        self.handle = HandleLogin ()

    def goto_login(self, username, pwd, code):
        self.handle.input_username ( username )
        self.handle.input_pwd ( pwd )
        self.handle.input_code ( code )
        self.handle.click_login_btn ()
