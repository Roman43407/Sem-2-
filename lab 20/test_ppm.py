import unittest
from ppm import Bmr

class TestPPM(unittest.TestCase):

    def setUp(self) -> None:
        self.bmr = Bmr()

    def test_if_calories_are_more_