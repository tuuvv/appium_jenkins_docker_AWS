from commons.mobile_driver_handler import MobileDriverHandle
from locators.main_page_locators import mainPageLocators
from locators.drop_and_drag_locators import dropDrags
import time


class DropDrag:

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

    def drop_drag_picture(self):
        try:
            self.driver_handler.drag_drop_element(self.drop_and_drag_locators.image_id, self.drop_and_drag_locators.midle_part_id)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking drop and drag button -->", e)

    def drop_drag_text(self):
        try:
            self.driver_handler.drag_drop_element(self.drop_and_drag_locators.text_id, self.drop_and_drag_locators.last_part_id)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking drop and drag text -->", e)

    def drop_drag_btn(self):
        try:
            self.driver_handler.drag_drop_element(self.drop_and_drag_locators.button_id, self.drop_and_drag_locators.last_part_id)
            time.sleep(3)
        except Exception as e:
            raise Exception("Exception occured while clicking drop and drag button -->", e)
