from commons.mobile_driver_handler import MobileDriverHandle
from locators.main_page_locators import mainPageLocators
from locators.crollview_page_locators import crollViewLocators
import time


class CrollView:

    def __init__(self):
        self.main_page_locators = mainPageLocators()
        self.crollview_page_locators = crollViewLocators()
        self.driver_handler = MobileDriverHandle()

    def load_page(self):
        print('User is on "main" page')
        time.sleep(10)

    def click_crollview_btn(self):
        try:
            self.driver_handler.click_element(self.main_page_locators.crollview_btn)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking on login button -->", e)

    def CrollView_to_label(self, tolabel):
        try:
            self.driver_handler.CrollView_Click(tolabel)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while crollview to label -->", e)

    def click_yes_btn(self):
        try:
            self.driver_handler.click_element(self.crollview_page_locators.yes_btn)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking on yes button -->", e)