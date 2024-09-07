# 第一阶段

# import time
# from time import sleep
#
# from selenium.webdriver import ActionChains
# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
#
#
# driver = webdriver.Chrome ()
# driver.get ( "https://www.163.com/" )
# driver.maximize_window ()
#
# sleep ( 0.5 )
#
# ActionChains ( driver ).move_to_element ( driver.find_element_by_class_name ( 'ntes-nav-login-title' ) ).perform ()
#
# driver.switch_to.frame ( 1 )
#
#
#
# driver.find_element_by_xpath ( '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]' ).click ()
# driver.find_element_by_name ( 'email' ).send_keys ( '1223sss212@163.com' )
# driver.find_element_by_name ( 'password' ).send_keys ( '1223sss212@163.com' )
# driver.find_element_by_name ( 'mailclause' ).click ()
# driver.find_element_by_id ( 'dologin' ).click ()
#
# driver.quit ()
# driver.close ()





# 第二阶段

import time
from time import sleep

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver



class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.163.com/')
        self.driver.maximize_window()

    def login(self, email, password):
        try:
            ActionChains ( self.driver ).move_to_element (
            self.driver.find_element_by_class_name ( 'ntes-nav-login-title' ) ).perform ()

            self.driver.switch_to.frame ( 1 )
            self.driver.find_element_by_xpath ( '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]' ).click ()

            self.driver.find_element_by_name ( 'email' ).send_keys ( email )
            self.driver.find_element_by_name ( 'password' ).send_keys ( password )
            # Click on the mail clause button
            self.driver.find_element_by_name ( 'mailclause' ).click ()

            # Click on the login button
            self.driver.find_element_by_id ( 'dologin' ).click ()

        except Exception as e:
            print ( f"An error occurred: {e}" )

login=LoginPage()
login.login('msmsmsm','kskskks')
login.driver.quit()
login.driver.close()



# 第三阶段



