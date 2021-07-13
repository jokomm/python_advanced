"""Pytest."""

import pytest

from circle import calculate_circle


def test_circle_positive():
    assert calculate_circle(12) == (75.4, 452.39)


def test_circle_negative():
    assert calculate_circle(-1) == None


def test_circle_zero():
    assert calculate_circle(0) == (0.0, 0.0)


if __name__ == '__main__':
    pytest.main()