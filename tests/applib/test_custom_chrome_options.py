import unittest
from applib.custom_chrome_options import CustomChromeOptions
from selenium.webdriver.chrome.options import Options



class TestCustomChromeOptions(unittest.TestCase):
    def test_options(self):
        options = CustomChromeOptions().setup()
        self.assertIsInstance(options, Options)
        self.assertEqual(len(options.arguments), 3)
        self.assertEqual(len(options.experimental_options), 2)
