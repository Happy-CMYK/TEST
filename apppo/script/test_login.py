import pytest
from page.login_page import LoginProxy
from page.mine_page import MineProxy
from utils import UtilsDriver

from apppo.utils import read_username_excel


class Test_Login:

    def setup_class(self):
        self.mine = MineProxy()
        self.login = LoginProxy()
        self.driver = UtilsDriver.get_driver ()
        self.mine.goto_login_page()
        pass


    def teardown_class(self):
        UtilsDriver.quit_driver()
        pass

    @pytest.mark.parametrize ( ["username", "pwd" ], read_username_excel () )
    def test_username(self,username,pwd):
        self.login.login(username,pwd)
