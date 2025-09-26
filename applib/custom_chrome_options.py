from selenium.webdriver.chrome.options import Options



class CustomChromeOptions:
    def __init__(self) -> None:
        self._options = Options()


    def setup(self) -> Options:
        """
        Set options for Google Chrome: --user-agent, --start-maximized, ... 
        """
        self._options.add_argument(f'--user-agent={self._user_agent()}')
        self._options.add_argument("--start-maximized")
        self._options.add_argument("--disable-blink-features=AutomationControlled")
        self._options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self._options.add_experimental_option('useAutomationExtension', False)
        return self._options
    

    def _user_agent(self) -> str:
        """
        Return default user-agent for browser.
        """
        return 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
