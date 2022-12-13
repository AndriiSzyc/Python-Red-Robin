from unittest import TestCase

from signers import Signer


class TestNumbers(TestCase):
    """Asserts types
    self.assertEqual(a, b) -> a==b
    self.assertNotEqual(a, b) -> a!=b
    self.assertTrue(a) -> bool(a) is True
    self.assertFalse(a) -> bool(a) is False
    self.assertIs(a, b) -> a is b
    self.assertIsNot(a, b) -> a is not b
    self.assertIsNone(a) -> a is None
    self.assertIn(a, b) -> a in b
    self.assertNotIn(a, b) -> a  not in b
    self.assertIsInstance(a, b) -> isinstance(a, b)
    """

    def _create_numbers(number: int):
        return numbers()

    def setUp(self) -> None:
        self.number_0 = numbers(0)
        self.number_1 = numbers(1)
        self.number_2 = numbers(2)
        self.number_3 = numbers(3)
        self.number_4 = numbers(4)
        self.number_5 = numbers(5)

    def test_number_string(self):
        self.assertIsInstance(self.number_0, str)

    def test_number(self):
        self.assertEqual(self.number_0, "zero")
        self.assertEqual(self.number_1, "one")
        self.assertEqual(self.number_2, "two")
        self.assertEqual(self.number_3, "three")
        self.assertEqual(self.number_4, "four")

    def test_unexpected_argumetn(self):
        self.assertIsNotNone(self.number_5)
        self.assertEqual(self.number_5, "Unexpected argument")
