from behave import given, when, then

@given('we have behave installed')
def step_impl(context):
    print('why not print')

@when('we implement a test')
def step_impl(context):
    print('see me???')
    assert True is False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False