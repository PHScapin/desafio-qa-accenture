from behave import given, when, then
from pages.web_tables_page import WebTablesPage
from faker import Faker

fake = Faker('en_US')

@given('I access the Web Tables page')
def step_impl(context):
    context.tables_page = WebTablesPage(context.driver)
    context.tables_page.navigate()

@when('I create a new record with random data')
def step_impl(context):
    context.tables_page.click_add_record()
    
    context.user_data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "age": fake.random_int(min=18, max=65),
        "salary": fake.random_int(min=2000, max=15000),
        "department": fake.job().split()[0][:10] 
    }
    
    context.tables_page.fill_record_form(
        first=context.user_data["first_name"],
        last=context.user_data["last_name"],
        email=context.user_data["email"],
        age=context.user_data["age"],
        salary=context.user_data["salary"],
        department=context.user_data["department"]
    )
    context.tables_page.submit_form()

@then('the new record should be visible in the table')
def step_impl(context):
    context.tables_page.search_record(context.user_data["email"])
    is_present = context.tables_page.is_record_present(context.user_data["email"])
    assert is_present is True, "The newly created record was not found in the table."

@when('I edit the newly created record with new random data')
def step_impl(context):
    context.tables_page.search_record(context.user_data["email"])
    context.tables_page.click_edit_record(context.user_data["email"])
    
    context.user_data["first_name"] = fake.first_name()
    context.user_data["salary"] = fake.random_int(min=20000, max=50000)
    
    context.tables_page.fill_record_form(
        first=context.user_data["first_name"],
        last=context.user_data["last_name"],
        email=context.user_data["email"],
        age=context.user_data["age"],
        salary=context.user_data["salary"],
        department=context.user_data["department"]
    )
    context.tables_page.submit_form()

@then('the updated record should be visible in the table')
def step_impl(context):
    context.tables_page.search_record(context.user_data["email"])
    is_present = context.tables_page.is_record_present(context.user_data["first_name"])
    assert is_present is True, "The updated record was not found."

@when('I delete the current record')
def step_impl(context):
    context.tables_page.search_record(context.user_data["email"])
    context.tables_page.click_delete_record(context.user_data["email"])

@then('the record should no longer be visible in the table')
def step_impl(context):
    context.tables_page.search_record(context.user_data["email"])
    is_present = context.tables_page.is_record_present(context.user_data["email"])
    assert is_present is False, "The record was not deleted successfully."