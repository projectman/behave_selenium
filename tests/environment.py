"""
    Module to create hooks scenarios.
"""

from behave import given
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# TODO: update allure report
from pages.home.home_page import HomePage
from utilities import utils


@given('user chooses browser "{browser}"')
def step_impl(context, browser):
    context.driver = select_driver_for(context, browser)
    context.hp = HomePage(context.driver)
    context.hp_data = utils.read_yaml(context.hp.HOME_PAGE_YAML)
    print(f'I will set browser: {browser}')


def select_driver_for(context, browser_name: str) -> None:
    """
    @param browser_name: str, name of browser from the list of browsers
    @return None, update the context. driver parameter by initiated WebDriver object
    """
    print(f'select_driver_for: chosen driver: {browser_name}')

    # Default driver: CHROME
    dr_path = ChromeDriverManager().install()
    if browser_name == context.hp.FIREFOX:
        dr_path = GeckoDriverManager().install()
        context.driver = webdriver.Firefox(executable_path=dr_path)
    elif browser_name == context.hp.MOBILE:
        # TODO: update code for MOBILE browser
        context.driver = webdriver.Chrome(executable_path=dr_path)
    else:
        context.driver = webdriver.Chrome(executable_path=dr_path)


def after_scenario(context, scenario):
    context.driver.quit()


def after_step(context, step):
    # TODO: update allure module
    if step.status == 'failed':
        print('how allure works? ')
        # allure.attach(
        #     context.driver.get_screenshot_as_png(), name='screenshot',
        #     attachment_type=allure.attachment_type.PNG
        # )

