from dataclasses import dataclass


@dataclass
class BaseData:
    """
    Data class with project level constants
    
    """
    FIREFOX: str = 'firefox'
    CHROME: str = 'chrome'
    MOBILE: str = 'mobile'
    HOME_URL: str = 'https://www.pennymac.com'
    WAIT_TIME: str = 5
    HOME_PAGE_YAML: str = 'data/home.yaml'
    ABOUT_US_DATA: str = 'data/about_us.yaml'