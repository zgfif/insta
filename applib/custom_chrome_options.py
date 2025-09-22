from selenium.webdriver.chrome.options import Options


class CustomChromeOptions:
    def __init__(self) -> None:
        self._options = Options()

    
    def setup(self) -> Options:
        self._options.add_argument('--user-agen=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36')
        self._options.add_argument("--start-maximized")
        self._options.add_argument("--disable-blink-features=AutomationControlled")
        self._options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self._options.add_experimental_option('useAutomationExtension', False)
        return self._options
