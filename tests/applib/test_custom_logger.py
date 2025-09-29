import unittest
from applib.custom_logger import CustomLogger
import os
import logging



class TestCustomLogger(unittest.TestCase):
    def test_create_empty_logfile(self):
        logpath = 'logs/test.log'
        
        self.assertFalse(os.path.exists(logpath))
        
        logger = CustomLogger(logpath=logpath).setup()
        
        self.assertIsInstance(logger, logging.Logger)
                
        self.assertTrue(os.path.exists(logpath))

        with open(logpath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 0)

        os.remove(logpath)


    def test_add_to_logfile(self):
        message = 'Test info message.'

        logpath = 'logs/test2.log'
        
        logger = CustomLogger(logpath=logpath).setup()
        
        logger.info(message)

        with open(logpath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        self.assertIn(message, lines[-1])
