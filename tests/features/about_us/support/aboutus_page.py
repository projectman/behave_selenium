from features.pageobjects.BasePage import BasePage


class AboutUsPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def open_home_page(self) -> None:
        self.driver.get(self.HOME_URL)

    def click_link_includes_(inner_text: str) -> None: 
        locator = self.link_includes_(inner_text)
        self.locate_then_click(locator)

