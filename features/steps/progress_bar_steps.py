from behave import given, when, then
from pages.progress_bar_page import ProgressBarPage

@given('I navigate to the "Progress Bar" page in the Widgets menu')
def step_impl(context):
    context.progress_page = ProgressBarPage(context.driver)
    context.progress_page.navigate()

@when('I click the Start button and stop it before 25%')
def step_impl(context):
    context.progress_page.stop_at_target(target_value=22)

@then('I validate that the progress bar value is less than or equal to 25%')
def step_impl(context):
    current_value = context.progress_page.get_progress_value()
    assert current_value <= 25, f"Assertion Failed: Current value is {current_value}%, exceeding the 25% limit."

@when('I click Start again to reach 100% and reset the progress bar')
def step_impl(context):
    context.progress_page.resume_and_reset()