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

        with Browser() as b:            
            load_dotenv()
            
            b.open(url=url)

            username = os.getenv('IUSERNAME', '')

            password = os.getenv('IPASSWORD', '')

            Login(driver=b.driver, logger=b.logger, username=username, password=password).perform()

            SaveLoginInfo(driver=b.driver, logger=b.logger).process()
            
            Profile(driver=b.driver, logger=b.logger, filename=f'{url}.xlsx').process()
