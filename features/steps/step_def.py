from behave import given, when, then
from selenium import webdriver

@given('I am on home page')
def step_impl(context):
    context.driver.get("https://codoid.com")

@when('I submit contact us form')
def step_impl(context):
    pass

@then('I should see Thank You page with a message')
def step_impl(context):
    pass