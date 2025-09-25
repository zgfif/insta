import unittest
from applib.text_from_image import TextFromImage



class TestTextFromImage(unittest.TestCase):
    def test_extract_txt(self):
        imagepath = './video/frame_0001.png'
        
        text = TextFromImage(imagepath=imagepath).extract()
        
        self.assertEqual(text, 'Они создают безумную')
