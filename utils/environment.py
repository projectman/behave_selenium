# TODO: update allure reprot
# import allure
from selenium import webdriver
from behave import fixture, use_fixture
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from tests.utils.main_data import MainData

@fixture
def before_scenario(context) -> None:
    """
        Add Maindata data class to context object before scenario execution. 
    """
    # save Main data in context object
    context.md = MainData()

def select_driver_for(browser_name: str) -> None:
    """
    @param browser_name: str, name of browser from the list of brosers
    @return None, update the context.driver parameter by initiated WebDriver object 
    """
    # Default driver: CHROME
    if browser_name == context.md.FIREFOX: 
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == context.md.MOBILE: 
        # TODO: decide how will work mobile web browser
        context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    else:
        context.dirver = context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())  
        

def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    # TODO: move in the base page
    if step.status == 'failed':
        allure.attach(
            context.driver.get_screenshot_as_png(), name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )
