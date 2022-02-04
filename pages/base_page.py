
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data.base_data import BaseData
from utilities.my_logger import custom_logger as log
from selenium.webdriver.support.ui import WebDriverWait




class BasePage(BaseData):

    """
    This is the Base Page class that include the general methods for manage
    selenium web driver universal methods with specific page data.

    """

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.log = log()
        self._wait = WebDriverWait(self.driver, self.WAIT_TIME)


    def get_link_includes(self, inner_text: str) -> str:
        """
        @param inner_text, str, text that should be included in link
        """
        return f"//a[contains(text(), '${inner_text}')]"

    def wait_located_click(self, locator: str, locator_type: str = By.XPATH):
        """
        @param: locator, str, to locate element,
        type of locator: xpath - default
        # FIXME: need to update from string xpath to "By" class selector
        @returns: webdriver object of element, was located and clicked
        @SUCCESS: webdriver element if element was found and clicked,
        @FAILED: None, when element was not found.
        """

        el = self.wait_element_located(locator, locator_type)

        self.log.debug(f'found element for locator: {locator}')
        # LOGME: located element for locator: {locator}

        # TODO: get the click Exceptions errors, then log and process them
        return el.click()

    def wait_element_located(self, locator: str, by_type: str = By.XPATH):
        """
        @param: locator, str - name of locator of parameter in base
        @param: locator_type, str - name of locator type, look expl in
        self.wait_located_click
        if element is not found will rise assertion explanation
        @return: webdriver object of element if element was located

        """
        self.log.debug(
            f'trying to wait and locate element for locator: {locator}, '
            f'with locator type: {by_type}'
        )

        # DEBUG: check the By.XPATH type and add it in validation method
        el  = self._wait.until(
            EC.presence_of_element_located((by_type, locator))
        )
        return el

    def open_url_(self, url: str) -> None:
        """
        @param: str, url - need to be open
        """
        self.log.debug(f'Trying to open URL: {url}')
        self.driver.get(url)

    def wait_link_click_with_(self, inner_text: str):
        locator = self.get_link_includes(inner_text)
        # link created from inner_text value it will be xpath as default
        self.wait_located_click(locator)

    def select_by_type(self, locator_key: str) -> str:
        """
        @param: locator_key, str - key of key: value a pair of locator data
        when key ended by '_ID' - will be chosen 'By.ID' selector,
        '_CSS': By.CSS
        @return: By class object
        """
        by_type = By.XPATH
        if locator_key.endswith('_ID'):
            by_type = By.ID
        elif locator_key.endswith('_CSS'):
            by_type = By.CSS_SELECTOR

        return by_type


    def click_located(self, el: webdriver):
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
bp.select_by_type('my_page_CSS')