from selenium.webdriver.common.by import By

from utils import UtilsDriver,find_element_wait


class BasePage:

    def __init__(self):
        self.driver = UtilsDriver.get_driver()   #由于有类方法,所以不用实例化类对像就可以调用get_driver函数


    def find_element(self,xpath_str):
        return find_element_wait(self.driver,(By.XPATH,xpath_str))
