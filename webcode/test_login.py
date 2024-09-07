from selenium import webdriver
import time


class Test_login:

    def setup_method(self):
        self.driver = webdriver.Chrome ()

        url = "http://127.0.0.1/"
        self.driver.get ( url )
        self.driver.maximize_window ()

        self.driver.find_element_by_class_name ( "red" ).click ()

    def teardown_method(self):
        time.sleep ( 2 )
        self.driver.close ()
        self.driver.quit ()

    def test_username(self):
        # 寻找元素的时候最好也要给个隐式等待(元素可能会变)
        self.driver.implicitly_wait ( 5 )
        self.driver.find_element_by_id ( "username" ).send_keys ( "1388888888" )
        self.driver.find_element_by_id ( "password" ).send_keys ( "123456" )
        self.driver.find_element_by_id ( "verify_code" ).send_keys ( "8888" )

        self.driver.find_element_by_name ( "sbtbutton" ).click ()

        self.driver.implicitly_wait ( 5 )
        res = self.driver.find_element_by_class_name ( "layui-layer-content" ).text
        assert "账号格式不匹配" in res

    # 这个就相当于第二个,打开浏览器运行他并关闭
    def test_password(self):
        pass





