import pytest
from main import numbers


def test_number_zero():
    assert numbers(0) == 'zero'

def test_number_string():
    assert isinstance(numbers(0), str)

def test_number_unexpected():
    assert numbers(5) == 'Unexpected argument'
