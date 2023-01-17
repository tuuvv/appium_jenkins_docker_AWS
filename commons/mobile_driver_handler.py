from appium.webdriver.common.mobileby import MobileBy as mobily_by
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from appium.webdriver.common.multi_action import MultiAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
import json

class MobileDriverHandle():

    def __init__(self):
        # sauce_url = "http://127.0.0.1:4723/wd/hub"
        sauce_url = 'https://qateam_4mOEUA:NzsduYY6QU5YqCYvFT96@hub-cloud.browserstack.com/wd/hub'
        desired_caps = {
            'autoGrantPermissions': True,
            'platformName': 'Android',
            'platformVersion': '11',
            'deviceName': 'R58R332YAYL',
            'deviceOrientation': 'portrait',
            'app': 'C:\\Users\\vuvan\\OneDrive\\Documents\\QA_PW_TUU\\appium_jenkins_docker_AWS-main\\source\\Android_Demo_App.apk',
            'appPackage': 'com.code2lead.kwad',
            'appActivity': 'com.code2lead.kwad.MainActivity',
            'appWaitActivity': 'com.code2lead.kwad.MainActivity',
            'full-reset': True
        }
        # for browserstack test
        # Use Appium-Python-Client v0.27 or above
        desired_cap = {
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "app": "bs://8b26585442dee3c22be4cfefc3d5b31412e1ddfe",
            'bstack:options': {
                "projectName": "test ok hay ko",
                "appiumVersion": "1.18.0",
                "acceptInsecureCerts": "true",
            },
        }

        self.driver = webdriver.Remote(sauce_url, desired_cap)
        # self.driver = webdriver.Remote(sauce_url, desired_caps)

    def get_driver(self):
        return self.driver

    def get_by(self, locator_type):
        try:
            if locator_type.lower() == 'xpath':
                locator_by = mobily_by.XPATH
            elif locator_type.lower() == 'id':
                locator_by = mobily_by.ID
            elif locator_type.lower() == 'css':
                locator_by = mobily_by.CSS_SELECTOR
            elif locator_type.lower() == 'link':
                locator_by = mobily_by.LINK_TEXT
            elif locator_type.lower() == 'class':
                locator_by = mobily_by.CLASS_NAME
            else:
                raise Exception("By of Locator not found for -->", locator_type)
            return locator_by
        except Exception as e:
            raise Exception("Error occurred while getting the by -->", e)

    def get_element(self, locator):
        try:
            split_locator = locator.split('~')
            locator_by = self.get_by(split_locator[0])
            locator_path = split_locator[1]
            ele = self.get_driver().find_element(by=locator_by, value=locator_path)
            return ele
        except Exception as e:
            raise Exception("Error occurred while getting the element:", e)

    def get_element_wait(self, locator):
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        try:
            split_locator = locator.split('~')
            locator_by = self.get_by(split_locator[0])
            locator_path = split_locator[1]
            ele = wait.until(lambda x: x.find_element(by=locator_by, value=locator_path))
            return ele
        except Exception as e:
            raise Exception("Error occurred while getting the element:", e)

    def click_element(self, locator):
        try:
            self.get_element(locator).click()
        except Exception as e:
            raise Exception("Exception occurred while clicking element:", e)

    def send_keys(self, locator, text):
        try:
            self.get_element(locator).send_keys(text)
        except Exception as e:
            raise Exception("Exception occurred while sending text to element:", locator, "-->", e)

    def click_element_wait(self, locator):
        try:
            self.get_element_wait(locator).click()
        except Exception as e:
            raise Exception("Exception occurred while clicking element:", e)

    def send_keys_wait(self, locator, text):
        try:
            self.get_element_wait(locator).send_keys(text)
        except Exception as e:
            raise Exception("Exception occurred while sending text to element:", locator, "-->", e)

    def CrollView_Click(self, tolabel):
        try:
            self.get_driver().find_element(mobily_by.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("'+tolabel+'"))').click()
        except Exception as e:
            raise Exception("Exception occurred while sending text to element:", tolabel, "-->", e)

    def longclick_element(self, locator):
        try:
            ele= self.get_element(locator)
            action = ActionChains(self.get_driver())
            action.click_and_hold(ele).perform()
        except Exception as e:
            raise Exception("Exception occurred while clicking element:", e)

    def tap_element(self, locator):
        try:
            coord = self.get_element(locator).location
            json_str = json.dumps(coord)
            resp = json.loads(json_str)
            action = TouchAction(self.get_driver())
            action.tap(None, resp["x"], resp["y"], 1).perform()
        except Exception as e:
            raise Exception("Exception occurred while tap element:", e)

    def drag_drop_element(self, locator, tolocator):
        try:
            ele = self.get_element(locator)
            toele = self.get_element(tolocator)
            action = TouchAction(self.get_driver())
            action.long_press(ele).move_to(toele).release().perform()
        except Exception as e:
            raise Exception("Exception occurred while clicking element:", e)

    def swipe_right_to_left_element(self):
        try:
            deviceSize = self.get_driver().get_window_size()
            screenWidth = deviceSize['width']
            screenHeight = deviceSize['height']

            ######Right to Left#######
            startx = screenWidth * 9 / 10
            endx = screenWidth / 10
            starty = screenHeight / 2
            endy = screenHeight / 2

            actions = TouchAction(self.get_driver())
            actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        except Exception as e:
            raise Exception("Exception occurred while clicking element:", e)

    def swipe_left_to_right_element(self):
        try:
            deviceSize = self.get_driver().get_window_size()
            screenWidth = deviceSize['width']
            screenHeight = deviceSize['height']

            ###### Left to Right    #######
            startx = screenWidth / 10
            endx = screenWidth * 9 / 10
            starty = screenHeight / 2
            endy = screenHeight / 2

            actions = TouchAction(self.get_driver())
            actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        except Exception as e:
            raise Exception("Exception occurred while clicking element:", e)

    def pinch_out_element(self):
        try:
            deviceSize = self.get_driver().get_window_size()
            xx = deviceSize['width']/2
            yy = deviceSize['height']/2

            action1 = TouchAction(self.driver)
            action1.long_press(x=xx, y=yy).move_to(x=0, y=300).wait(500).release()
            action2 = TouchAction(self.driver)
            action2.long_press(x=xx, y=yy).move_to(x=0, y=-300).wait(500).release()
            m_action = MultiAction(self.driver)
            m_action.add(action2, action1)
            m_action.perform()
        except Exception as e:
            raise Exception("Exception occurred while clicking element:", e)


    def pinch_in_element(self):
        try:
            deviceSize = self.get_driver().get_window_size()
            xx = deviceSize['width'] / 2
            yy = deviceSize['height'] / 2

            action1 = TouchAction(self.driver)
            action1.long_press(x=xx, y=300).move_to(x=0, y=yy).wait(500).release()
            action2 = TouchAction(self.driver)
            action2.long_press(x=xx, y=-300).move_to(x=0, y=yy).wait(500).release()
            m_action = MultiAction(self.driver)
            m_action.add(action2, action1)
            m_action.perform()
        except Exception as e:
            raise Exception("Exception occurred while clicking element:", e)
