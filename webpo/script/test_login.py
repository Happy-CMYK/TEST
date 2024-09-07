from page.page_login import ProxyLogin
from page.page_home import ProxyHome
from utils import UtilsDriver, find_login_msg, read_username_excel,get_logger
import pytest
import allure


@allure.feature ( "登录测试" )
class Test_Login:


    # 运行log
    def setup_class(self):
        self.logger=get_logger("login_log")

    def setup_method(self):
        self.login = ProxyLogin ()
        self.home = ProxyHome ()
        self.driver = UtilsDriver.get_driver ()
        self.driver.get ( "http://127.0.0.1/" )
        self.home.goto_login_page ()
        pass

    def teardown_method(self):
        UtilsDriver.quit_driver ()
        pass

    @allure.story ( "登录用户名异常数据测试" )
    @allure.severity ( allure.severity_level.CRITICAL )
    @pytest.mark.parametrize ( ["username", "pwd", "code", "ast_msg"], read_username_excel () )
    def test_username_error(self, username, pwd, code, ast_msg):
        with allure.step ( "输入数据并且登录" ):
            self.login.goto_login ( username, pwd, code )

        with allure.step ( "获取实际结果" ):
            msg = find_login_msg ()

        # 得到log
        self.logger.info(f"这次测试的数据是{username},{pwd},{code},预期结果是{ast_msg},实际结果是{msg}")

        assert ast_msg in msg

