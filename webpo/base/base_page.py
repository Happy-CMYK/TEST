from utils import UtilsDriver,find_element_wait
class PageBase:
    def __init__(self):
        self.driver = UtilsDriver.get_driver()

    def find_element(self,by_el,by_value):

        return find_element_wait(self.driver, by_el,by_value,5)