"""Unit test module for testing calculator module."""

import unittest

from calculator import Calculator


class TestOperations(unittest.TestCase):
    """Test the supported operations by the calculator."""
    def __init__(self, *args, **kwargs):
        super(TestOperations, self).__init__(*args, **kwargs)
        self.c = Calculator()

    def test_basic(self):
        """Test the basic operations."""
        self.c.expression = "1 + 2 + 3"
        self.assertEqual(self.c.calculate(), 6.0)

        self.c.expression = "8 - 4 - 6"
        self.assertEqual(self.c.calculate(), -2.0)

        self.c.expression = "3* -5"
        self.assertEqual(self.c.calculate(), -15.0)

        self.c.expression = "65 /5"
        self.assertEqual(self.c.calculate(), 13.0)

    def test_advanced(self):
        """Test the advanced operations."""
        self.c.expression = "9 ^ 0.5"
        self.assertEqual(self.c.calculate(), 3.0)

        self.c.expression = "3 % 2"
        self.assertEqual(self.c.calculate(), 1.0)

        self.c.expression = "15 @ 60"
        self.assertEqual(self.c.calculate(), 37.5)

        self.c.expression = "13 $ 16"
        self.assertEqual(self.c.calculate(), 16.0)

        self.c.expression = "13 & 16"
        self.assertEqual(self.c.calculate(), 13.0)

        self.c.expression = "~9"
        self.assertEqual(self.c.calculate(), -9.0)

        self.c.expression = "5 !"
        self.assertEqual(self.c.calculate(), 120.0)

    def test_precedence(self):
        """Check the order which operations are done."""
        self.c.expression = "1 + 2 * 3 + 4 / 0.5 $ (1 / 3)"
        self.assertEqual(self.c.calculate(), 15.0)

        self.c.expression = "((1 - 4)^3)*-1"
        self.assertEqual(self.c.calculate(), 27.0)


if __name__ == '__main__':
    unittest.main()
