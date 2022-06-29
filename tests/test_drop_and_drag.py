from pytest_bdd import parsers, scenarios, given, when, then

from pages.drop_drag_page import DropDrag

drop_drag_page = DropDrag()

scenarios('../features/dropdrag.feature')


@given("User is on 'main' page")
def mainsloadPage():
    drop_drag_page.load_page()


@when(parsers.parse("Scroll to '{tolabel}' button and click"))
def scroll_to_label(tolabel):
    drop_drag_page.sroll_to_label(tolabel)

@then("Drop and drag picture to midle part")
def drop_drag_picture():
    drop_drag_page.drop_drag_picture()

@then("Drop and drag text to last part")
def drop_drag_text():
    drop_drag_page.drop_drag_text()

@then("Drop and drag button to last part")
def drop_drag_btn():
    drop_drag_page.drop_drag_btn()
