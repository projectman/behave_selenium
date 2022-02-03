from behave import when, then


@when(u'When find link contains text "{innerText}" and click it')
def step_impl(context, innerText):
    context.reg.click_link_includes_(innerText)


@then('on opened page Title will be as expected')
def step_impl(context):
    print(f'I will search text for: "{context.cur_page}"')


@then('on opened page quantity of located Our Values elements equal {el_qty}')
def step_impl(context, el_qty):
    print(f'I count elements equal : {el_qty}')


@then('all expected values "{elements}" present in')
def step_impl(context, elements):
    print(f'I will validate Our Value elements: {elements.split()}')
