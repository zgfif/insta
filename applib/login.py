from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from applib.human_like_mouse_move import human_like_mouse_move
from applib.human_pause import human_pause



class Login:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, username: str, password: str) -> None:
        self._driver = driver
        self._username = username
        self._password = password


    def perform(self) -> None:
        """
        
        """
        input_username_element = self._input_username_element()
        if not input_username_element:
            return
        
        input_password_element = self._input_password_element()
        if not input_password_element:
            return
        
        login_button_element = self._login_button_element()
        if not login_button_element:
            return
        
        human_like_mouse_move(driver=self._driver, element=input_username_element)
        input_username_element.send_keys(self._username)
        human_pause(2, 5)

        human_like_mouse_move(driver=self._driver, element=input_password_element)
        input_password_element.send_keys(self._password)
        human_pause(2, 6)
        
        human_like_mouse_move(driver=self._driver, element=login_button_element)
        login_button_element.click()
        human_pause(7, 15)



    def _input_username_element(self) -> WebElement|None:
        """
        Return input username element. If could not found return None.
        """
        selector = (By.XPATH, "//input[@name='username']")

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Could not found username input. Return None.')



    def _input_password_element(self) -> WebElement|None:
        """
        Return input password element. If could not found return None.
        """
        selector = (By.XPATH, "//input[@name='password']")
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Could not found password input. Return None.')



    def _login_button_element(self) -> WebElement|None:
        selector = (By.XPATH, "//div[text()='Log in']")
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Could not found password input. Return None.')
