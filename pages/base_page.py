from data.main_data import MainData
import logging
from Utilities.LogUtil import Logger
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
# TODO: add logger
# NOTE: logger
log = Logger(__name__, logging.INFO)


class BasePage(MainData):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    @property
    def link_includes_(self, inner_text: str):
        """
        @param inner_text, str, text that should be included in link
        """
        return f"//a[contains(text(), '${inner_text}')]"

    def locate_then_click(locator: str, )
        """
        @param locator, str, to locate element, xpath: default
        @return None - as eroro
        """
        # FIXME: we are here
        pass


    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configReader.readConfig("locators", locator)).click()
        log.logger.info("Clicking on an element: " + str(locator))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configReader.readConfig("locators", locator)).send_keys(value)

        log.logger.info("Typing in an element: " + str(locator) + " value entered as : " + str(value))

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element_by_id(configReader.readConfig("locators", locator))

        select = Select(dropdown)
        select.select_by_visible_text(value)

        log.logger.info("Selecting from an element: " + str(locator) + " value selected as : " + str(value))

    def moveTo(self, locator):
        #added comments
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element_by_id(configReader.readConfig("locators", locator))

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        log.logger.info("Moving to an element: " + str(locator))
