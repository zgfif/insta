import unittest
from applib.login import Login
from applib.browser import Browser
import os



class TestLogin(unittest.TestCase):
    def test_login(self):
        browser = Browser()
        
        browser.open(url='https://instagram.com/pashabratanov')

        Login(driver=browser.driver, username=os.environ.get('USERNAME'), password=os.environ.get('PASSWORD'))