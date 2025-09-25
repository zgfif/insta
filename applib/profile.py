from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from applib.media_data import ImageData
from applib.xlsx_file import XlsxFile




class Profile:
    TIMEOUT = 10


    def __init__(self, driver: WebDriver, filename: str) -> None:
        self._driver = driver
        self._filename = filename
    

    def process(self) -> None:
        """
        Process all media elements on page and save data to xlsx file.
        """
        images_block = self._images_block_element()

        if not images_block:
            return
        
        images_links = self._image_links_elements(images_block)

        if not images_links:
            return

        for i, link in enumerate(images_links[0:1]):
            data = ImageData(driver=self._driver, image_link=link, id=i+1).extract()
            print(f'media: {i}',data)

            XlsxFile(filepath=self._filename).add_row(data)
    


    def _image_links_elements(self, images_block: WebElement) -> list[WebElement]|list:
        """
        Return list of media links. If could not found any links return an empty list.
        """
        selector = (By.TAG_NAME, 'a')
        try:
            return WebDriverWait(images_block, self.TIMEOUT).until(
                EC.presence_of_all_elements_located(selector)
            )
        except TimeoutException:
            print('Could not found any media links. Return an empty links.')
            return []



    def _images_block_element(self) -> WebElement|None:
        """
        Return block which contains medeia. If could not found return None.
        """
        selector = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/div/div[2]/div/div/div/div')
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            print('Could not found images block. Return None.')
