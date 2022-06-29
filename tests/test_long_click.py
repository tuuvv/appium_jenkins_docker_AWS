from pytest_bdd import parsers, scenarios, given, when, then

from pages.long_click_page import LongClick

long_click_page = LongClick()

scenarios('../features/longclick.feature')

@given("User is on 'main' page")
def mainsloadPage():
    long_click_page.load_page()

@when("User long clicks on 'LONG CLICK' button at Main page")
def longclick_btn():
    long_click_page.longclick_btn()