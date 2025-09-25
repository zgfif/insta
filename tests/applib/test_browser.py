import unittest
from applib.browser import Browser
import time



class TestBrowser(unittest.TestCase):
    def test_open_instagram(self):
        browser = Browser()
        
        browser.open(url='https://www.instagram.com/hildegard.debondt/')
        
        time.sleep(5)
        
        self.assertIn('hildegard.debondt', browser.driver.current_url)
        
        browser.close()
