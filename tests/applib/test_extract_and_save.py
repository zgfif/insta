import unittest
from applib.extract_and_save import ExtractAndSave



class TestExtractAndSave(unittest.TestCase):
    def test_process_one_url(self):
        urls = ['https://instagram.com/pashabratanov/', 'https://www.instagram.com/mikeinsdevon/']

        ExtractAndSave(urls=urls).perform()
