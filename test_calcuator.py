"""Calculator Tests."""

import unittest
import Calculator_exercise


class TestCalc(unittest.TestCase):
    """Tests solving different equations"""

    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual(Calculator_exercise.add('1+2'), '3')

    def test_subtract(self):
        self.assertEqual(Calculator_exercise.subtract('10-5'), '5')

    def test_multiply(self):
        self.assertEqual(Calculator_exercise.multiply('20*5'), '100')

    def test_divide(self):
        self.assertEqual(Calculator_exercise.divide('15/2'), '7.5')

    def test_power(self):
        self.assertEqual(Calculator_exercise.power('3^3'), '27')

    def test_modulo(self):
        self.assertEqual(Calculator_exercise.modulo('120%6'), '0')
        self.assertEqual(Calculator_exercise.modulo('120%7'), '1')

    def test_minimum(self):
        self.assertEqual(Calculator_exercise.minimum('10&5'), '5')
        self.assertEqual(Calculator_exercise.minimum('-4&-8'), '-8')

    def test_maximum(self):
        self.assertEqual(Calculator_exercise.maximum('10$5'), '10')
        self.assertEqual(Calculator_exercise.maximum('-4$-8'), '-4')

    def test_average(self):
        self.assertEqual(Calculator_exercise.average('20@10'), '15.0')

    def test_negate(self):
        self.assertEqual(Calculator_exercise.negate('~10'), '-10')
        self.assertEqual(Calculator_exercise.negate('~-10'), '10')

    def test_factorial(self):
        self.assertEqual(Calculator_exercise.factorial('5!'), '120')

    def test_parenthesis(self):
        self.assertEqual(Calculator_exercise.parenthesis('(1+2)'), '3')
        self.assertEqual(Calculator_exercise.parenthesis('(1+(2+3))'), '6')
        self.assertEqual(Calculator_exercise.parenthesis('(1+2)+(3+4)'), '10')
        self.assertEqual(Calculator_exercise.parenthesis('(1-2)+3+(4+(5+6))'), '17')

    def test_space_remove(self):
        self.assertEqual(Calculator_exercise.space_remove('1 2'), '12')
