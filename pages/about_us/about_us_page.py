from pages.base_page import BasePage


class AboutUsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self) -> None:
        self.open_url_(self.HOME_URL)

    def click_link_includes_(self, inner_text: str) -> None:
        el = self.wait_link_click_with_(inner_text)
        assert el is not None, \
            f'Element - link with inner text: {inner_text} can not be clicked.'



