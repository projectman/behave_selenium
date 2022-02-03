"""
    Module to create hooks scenarios.
"""


def before_all(context):
    print('It launch "before_all" hook process')



def after_scenario(context):
    context.driver.quit()


def after_step(context, step):
    # TODO: update allure module
    if step.status == 'failed':
        print('how allure works? ')
        # allure.attach(
        #     context.driver.get_screenshot_as_png(), name='screenshot',
        #     attachment_type=allure.attachment_type.PNG
        # )
