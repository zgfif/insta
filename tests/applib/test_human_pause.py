import unittest
from applib.human_pause import human_pause


class TestHumanPause(unittest.TestCase):
    def test_human_pause(self):
        human_pause()
