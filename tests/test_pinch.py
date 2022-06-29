from pytest_bdd import parsers, scenarios, given, when, then

from pages.pinch_page import Pinch

pinch_page = Pinch()

scenarios('../features/pinch_in_and_out.feature')


@given("User is on 'main' page")
def mainsloadPage():
    pinch_page.load_page()


@when(parsers.parse("Scroll to '{tolabel}' button and click"))
def scroll_to_label(tolabel):
    pinch_page.sroll_to_label(tolabel)

@then("User pinch out")
def pinch_out():
    pinch_page.pinch_out()

@then("User pinch in")
def pinch_in():
    pinch_page.pinch_in()
