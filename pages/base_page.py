from ctypes import Union
from typing import Optional

from selenium import webdriver
from data.main_data import MainData
from utilities.my_logger import custom_logger as log
import logging as level
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select



class BasePage(MainData):

    def __init__(self, driver):
        super().__init__()
        self._driver = driver
        self._log = log()

    def get_link_includes(self, inner_text: str) -> str:
        """
        @param inner_text, str, text that should be included in link
        """
        return f"//a[contains(text(), '${inner_text}')]"

    def locate_then_click(self, locator: str):
        """
        @param: locator, str, to locate element, xpath: default
        end of locator name includes type of locator:
        - by default it is xpath locator
        - '_CSS' - css locator
        - '_ID' - locate by ID and ...
        @returns:
        @SUCCESS: webdriver element if element was found and clicked,
        @FAILED: None, when element was not found.
        """
        self._log.debug('this is debug only ')
        el = self.locate_element(locator)
        if el is not None:
            self._log.debug(f'found element for locator: {locator}')
            # LOGME: located element for locator: {locator}
            return self.click_located(el)
        self._log.error('this is error level')
        return el

    def locate_element(self, locator: str):
        self._log.error('this is error level')
        return 'something'

    def click_located(self, el):
        pass
        return None
    # def click(self, locator):
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("_CSS"):
    #         self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator)).click()
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_element_by_id(configReader.readConfig("locators", locator)).click()
    #     log.logger.info("Clicking on an element: " + str(locator))
    #
    # def type(self, locator, value):
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).send_keys(value)
    #     elif str(locator).endswith("_CSS"):
    #         self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator)).send_keys(value)
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_element_by_id(configReader.readConfig("locators", locator)).send_keys(value)
    #
    #     log.logger.info("Typing in an element: " + str(locator) + " value entered as : " + str(value))
    #
    # def select(self, locator, value):
    #     global dropdown
    #     if str(locator).endswith("_XPATH"):
    #         dropdown = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator))
    #     elif str(locator).endswith("_CSS"):
    #         dropdown = self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator))
    #     elif str(locator).endswith("_ID"):
    #         dropdown = self.driver.find_element_by_id(configReader.readConfig("locators", locator))
    #
    #     select = Select(dropdown)
    #     select.select_by_visible_text(value)
    #
    #     log.logger.info("Selecting from an element: " + str(locator) + " value selected as : " + str(value))
    #
    # def moveTo(self, locator):
    #     #added comments
    #     if str(locator).endswith("_XPATH"):
    #         element = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator))
    #     elif str(locator).endswith("_CSS"):
    #         element = self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator))
    #     elif str(locator).endswith("_ID"):
    #         element = self.driver.find_element_by_id(configReader.readConfig("locators", locator))
    #
    #     action = ActionChains(self.driver)
    #     action.move_to_element(element).perform()
    #
    #     log.logger.info("Moving to an element: " + str(locator))

bp = BasePage('dos')
print()
bp.locate_then_click('my page')