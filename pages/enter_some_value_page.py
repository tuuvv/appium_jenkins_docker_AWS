from locators.main_page_locators import mainPageLocators
from locators.enter_value_page_locators import enterValueLocators
from commons.mobile_driver_handler import MobileDriverHandle
import time


class EnterSomeValue:

    def __init__(self):

        self.main_page_locators = mainPageLocators()
        self.enter_value_page_locators = enterValueLocators()
        self.driver_handler = MobileDriverHandle()

    def load_page(self):
        print('User is on "main" page')
        time.sleep(3)

    def click_entervalue_btn(self):
        try:
            self.driver_handler.click_element(self.main_page_locators.enter_some_value_btn)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking on login button -->", e)

    def sendkey_value(self, value):
        try:
            self.driver_handler.send_keys(self.enter_value_page_locators.input_id, value)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while sendkeys to input -->", e)