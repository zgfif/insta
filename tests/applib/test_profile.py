import unittest
from applib.profile import Profile
from applib.browser import Browser
from applib.login import Login
from applib.save_login_info import SaveLoginInfo
from dotenv import load_dotenv
import os



class TestProfile(unittest.TestCase):
    def test_profile(self):
        url = 'https://instagram.com/pashabratanov'

        b = Browser()
        
        load_dotenv()
        
        b.open(url=url)

        Login(driver=b.driver, username=os.getenv('IUSERNAME', ''), password=os.getenv('IPASSWORD', '')).perform()

        SaveLoginInfo(driver=b.driver).process()
        
        Profile(driver=b.driver, filename=f'{url}.xlsx').process()

        b.close()
