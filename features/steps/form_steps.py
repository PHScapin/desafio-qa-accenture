from behave import given, when, then
from pages.form_page import PracticeFormPage
from faker import Faker

fake = Faker('en_US')

@given('I access the Practice Form page')
def step_impl(context):
    context.form_page = PracticeFormPage(context.driver)
    context.form_page.navigate()

@when('I fill out the entire form with random values')
def step_impl(context):
    context.form_page.fill_basic_info(
        first=fake.first_name(),
        last=fake.last_name(),
        email=fake.email(),
        mobile=fake.numerify(text='##########')
    )
    context.form_page.select_gender("Male")
    context.form_page.set_date_of_birth("22 Aug 2022")
    context.form_page.select_hobbies("Sports")
    context.form_page.upload_txt_file("challenge_file.txt") 

@when('I submit the form')
def step_impl(context):
    context.form_page.submit_form()

@then('a confirmation popup should be displayed')
def step_impl(context):
    success_msg = context.form_page.get_success_message()
    assert "Thanks for submitting the form" in success_msg, "Popup is not working properly."

@then('I close the popup')
def step_impl(context):
    context.form_page.close_modal()