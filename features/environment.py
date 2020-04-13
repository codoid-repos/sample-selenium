from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def launch_browser(context):
    #Launch Browser
    context.driver = webdriver.Chrome(executable_path='drivers\chromedriver.exe')
    print("=============>Browser is launched")
    yield context.driver

    #Clean Up Browser
    context.driver.quit()
    print(context.scenario.duration)
    print("=============>Browser is quit")


def before_scenario(context,scenario):
    the_fixture1 = use_fixture(launch_browser, context)