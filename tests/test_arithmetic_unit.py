# tests/test_arithmetic_unit.py
import os
import sys

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from arithmetic import add  # noqa: E402
import pytest  # noqa: E402


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
