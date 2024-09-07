from base.base_page import BasePage


class PageLogin(BasePage):
    def find_email_btn(self):
        return self.find_element("//*[@resource-id='io.manong.developerdaily:id/btn_email']")


    def find_email(self):
        return self.find_element("//*[@text='请输入登录邮箱']")

    def find_pwd(self):
        return self.find_element("//*[@text='请输入密码']")

    def find_login_btn(self):
        return self.find_element("//*[@text='登录']")


class HandleLogin:
    def __init__(self):
        self.page = PageLogin()

    def click_email_btn(self):
        self.page.find_email_btn().click()

    def input_email(self,email):
        self.page.find_email().send_keys(email)

    def input_pwd(self,pwd):
        self.page.find_pwd().send_keys(pwd)

    def click_login_btn(self):
        self.page.find_login_btn().click()


class LoginProxy:
    def __init__(self):
        self.handle = HandleLogin()

    def login(self,email,pwd):
        self.handle.click_email_btn()
        self.handle.input_email(email)
        self.handle.input_pwd(pwd)
        self.handle.click_login_btn()
