from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        super().__init__()


    def first_done(self, text: str = ''):
        print(f'first_method from HomePage {text}')

    def second_method_home_page(self, text: str = ''):
        print(f'second method from HomePage class: {text}')
