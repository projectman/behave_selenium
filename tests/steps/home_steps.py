from behave import given, when, then


@given('user open "{page_name}"')
def step_impl(context, page_name):
    # NOTE: "Page Name" used as a key of dict from yaml data for re-usability
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
