from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from applib.human_like_mouse_move import human_like_mouse_move
from applib.human_pause import human_pause



class MediaData:
    TIMEOUT = 10

    def __init__(self, driver, image_link: WebElement, id: int) -> None:
        self._driver = driver
        self._image_link = image_link
        self._id = id

    
    def extract(self) -> dict:
        """
        Return the dict containing: id, url, comments and subs.
        """
        data = {
            'id': self._id, 
            'url': self._image_link.get_attribute("href"), 
            'comments': 'N/A', 
            'subs': '',
        }

        if not self._image_link:
            return data
        
        human_like_mouse_move(driver=self._driver, element=self._image_link)
        
        human_pause(1, 2)
        
        self._image_link.click()
        
        human_pause(1, 2)
        
        comments_block_element = self._comments_block_element()
        
        if not comments_block_element:
            return data
        
        if len(comments_block_element) > 2:
            data['comments'] = comments_block_element[2].text
        
        close_image_element = self._close_image_element()

        if not close_image_element:
            return data
        
        human_pause(5,10)

        human_like_mouse_move(driver=self._driver, element=close_image_element)

        close_image_element.click()

        human_pause(10, 15)

        return data



    def _comments_block_element(self) -> list:
        """
        Return the list of all ul tags on page.
        """
        selector = (By.TAG_NAME, 'ul')
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_all_elements_located(selector)
            )
        except TimeoutException:
            print('Could not found comments block. Return None.')
            return []



    def _close_image_element(self) -> WebElement|None:
        """
        Return  the close image view div. If could not found return None.
        """
        selector = (By.XPATH, '//div[./*[name()="svg" and @aria-label="Close"]]')

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Could not found close image element. Return None.')
