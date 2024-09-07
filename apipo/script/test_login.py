from api.login_api import LoginApi
from utils import RequestUtils,read_testcase_yaml
import pytest

class Test_Login:

    def setup_method(self):
        self.login_api = LoginApi()

    @pytest.mark.parametrize("caseinfo",read_testcase_yaml("./data/login.yml"))
    def test_login(self,caseinfo):
        # r = self.login_api.login("13832123321","123123","8888")
        # assert r.status_code == 200
        # assert "登录成功" in r.json()["msg"]
        RequestUtils().hanle_yaml(caseinfo)


     #  后端:  r = self.login_api.login("admin","123456","8888")