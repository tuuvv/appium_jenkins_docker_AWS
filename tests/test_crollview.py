from pytest_bdd import parsers, scenarios, given, when, then

from pages.scroll_view_page import CrollView

crollView = CrollView()

scenarios('../features/ScrollView.feature')

@given("User is on 'main' page")
def mainsloadPage():
    crollView.load_page()

@when("User clicks on 'ScrollView' button at Main page")
def hit_crollview_btn():
    crollView.click_crollview_btn()

@then(parsers.parse("Srollview and select '{tolabel}'"))
def CrollView_Click(tolabel):
    crollView.CrollView_to_label(tolabel)

@then("click yes btn")
def hit_yes_btn():
    crollView.click_yes_btn()