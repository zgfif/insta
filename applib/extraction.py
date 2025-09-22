from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement



class Extraction:
    TIMEOUT = 10

    def __init__(self, driver) -> None:
        self._driver = driver

    
    def perform(self) -> tuple:
        image_divs_elements = self._image_divs_elements()
        if not image_divs_elements:
            print('Can not found any elemnents.')
            return tuple()
        print(f'Found {len(image_divs_elements)} images.')
        return tuple()
    

    def _image_divs_elements(self) -> list[WebElement]|list:
        selector = (By.CSS_SELECTOR, 'div._aagw')
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_all_elements_located(selector)
            )
        except TimeoutException:
            return []
        

