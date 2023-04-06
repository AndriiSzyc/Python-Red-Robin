from unittest import TestCase
from signers import Signer


class Test_Singers(TestCase):
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

    def _create_signer(secret: str, salt: str):
        return Signer()

    def setUp(self) -> None:
        self.sign = Signer(secret="sec", salt="slt")

    def test_chek_isinstance_input(self):
        payload = {"name": "Ozzy"}
        self.assertIsInstance(payload, dict)

    def test_chek_work_correct_input(self):
        payload = {"name": "Ozzy"}
        self.assertTrue(self.sign.jwt_encode(payload))

    def test_jwt_encode(self):
        payload = {"name": "Ozzy"}
        encode = self.sign.jwt_encode(payload)
        self.assertIsNot(payload, encode)

    def test_jwt_decode(self):
        payload = {"name": "Ozzy"}
        encode = self.sign.jwt_encode(payload)
        decode = self.sign.jwt_decode(encode)
        self.assertEqual(decode, payload)

    def test_itsdangerous_encode(self):
        payload = {"name": "Ozzy"}
        encode = self.sign.itsdangerous_encode(payload)
        self.assertIsNot(payload, encode)

    def test_itsdangerous_decode(self):
        payload = {"name": "Ozzy"}
        encode = self.sign.itsdangerous_encode(payload)
        decode = self.sign.itsdangerous_decode(encode)
        self.assertEqual(decode, payload)
