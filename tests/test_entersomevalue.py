from pytest_bdd import parsers, scenarios, given, when, then

from pages.enter_some_value_page import EnterSomeValue

enterSomeValue = EnterSomeValue()

scenarios('../features/entersomevalue.feature')

@given("User is on 'main' page")
def mainsloadPage():
    enterSomeValue.load_page()

@when("User clicks on 'Enter some value' button at Main page")
def hit_entervalue_btn():
    enterSomeValue.click_entervalue_btn()

@then(parsers.parse("send '{value}' to input field"))
def sendkeys_to_input(value):
    enterSomeValue.sendkey_value(value)