from behave import when, then

from pages.about_us.about_us_page import AboutUsPage
from utilities import utils


@when(u'find link contains text "{inner_text}" and click it')
def step_impl(context, inner_text):
    print(f'It will click link includes: {inner_text}')
    context.aup = AboutUsPage(context.driver)
    # NOTE AboutUsPage class inherit from BasePage class
    res = context.aup.click_link_includes_(inner_text)
    # NOTE Webdriver element return if pass and None if not found/ not clicked
    assert res is not None, f'It can not click link contains text: {inner_text}'

# NOTE: this method made flexible and used with any URL address with
# key as name of page may be placed in Gherkin syntax
@then('on opened page "{title}" should be as expected')
def step_impl(context, title):
    print(f'I will wait title on page by key: "{title}"')

    # NOTE: this method is universal for all pages, just select key of title
    # it may be re-used on another pages.
    res = context.aup.wait_title_on_page(context.hp_data[title])
    assert res is not None, \
          'Expected title was not found on page for the default waiting time.'


@then('on opened page quantity of located Our Values elements equal {expected_qty}')
def step_impl(context, expected_qty):

    msg = f'Variable expected_qty: {expected_qty}, can not be integer.'
    assert expected_qty.isnumeric(), msg

    # NOTE: Saved found elements help to avoid 2nd search of elements
    # and spending time for this
    context.our_values = context.aup.get_our_values_elements()
    found_qty = len(context.our_values)

    msg = f'Found quantity: {found_qty} is not ' \
          f'equal expected quantity: {expected_qty}'
    assert found_qty == int(expected_qty), msg


@then('all expected values "{elements}" present in')
def step_impl(context, elements):
    expected_els = elements.split()
    print(f'I will validate Our Value elements: {expected_els}')
    found_els = [el.get_attribute('innerText') for el in context.our_values]
    utils.lists_have_equal_elements(expected_els, found_els)
