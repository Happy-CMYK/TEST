from base.base_page import BasePage





class PageMine(BasePage):
    def find_mine_btn(self):
        return self.find_element("//*[@text='我的']")

    def find_login_btn(self):
        return self.find_element("//*[@text='登录/注册']")


class HandleMine:
    def __init__(self):
        self.page = PageMine()

    def click_mine_btn(self):
        self.page.find_mine_btn().click()

    def click_login_btn(self):
        self.page.find_login_btn().click()

class MineProxy:
    def __init__(self):
        self.handle = HandleMine()

    def goto_login_page(self):
        self.handle.click_mine_btn()
        self.handle.click_login_btn()