from typing import Union, List
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
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
        self._mylog = log()
        self._wait = WebDriverWait(self.driver, self.WAIT_TIME)

    @staticmethod
    def get_link_includes(inner_text: str) -> str:
        """
        @param inner_text, str, text that should be included in link
        """
        return f"//a[contains(text(), '{inner_text}')]"

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

        self._mylog.debug(f'try to click: Found element for locator: {locator}')
        # LOGME: located element for locator: {locator}

        # TODO: get the click Exceptions errors, then log and process them
        return el.click()

    def wait_element_located(self, locator: str, by_type: str = By.XPATH
                             ) -> Union[None, WebElement]:
        """
        @param: locator, str - name of locator of parameter in base
        @param: locator_type, str - name of locator type, look expl in
        self.wait_located_click
        if element is not found will rise assertion explanation
        @return: webdriver object of element if element was located

        """
        self._mylog.debug(
            f'trying to wait and locate element for locator: {locator}, '
            f'with locator type: {by_type}'
        )

        # DEBUG: check the By.XPATH type and add it in validation method
        el = self._wait.until(
            EC.presence_of_element_located((by_type, locator))
        )
        self._mylog.debug(f'Found element: {el}')
        return el

    def wait_all_elements_located(self, locator: str, by_type: str = By.XPATH
                                  ) -> List:
        """
        Wait and locate all elements with received locator
        @param: locator, str, locator of element
        @param: by_type, By.XPATH default or another "By.ID" and other elements
        @returns: List, empty list if no elements were found and List of
        Web elements if elements were found.
        """
        self._mylog.debug(f'Trying to locate all element with locator: '
                          f'{locator}, type of locator "By": {by_type}')

        els = self._wait.until(
            EC.presence_of_all_elements_located((by_type, locator))
        )
        return els

    def open_url(self, url: str) -> None:
        """
        @param: str, url - need to be open
        """
        self._mylog.debug(f'Trying to open URL: {url}')
        self.driver.get(url)

    def wait_link_click_with_(self, inner_text: str) -> Union[None, WebElement]:
        locator = self.get_link_includes(inner_text)
        # link created from inner_text value it will be xpath as default
        self._mylog.debug(f'will wait element located: {locator}')
        el = self.wait_element_located(locator)

        el = self.click_located(el)

        return el

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
        """
        @param: el, webdriver element object, will be validated if is None
        @returns: webdriver element if click was successful and None if not.
        """

        self._mylog.debug(f'trying ot click element: {el}')
        self._mylog.debug(f'type of element arrived: {type(el)}')
        if el is not None:
            try:
                el.click()
                self._mylog.debug(f'Element after click: {el}')
            except TimeoutException:
                el = None
                self._mylog.error(f'driver can not click element: {el}')
        else:
            msg = f'element was not located and arrived for click as None.'
            self._mylog.error(msg)

        return el

    def click_link_includes_(self, inner_text: str) -> Union[None, WebElement]:
        self._mylog.debug(
            f'Inner text: {inner_text} arrived in click_link_includes_')
        el = self.wait_link_click_with_(inner_text)

        return el

    def wait_title_on_page(self, text: str) -> webdriver:
        """
        @param: text, str - text of title should consist

        """

        self._mylog.debug(f'It will wait on page title: {text}')

        return self._wait.until(EC.title_contains(text))

bp = BasePage('dos')
print()
bp.select_by_type('my_page_CSS')