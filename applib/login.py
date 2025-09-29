from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from applib.human_like_mouse_move import human_like_mouse_move
from applib.human_pause import human_pause
import logging



class Login:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, logger: logging.Logger,  username: str, password: str, ) -> None:
        self._driver = driver
        self._logger = logger
        self._username = username
        self._password = password


    def perform(self) -> None:
        """
        Enter username, password and press "Log in".
        """
        input_username_element = self._input_username_element()
        if not input_username_element:
            input_username_element = self._find_deeper_username()
            if not input_username_element:
                return
        
        input_password_element = self._input_password_element()
        if not input_password_element:
            return
        
        login_button_element = self._login_button_element()
        if not login_button_element:
            return
        
        self._logger.info('Start log in...')
        human_like_mouse_move(driver=self._driver, element=input_username_element)
        input_username_element.send_keys(self._username)
        human_pause(2, 5)

        human_like_mouse_move(driver=self._driver, element=input_password_element)
        input_password_element.send_keys(self._password)
        human_pause(2, 6)
        
        human_like_mouse_move(driver=self._driver, element=login_button_element)
        login_button_element.click()
        human_pause(7, 15)


    def _find_deeper_username(self) -> WebElement|None:
        """
        If page does not have username input we try to find "Log in" link and search again.
        """
        self._logger.info('Searching for another log in button...')
        
        link_on_login_page = self._link_on_login_page()
        
        if not link_on_login_page:
            return
        
        link_on_login_page.click()
        return self._input_username_element()



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
            self._logger.warning('Could not found username input. Return None.')



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
            self._logger.warning('Could not found password input. Return None.')



    def _login_button_element(self) -> WebElement|None:
        selector = (By.XPATH, "//div[text()='Log in']")
        
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.warning('Could not found password input. Return None.')



    def _link_on_login_page(self) -> WebElement|None:
        selector = (By.XPATH, "//a[text()='Log in']")
        
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.warning('Could not another login button. Return None.')
