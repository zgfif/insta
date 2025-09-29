import unittest
from applib.save_login_info import SaveLoginInfo
from applib.browser import Browser
from applib.login import Login
from dotenv import load_dotenv
import os



class TestSaveLoginInfo(unittest.TestCase):
    def test_process_save_login_info(self):
        url = 'https://www.instagram.com/geek_culture_store/'
        
        load_dotenv()
        
        b = Browser()
        
        b.open(url=url)
        
        Login(
            driver=b.driver,
            logger=b.logger,
            username=os.getenv('IUSERNAME', ''), 
            password=os.getenv('IPASSWORD', ''),
        ).perform()

        SaveLoginInfo(driver=b.driver, logger=b.logger, save=False).process()

        b.close()
