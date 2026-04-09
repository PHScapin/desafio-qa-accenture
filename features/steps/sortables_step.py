from behave import given, when, then
from pages.sortable_page import SortablePage

@given('I navigate to the "Sortable" page')
def step_impl(context):
    context.sortable_page = SortablePage(context.driver)
    context.sortable_page.navigate()

@when('I reorder the list into ascending order using drag and drop')
def step_impl(context):
    context.sortable_page.sort_in_ascending_order()

@then('I validate that the list is in ascending order')
def step_impl(context):
    current_order = context.sortable_page.get_list_items_text()
    expected_order = ["One", "Two", "Three", "Four", "Five", "Six"]
    
    assert current_order == expected_order, f"Assertion Failed: The list order is {current_order}"