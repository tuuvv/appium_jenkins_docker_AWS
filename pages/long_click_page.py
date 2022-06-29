from commons.mobile_driver_handler import MobileDriverHandle
from locators.main_page_locators import mainPageLocators
from locators.crollview_page_locators import crollViewLocators
import time


class LongClick:

    def __init__(self):
        self.main_page_locators = mainPageLocators()
        self.crollview_page_locators = crollViewLocators()
        self.driver_handler = MobileDriverHandle()

    def load_page(self):
        print('User is on "main" page')
        time.sleep(3)

    def longclick_btn(self):
        try:
            self.driver_handler.longclick_element(self.main_page_locators.longclick_btn)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking on login button -->", e)
