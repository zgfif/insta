from typing import Sequence
from applib.browser import Browser
from applib.login import Login
from applib.save_login_info import SaveLoginInfo
from applib.profile import Profile
from dotenv import load_dotenv
import os




class ExtractAndSave:
    def __init__(self, urls: Sequence) -> None:
        self._browser = Browser()
        self._urls = urls



    def perform(self) -> None:
        """
        Process every url and save to file.
        """
        load_dotenv()

        if not self._urls:
            print('the urls list is empty.')
            return
    
        # processing the first url
        self._browser.open(url=self._urls[0])
        
        Login(driver=self._browser.driver, 
                username=os.getenv('IUSERNAME', ''), 
                password=os.getenv('IPASSWORD', '')
        ).perform()

        SaveLoginInfo(driver=self._browser.driver).process()

        Profile(driver=self._browser.driver, filename=self._filename(url=self._urls[0])).process()

        # process other urls
        for url in self._urls[1:]:
            self._browser.open(url=url)

            Profile(driver=self._browser.driver, filename=self._filename(url=url)).process()
        
        if self._browser:
            self._browser.close()



    def _filename(self, url: str) -> str:
        """
        Return xlsx-filename based on the url.
        Example:
        >>>url = 'https://instagram.com/pashabratanov/'
        >>>_filename(url) -> pashabratanov.xlsx
        """
        profile = url.rstrip('/').split('/')[-1]
        return profile + '.xlsx'
