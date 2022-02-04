import time

from behave import given, when, then
from pages.home.home_page import HomePage
from utilities import utils


@given('user chooses browser "{browser}"')
def step_impl(context, browser):
    # context.driver = select_driver_for(context, browser)
    # context.hp = HomePage(context.driver)
    # context.hp_data = utils.read_yaml(context.hp.HOME_PAGE_YAML)
    print(f'I will set browser: {browser}')


@given('user open "{page_name}"')
def step_impl(context, page_name):
    # NOTE: "Page Name" used as a key of dict from yaml data for re-usability
    print(f'open page: {page_name}')
    context.hp = HomePage(context.driver)
    # let save all url that will be need to open in data/home.yaml file...
    context.hp_data = utils.read_yaml(context.hp.HOME_PAGE_YAML)
    context.hp.open_url_(context.hp_data[page_name])


# Home page code not used for pennymac
@given('we have behave installed')
def step_impl(context):
    print('Home: we have behave...')


@when('we implement a test for home')
def step_impl(context):
    print('home when')
    assert True is not False, 'True can not be False!'


@then('behave will test it for us at home!')
def step_impl(context):
    assert True is not False
