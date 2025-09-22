import unittest
from applib.extraction import Extraction
from applib.browser import Browser



class TestExtraction(unittest.TestCase):
    def test_perform_extraction(self):
        url = 'https://www.instagram.com/aasdjjfjfkfk/'
        
        browser = Browser()
        
        browser.open(url=url)
        
        data = Extraction(driver=browser.driver).perform()

        self.assertIsInstance(data, tuple)
