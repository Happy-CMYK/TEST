import time

import xlrd
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class UtilsDriver:
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            desired_caps = {}

            # 系统的名称
            desired_caps["platformName"] = "Android"
            # 系统的版本
            desired_caps["platformVersion"] = "7.1"

            # 设备的名称
            desired_caps["deviceName"] = "127.0.0.1:62001"

            # 要测试那个app
            desired_caps["appPackage"] = "io.manong.developerdaily"

            # 要测试app的界面的id
            desired_caps["appActivity"] = "io.toutiao.android.ui.activity.MainActivity"

            cls.__driver = webdriver.Remote ( "http://127.0.0.1:4723/wd/hub", desired_caps )
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            cls.get_driver ().close_app ()
            cls.get_driver ().quit ()
            cls.__driver = None


def find_element_wait(driver: WebDriver, value, num=5):
    ctime = time.time ()

    while time.time () < ctime + num:
        time.sleep ( 1 )
        try:
            WebDriverWait ( driver, 5 ).until ( EC.presence_of_element_located ( ("xpath", '//*[@text="好的"]') ) )
            driver.find_element ( "xpath", "//*[@text='好的']" ).click ()
            WebDriverWait ( driver, 5 ).until ( EC.presence_of_element_located ( ("xpath", '//*[@text="允许"]') ) )
            driver.find_element ( "xpath", "//*[@text='允许']" ).click ()
            WebDriverWait ( driver, 5 ).until ( EC.presence_of_element_located ( ("xpath", '//*[@text="允许"]') ) )
            driver.find_element ( "xpath", "//*[@text='允许']" ).click ()
            return driver.find_element ( *value )
        except:
            pass


        return driver.find_element ( *value )




def read_username_excel():
    excel = xlrd.open_workbook("./data/login_username_error.xlsx")
    sheet = excel.sheet_by_index(0)
    datas = []
    for i in range(sheet.nrows):
        datas.append(tuple(sheet.row_values(i)[:-1]))

    return datas[1:]


if __name__ == '__main__':
    print(read_username_excel())



