from behave import given, when, then
from pages.windows_page import WindowsPage

@given('I access the "Browser Windows" page')
def step_impl(context):
    context.windows_page = WindowsPage(context.driver)
    context.windows_page.navigate()

@when('I click on the "New Window" button')
def step_impl(context):
    context.windows_page.open_new_window()

@then('a new window should open with the message "{expected_text}"')
def step_impl(context, expected_text):
    actual_text = context.windows_page.get_sample_text()
    assert actual_text == expected_text, f"Expected {expected_text} but got {actual_text}"

@then('I close the new window')
def step_impl(context):
    context.windows_page.close_and_return()