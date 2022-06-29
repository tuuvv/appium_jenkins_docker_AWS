from pytest_bdd import parsers, scenarios, given, when, then

from pages.tap_acivity_page import TapAcivity

tap_acivity_page = TapAcivity()

scenarios('../features/tapandswipeactivity.feature')

@given("User is on 'main' page")
def mainsloadPage():
    tap_acivity_page.load_page()

@when("User tap on 'TAP ACTIVITY' button at Main page")
def tap_btn():
    tap_acivity_page.tap_btn()

@then("User tap on 'SPORT' tab")
def tap_on_sport_tab():
    tap_acivity_page.tap_on_sport_tab()

@then("User tap on 'MOVIE' tab")
def tap_on_movie_tab():
    tap_acivity_page.tap_on_movie_tab()

@then("User swipe right to lelf")
def swipe_right_to_left():
    tap_acivity_page.swipe_right_to_left()

@then("User swipe left to right")
def swipe_left_to_right():
    tap_acivity_page.swipe_left_to_right()