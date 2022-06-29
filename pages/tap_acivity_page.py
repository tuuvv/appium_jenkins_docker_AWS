from commons.mobile_driver_handler import MobileDriverHandle
from locators.main_page_locators import mainPageLocators
from locators.tap_activity_locators import TapLocators
import time


class TapAcivity:

    def __init__(self):
        self.main_page_locators = mainPageLocators()
        self.tap_activity_locators = TapLocators()
        self.driver_handler = MobileDriverHandle()

    def load_page(self):
        print('User is on "main" page')
        time.sleep(3)

    def tap_btn(self):
        try:
            self.driver_handler.tap_element(self.main_page_locators.tap_btn)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while tap on button -->", e)

    def tap_on_sport_tab(self):
        try:
            self.driver_handler.tap_element(self.tap_activity_locators.sport_xpath)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while tap on button -->", e)

    def tap_on_movie_tab(self):
        try:
            self.driver_handler.tap_element(self.tap_activity_locators.movie_xpath)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while tap on button -->", e)

    def swipe_right_to_left(self):
        try:
            self.driver_handler.swipe_right_to_left_element()
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while tap on button -->", e)

    def swipe_left_to_right(self):
        try:
            self.driver_handler.swipe_left_to_right_element()
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while tap on button -->", e)