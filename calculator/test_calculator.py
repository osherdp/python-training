"""Unit test module for testing calculator module."""

import unittest

from calculator import evaluate


class TestOperations(unittest.TestCase):
    """Test the supported operations by the calculator."""
    def test_simple_equations(self):
        """Test basic expressions."""
        self.assertEqual(evaluate("1 + (2 + 3)"), 6.0)
        self.assertEqual(evaluate("(8 - 4) - 6"), -2.0)

        self.assertEqual(evaluate("3* -5"), -15.0)
        self.assertEqual(evaluate("65 /5"), 13.0)

        self.assertEqual(evaluate("9 ^ 0.5"), 3.0)
        self.assertEqual(evaluate("3 % 2"), 1.0)

        self.assertEqual(evaluate("15 @ 60"), 37.5)
        self.assertEqual(evaluate("13 $ 16"), 16.0)
        self.assertEqual(evaluate("13 & 16"), 13.0)

        self.assertEqual(evaluate("~9"), -9.0)
        self.assertEqual(evaluate("5 !"), 120.0)

    def test_precedence(self):
        """Test the order which operations are done."""
        self.assertEqual(evaluate("((1 - 4)^3)*-1"), 27.0)
        self.assertEqual(evaluate("((1 + 2) * 9 + 4! + ~-2)"), 53.0)
        self.assertEqual(evaluate("1 + 2 * 3 + 4 / 0.5 $ (1 / 3)"), 15.0)
        self.assertEqual(evaluate("(0.3 + (4@0.5))$(~0.25 + ((3^-2)@0.5))"),
                         2.55)


class TestEdgeCases(unittest.TestCase):
    """Test rare cases of inputs to see function behavior."""
    def test_wrong_input(self):
        # un-supported operator
        with self.assertRaises(ValueError):
            evaluate("1#1")

        # should be "55*0.2"
        with self.assertRaises(ValueError):
            evaluate("55*.2")

        # should be "~-1"
        with self.assertRaises(ValueError):
            evaluate("--1")

        with self.assertRaises(ValueError):
            evaluate("(((8@5.67) + 1)")

        with self.assertRaises(ValueError):
            evaluate('1+a*76')

        self.assertEqual(evaluate("-1-2*-2"), 3.0)


if __name__ == '__main__':
    unittest.main()
