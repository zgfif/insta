import unittest
from applib.media_data import MediaData
from applib.browser import Browser



class TestImage(unittest.TestCase):
    def test_perform_extraction(self):
        url = 'https://www.instagram.com/aasdjjfjfkfk/'
        
        browser = Browser()
        
        browser.open(url=url)
        
        data = MediaData(driver=browser.driver, image_link=None, id=1).extract()

        self.assertIsInstance(data, tuple)

        browser.close()
