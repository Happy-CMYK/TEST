from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time

from selenium.webdriver.common.by import By
import xlrd
import logging
import logging.handlers

class UtilsDriver:
    # 单例设计模式  同一时间只能有一个实例

    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()

        return cls.driver


    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.get_driver().close()
            cls.get_driver().quit()
            cls.driver = None

def find_login_msg():
    # UtilsDriver.get_driver().implicitly_wait(5)
    # el = UtilsDriver.get_driver().driver.find_element_by_class_name("layui-layer-content")
    el = find_element_wait(UtilsDriver.get_driver(),By.CLASS_NAME,"layui-layer-content")
    msg =el.text
    return msg
# 设置一个最大等待时间 比如5秒
# 每隔0.x秒去检查一次
# 如果找到就继续
# 如果没找到就继续找
# 如果最大等待时间还没找到 直接报错

def find_element_wait(driver: WebDriver,by_sm,by_value,num = 5):

    ctime = time.time()
    while True:
        time.sleep(0.2)
        try:
            return driver.find_element(by_sm,by_value)
        except:
            print("没找着")

        if time.time()>ctime+num:
            break

    return driver.find_element(by_sm,by_value)

# 加载测试数据
# [("138888888","123456","8888","账号格式不匹配"),("138888888","123456","8888","账号格式不匹配")]

def read_username_excel():
    excel = xlrd.open_workbook("./data/login_username_error.xlsx")
    sheet = excel.sheet_by_index(0)
    datas = []
    for i in range(sheet.nrows):
        datas.append(tuple(sheet.row_values(i)[:-1]))

    return datas[1:]



def get_logger(name):
    logger = logging.getLogger(name)
    # 2、设置日志器级别
    logger.setLevel(logging.DEBUG)
    # 3、创建两个处理器（输出到控制台以及输出到文件）
    # 3.1 创建输出到控制台的处理器
    sf = logging.StreamHandler()
    # 3.2 创建输出到文件的处理器
    hf = logging.handlers.TimedRotatingFileHandler("log/log.log", when='M',interval=1, backupCount=0,encoding="utf8")
    # 4、设置级别
    sf.setLevel(logging.INFO)
    hf.setLevel(logging.INFO)
    # 5、创建格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)
    # 6、添加格式器到处理器当中
    sf.setFormatter(formatter)
    hf.setFormatter(formatter)
    # 7、将处理器添加到日志器
    logger.addHandler(sf)
    logger.addHandler(hf)
    return logger



if __name__ == '__main__':
    print(read_username_excel())