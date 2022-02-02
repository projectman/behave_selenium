import time

# FIXME: what is inside behave module, what we need instead of wild card? 
from behave import *
from features.about_us.aboutus_page import AboutUsPage

# Expected steps
Given user choses browser "chrome"
And user open Home Page
When find link contains text "About Us" and click it
# Then on opened page Title will be as expected
# Then on opened page quantity of located Our Values elements eqal 3
# And all expected values "Accountable, Realiable, Ethical" present in

# New code
@given(u'user chose browser "{browser}"')
def step_impl(context):
    # FIXME: does this update browser??? 
    context.select_driver_for(borwser)
    context.aup = AboutUsPage(context.driver)


# TODO: update open page with dictionary opened by name "Home Page"
@given(u'user open Home Page')
def step_impl(context):
    context.reg.open_home_page()


@when(u'When find link contains text "{innerText}" and click it')
def step_impl(context, innerText):
    context.reg.click_link_includes_(innerText)





# Old code







@then(u'I enter the phone number as "{phoneNumber}"')
def step_impl(context, phoneNumber):
    context.reg.setPhoneNumber(phoneNumber)


@then(u'I enter the email as "{email}"')
def step_impl(context, email):
    context.reg.setEmail(email)


@then(u'I enter the country as "{country}"')
def step_impl(context, country):
    context.reg.setCountry(country)


@then(u'I enter the city as "{city}"')
def step_impl(context, city):
    context.reg.setCity(city)


@then(u'I enter the username as "{email}"')
def step_impl(context, email):
    context.reg.setUsername(email)


@then(u'I enter the password as "{password}"')
def step_impl(context, password):
    context.reg.setPassword(password)


@then(u'I click on the submit button')
def step_impl(context):
    context.reg.submitForm()
    assert False
    time.sleep(3)
