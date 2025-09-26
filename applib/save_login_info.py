from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from applib.human_like_mouse_move import human_like_mouse_move
from applib.human_pause import human_pause



class SaveLoginInfo:
    TIMEOUT = 10


    def __init__(self, driver: WebDriver, save: bool = False) -> None:
        self._driver = driver
        self._save = save

    
    def process(self) -> None:
        """
        Process "Save login info" window.
        """
        human_pause(4, 6)

        save_info_element = self._save_info_element()
        if not save_info_element:
            return
        
        not_now_element = self._not_now_element()
        if not not_now_element:
            return

        print('Start Save login info...')

        if self._save:
            human_like_mouse_move(driver=self._driver, element=save_info_element)
            save_info_element.click()
        else:
            human_like_mouse_move(driver=self._driver, element=not_now_element)
            not_now_element.click()

        human_pause(2, 3)


    def _save_info_element(self) -> WebElement|None:
        selector = (By.XPATH, "//button[text()='Save info']")
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.element_to_be_clickable(selector)
            )
        except TimeoutException:
            print('Could not found "Save info" element. Return None.')


    def _not_now_element(self) -> WebElement|None:
        selector = (By.XPATH, "//div[text()='Not now']")        
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.element_to_be_clickable(selector)
            )
        except TimeoutException:
            print('Could not found "Not now" element. Return None.')
