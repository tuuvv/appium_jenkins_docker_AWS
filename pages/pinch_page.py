from commons.mobile_driver_handler import MobileDriverHandle
from locators.main_page_locators import mainPageLocators
from locators.drop_and_drag_locators import dropDrags
import time


class Pinch:

    def __init__(self):
        self.main_page_locators = mainPageLocators()
        self.drop_and_drag_locators = dropDrags()
        self.driver_handler = MobileDriverHandle()

    def load_page(self):
        print('User is on "main" page')
        time.sleep(5)

    def sroll_to_label(self, tolabel):
        self.driver_handler.CrollView_Click(tolabel)
        time.sleep(5)

    def pinch_out(self):
        try:
            self.driver_handler.pinch_out_element()
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking drop and drag button -->", e)

    def pinch_in(self):
        try:
            self.driver_handler.pinch_in_element()
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking drop and drag text -->", e)
