from dataclasses import dataclass

@dataclass
class MainData:
    """
    Data class with project level constants
    
    """
    FIREFOX: str = 'firefox'
    CHROME: str = 'chrome'
    MOBILE: str = 'mobile'
    HOME_URL: str = 'https://www.pennymac.com'