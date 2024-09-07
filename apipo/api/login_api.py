import requests


class LoginApi:

    def __init__(self):
        self.url = "http://127.0.0.1/index.php?m=Home&c=User&a=do_login"
        self.code_url = "http://127.0.0.1/index.php?m=Home&c=User&a=verify"
        self.session = requests.session()


    def login(self,username,pwd,code):
        data = {
            "username": username,
            "password": pwd,
            "verify_code": code
        }

        res = self.session.get(self.code_url)
        # 这里面的data就在这个方法里面
        r = self.session.post(self.url, data=data)
        return r




