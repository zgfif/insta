from applib.custom_chrome_options import CustomChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from applib.human_pause import human_pause
from applib.cdp_scripts import script1, script2
from selenium.common.exceptions import TimeoutException, WebDriverException




class Browser:
    def __init__(self) -> None:
        """
        Initialize ChromeBrowser with custom options.
        """
        chrome_options = CustomChromeOptions().setup()
        self._driver = webdriver.Chrome(options=chrome_options)
        
        # Perform running scripts on every page before loading.
        for script in script1, script2:
            self._driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})



    def open(self, url: str) -> None:
        """
        Open url.
        """
        try:
            print(f'Opening page {url} ...')
            self._driver.get(url=url)
        
            WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            human_pause(4, 5)
        except TimeoutException:
            print(f"Timeout while loading {url}")
        except WebDriverException as e:
            print(f"WebDriver error while opening {url}: {e}")
        



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
        print('Closing browser...')
        self._driver.quit()


    def __enter__(self):
        """Return self for working with."""
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close browser after exit from context.
        """
        self.close()
