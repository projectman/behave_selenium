from behave import given, when, then


# TODO: update open page with dictionary opened by name "Home Page"
@given('user open "{page_name}"')
def step_impl(context, page_name):
    # NOTE: save cur_page for later re-useability 
    context.cur_page = page_name
    print(f'it will open {page_name}')

# Home page code not used for pennymay
@given('we have behave installed')
def step_impl(context):
    print('Home: we have behave...')


@when('we implement a test for home')
def step_impl(context):
    print('home when')
    context.hp = HomePage()
    context.hpd = read_yaml(context.hp.HOME_PAGE_YAML)
    title = context.hpd['title']
    print(f'in home steps get title: {title}')
    assert True is not False, 'True can not be False!'


@then('behave will test it for us at home!')
def step_impl(context):
    print(f'home then: access Main data: {context.hp.CHROME}')
    context.hp.second_method_home_page('home_steps')
    assert True is not False
