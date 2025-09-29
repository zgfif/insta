import unittest
from applib.xlsx_file import XlsxFile
import os
from applib.custom_logger import CustomLogger


class TestXslxFile(unittest.TestCase):
    def test_add_row_to_unexisting_file(self):
        logger = CustomLogger(logpath='test2.log').setup()
        column_names = ('id', 'url', 'comments', 'subs',)

        filepath = 'pashabratanov.xlsx'
        
        self.assertFalse(os.path.exists(filepath))

        data = {
            'id': '1', 
            'url': 'https://www.instagram.com/pashabratanov/', 
            'comments': 'brash_ovyn\nКакая красивая природа.\n164w1 likeReply\nSee translation\nkaradymov_v\nПахан,откуда на желеповской горе хата взялась?)\n164wReply\nSee translation\nbratanovaalena\n❤❤❤\n164w1 likeReply', 
            'subs': 'no subs',
        }

        xlsx_file = XlsxFile(filepath=filepath, logger=logger)
        
        xlsx_file.add_row(data)
        
        self.assertTrue(os.path.exists(filepath))

        rows = xlsx_file.rows()

        self.assertTupleEqual(column_names, rows[0])

        initial_data = tuple(data.values())

        self.assertTupleEqual( initial_data, rows[1])

        os.remove(filepath)



    def test_add_row_to_existing_file(self):
        logger = CustomLogger(logpath='test2.log').setup()
        column_names = ('id', 'url', 'comments', 'subs',)

        filepath = 'pashabratanov_exist.xlsx'
        
        self.assertTrue(os.path.exists(filepath))

        data = {
                'id': '2', 
                'url': 'https://www.instagram.com/pashabratanov/', 
                'comments': 'branches and sky', 
                'subs': 'no subs',
            }

        xlsx_file = XlsxFile(logger=logger, filepath=filepath)
        
        xlsx_file.add_row(data)
        
        self.assertTrue(os.path.exists(filepath))

        rows = xlsx_file.rows()
        second_row = (
            '1', 
            'https://www.instagram.com/pashabratanov/', 
            'brash_ovyn\nКакая красивая природа.\n164w1 likeReply\nSee translation\nkaradymov_v\nПахан,откуда на желеповской горе хата взялась?)\n164wReply\nSee translation\nbratanovaalena\n❤❤❤\n164w1 likeReply', 
            'no subs',
        )
        last_row = tuple(data.values())
        self.assertTupleEqual(column_names, rows[0])
        self.assertTupleEqual(second_row, rows[1])
        self.assertTupleEqual(last_row, rows[-1])

