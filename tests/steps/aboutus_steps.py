from behave import when, then


@when(u'find link contains text "{innerText}" and click it')
def step_impl(context, innerText):
    # context.reg.click_link_includes_(innerText)
    print(f'will click {innerText}')

@then('on opened page "{title}" will be as expected')
def step_impl(context, title):
    print(f'I will search text for: "{title}"')
    assert True is False, 'we need some failed test'


@then('on opened page quantity of located Our Values elements equal {el_qty}')
def step_impl(context, el_qty):
    print(f'I count elements equal : {el_qty}')


@then('all expected values "{elements}" present in')
def step_impl(context, elements):
    print(f'I will validate Our Value elements: {elements.split()}')
