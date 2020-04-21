"""Unit test module for testing calculator module."""

import unittest

from calculator import evaluate


class TestOperations(unittest.TestCase):
    """Test the supported operations by the calculator."""
    def test_basic(self):
        """Test the basic operations."""
        self.assertEqual(evaluate("1 + (2 + 3)"), 6.0)
        self.assertEqual(evaluate("(8 - 4) - 6"), -2.0)

        self.assertEqual(evaluate("3* -5"), -15.0)
        self.assertEqual(evaluate("65 /5"), 13.0)

    def test_advanced(self):
        """Test the advanced operations."""
        self.assertEqual(evaluate("9 ^ 0.5"), 3.0)
        self.assertEqual(evaluate("3 % 2"), 1.0)

        self.assertEqual(evaluate("15 @ 60"), 37.5)
        self.assertEqual(evaluate("13 $ 16"), 16.0)
        self.assertEqual(evaluate("13 & 16"), 13.0)

        self.assertEqual(evaluate("~9"), -9.0)
        self.assertEqual(evaluate("5 !"), 120.0)

    def test_precedence(self):
        """Check the order which operations are done."""
        self.assertEqual(evaluate("((1 - 4)^3)*-1"), 27.0)
        self.assertEqual(evaluate("((1 + 2) * 9 + 4! + ~-2)"), 53.0)
        self.assertEqual(evaluate("1 + 2 * 3 + 4 / 0.5 $ (1 / 3)"), 15.0)
        self.assertEqual(evaluate("(0.3 + (4@0.5))$(~0.25 + ((3^-2)@0.5))"),
                         2.55)


if __name__ == '__main__':
    unittest.main()
