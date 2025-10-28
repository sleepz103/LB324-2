# tests/test_arithmetic_unit.py
from arithmetic import add
import pytest


def test_add_integers():
    assert add(1, 2) == 3


def test_add_floats():
    assert add(1.5, 2.25) == 3.75


@pytest.mark.parametrize(
    "a, b, expected",
    [(0, 0, 0), (-1, 1, 0), (1000, 2000, 3000)]
)
def test_add_param(a, b, expected):
    assert add(a, b) == expected
