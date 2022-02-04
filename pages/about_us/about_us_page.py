from typing import List

from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utilities import utils


class AboutUsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.data = utils.read_yaml(self.ABOUT_US_DATA)

    def open_home_page(self) -> None:
        self.open_url(self.HOME_URL)

    def get_our_values_elements(self) -> List[WebElement]:
        els = self.wait_all_elements_located(self.data['checkmark_span'])
        return els
