"""
    Module to create hooks scenarios.
"""
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# TODO: update allure report
from data.base_data import BaseData

POSITIONS = ((0, 0), (500, 200), (1000, 400))


def before_all(context):
    # chrome will be used as default browser
    browser = context.config.userdata.get('browser', 'chrome')
    print(f'in before all was chosen: {browser}')
    select_driver_for(context, browser)

def select_driver_for(context, browser_name: str) -> None:
    """
    @param: context, behave.runner.Context object
    @param: browser_name: str, name of browser from the list of browsers
    select the webdriver with in accordance with arrived browser_name, then
    @returns: None, update the context. driver parameter
    by initiated WebDriver object

    """

    # Default driver: CHROME
    bd = BaseData()
    dr_path = ChromeDriverManager().install()

    if browser_name == bd.FIREFOX:
        # dr_path = GeckoDriverManager().install()   only chrome for debug
        context.driver = webdriver.Chrome(executable_path=dr_path)
        pos_i = 1

    elif browser_name == bd.MOBILE:
        # TODO: update code for MOBILE browser
        context.driver = webdriver.Chrome(executable_path=dr_path)
        pos_i = 2
    else:
        # Chrome browser by default
        context.driver = webdriver.Chrome(executable_path=dr_path)
        pos_i = 0

    context.driver.set_window_position(*POSITIONS[pos_i])


def after_scenario(context, scenario):
    print(f'it was scenario: {scenario.name}')
    context.driver.quit()


def after_step(context, step):
    # TODO: update allure module
    if step.status == 'failed':
        print('allure will be implemented')
        # allure.attach(
        #     context.driver.get_screenshot_as_png(), name='screenshot',
        #     attachment_type=allure.attachment_type.PNG
        # )

