from pages.base_page import BasePage


class AboutUsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self) -> None:
        self.driver.get(self.HOME_URL)

    def click_link_includes_(self, inner_text: str) -> None: 
        locator = self.get_link_includes(inner_text)
        self.locate_then_click(locator)


