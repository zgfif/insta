from applib.custom_chrome_options import CustomChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from applib.human_pause import human_pause
from applib.cdp_scripts import script1, script2



class Browser:
    def __init__(self) -> None:
        """
        Initialize ChromeBrowser with custom options.
        """
        chrome_options = CustomChromeOptions().setup()
        self._driver = webdriver.Chrome(options=chrome_options)
        
        # Perform running scripts on every page before loading.
        self._driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script1})        
        self._driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script2})
       


    def open(self, url: str) -> None:
        """
        Open url.
        """
        self._driver.get(url=url)
        
        # wait until loads body.
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        human_pause(4, 5)



    @property
    def driver(self) -> WebDriver:
        """
        Return instance of WebDriver.
        """
        return self._driver



    def close(self) -> None:
        """
        Terminate driver.
        """
        self._driver.quit()
