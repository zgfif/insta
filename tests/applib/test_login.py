import unittest
from applib.login import Login
from applib.browser import Browser
import os
from dotenv import load_dotenv
from time import sleep



class TestLogin(unittest.TestCase):
    def test_login(self):
        url = 'https://instagram.com/pashabratanov'

        browser = Browser()
        
        browser.open(url=url)
        
        load_dotenv()
        
        sleep(14)
        username = os.getenv('IUSERNAME', '')
        password = os.getenv('IPASSWORD', '')

        login = Login(driver=browser.driver, 
                      username=username, 
                      password=password,
                      )

        login.perform()

        browser.close()
