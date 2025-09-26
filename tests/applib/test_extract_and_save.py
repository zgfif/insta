import unittest
from applib.extract_and_save import ExtractAndSave



class TestExtractAndSave(unittest.TestCase):
    def test_process_one_url(self):
        urls = ['https://instagram.com/pashabratanov',]

        ExtractAndSave(urls=urls).perform()
