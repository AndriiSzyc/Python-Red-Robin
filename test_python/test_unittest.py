import unittest
from unittest import TestCase

from main import numbers

class TestNumbers(TestCase):

    # def _create_numbers(number: int):
    #     return numbers(number)

    def setUp(self) -> None:
        self.number_0 = self.numbers(0)
        self.number_1 = self.numbers(1)
        self.number_2 = self.numbers(2)
        self.number_3 = self.numbers(3)
        self.number_4 = self.numbers(4)

    def test_number_string(self):
        self.assertEqual(self.number_0, 'zero')
счч
