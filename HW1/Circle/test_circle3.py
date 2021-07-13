"""Nose."""

import unittest

import nose2

from circle import calculate_circle


class TestCircle(unittest.TestCase):

    def test_circle_positive(self):
        self.assertEqual(calculate_circle(12), (75.4, 452.39))

    def test_circle_negative(self):
        self.assertEqual(calculate_circle(-1), None)

    def test_circle_zero(self):
        self.assertEqual(calculate_circle(0), (0.0, 0.0))


if __name__ == '__main__':
    nose2.main()
