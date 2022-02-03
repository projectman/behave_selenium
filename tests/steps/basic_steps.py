"""
    Module includes the general for all pages steps
"""

from behave import given


@given('user chooses browser "{browser}"')
def step_impl(context, browser):
    # TODO: add method for selection right driver
    print(f'I will set browser: {browser}')
