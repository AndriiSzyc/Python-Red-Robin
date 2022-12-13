import pytest
from signers import Signer

@pytest.fixture
def sign():
    return Signer(secret='sec', salt='slt')

def test_chek_isinstance_input(sign):
    payload = {'name': 'Ozzy'}
    assert isinstance(payload, dict)


def test_jwt_encode(sign):
    payload = {'name': 'Ozzy'}
    encode = sign.jwt_encode(payload)
    assert payload != encode


def test_jwt_decode(sign):
    payload = {'name': 'Ozzy'}
    encode = sign.jwt_encode(payload)
    decode = sign.jwt_decode(encode)
    assert decode == payload


def test_itsdangerous_encode(sign):
    payload = {'name': 'Ozzy'}
    encode = sign.itsdangerous_encode(payload)
    assert payload != encode


def test_itsdangerous_decode(sign):
    payload = {'name': 'Ozzy'}
    encode = sign.itsdangerous_encode(payload)
    decode = sign.itsdangerous_decode(encode)
    assert decode == payload