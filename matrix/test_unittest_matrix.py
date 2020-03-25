"""Matrix class unit test.

This module uses unittest and pytest to generate tests for the Matrix class
from matrix.py. Aspects which are tested: initialization, immutability,
mathematical operations, boolean operations, iterations and is hashable.
"""

import unittest

from matrix import Matrix


class TestMatrixCreate(unittest.TestCase):
    """Test the creation of a matrix and that an instance can't be modified.
    """
    def test_initialization(self):
        """Test init function of Matrix."""
        self.assertIsInstance(Matrix((1, 2), (3, 4)), Matrix)
        self.assertIsInstance(Matrix((1, 2), (5.5, 4)), Matrix)

        with self.assertRaises(ValueError):
            Matrix((1, 2), (3, [4, 5, 6]))

        with self.assertRaises(ValueError):
            Matrix((1, 2), (3, 4, 5))

    def test_modification(self):
        """Test that Matrix attribute can't be modified."""
        m = Matrix((1, 1), (2, 2))

        with self.assertRaises(TypeError):
            m._matrix[0] = (1, 2)


class TestMatrixFunctions(unittest.TestCase):
    """Test the built-in functions of Matrix."""
    def test_representation(self):
        """Test __str__  and __repr__ functions."""
        data = (1, 1, 1), (2, 2, 2), (3, 3, 3)
        m = Matrix(*data)

        self.assertEqual(str(m), str(data))
        self.assertEqual(repr(m), f'<Matrix object {hash(m)}>')

    def test_tuples(self):
        """Test tuple which should return the matrix data as tuple."""
        data = (1, 1), (2, 2)
        m = Matrix(*data)

        self.assertEqual(m.tuples, data)

    def test_unity(self):
        """Test unity() which should return a matrix with 1's in the main
        diagonal and 0's elsewhere.
        """
        self.assertEqual(
            Matrix.unity(2), Matrix((1, 0), (0, 1)))

        self.assertEqual(
            Matrix.unity(3), Matrix((1, 0, 0), (0, 1, 0), (0, 0, 1)))

    def test_ones(self):
        """Test ones() which should return a matrix full of 1's."""
        self.assertEqual(
            Matrix.ones(2), Matrix((1, 1), (1, 1)))

        self.assertEqual(
            Matrix.ones(3), Matrix((1, 1, 1), (1, 1, 1), (1, 1, 1)))


class TestMatrixOperators(unittest.TestCase):
    """Test the mathematical and boolean operations supported by Matrix."""
    def test_add(self):
        """Test addition operator."""
        m1 = Matrix.ones(3)
        m2 = Matrix((11, 12, 13), (14, 15, 16), (17, 18, 19))
        m3 = Matrix.ones(2)

        self.assertEqual(m1 + m2,
                         Matrix((12, 13, 14), (15, 16, 17), (18, 19, 20)))

        with self.assertRaises(ValueError):
            m1 + m3

        with self.assertRaises(AttributeError):
            m1 + 10

        with self.assertRaises(AttributeError):
            m1 + 0.5

    def test_sub(self):
        """Test subtraction operator."""
        m1 = Matrix((1, 2), (3, 4))
        m2 = Matrix((5, 6), (7, 8))
        m3 = Matrix.ones(3)

        self.assertEqual(m1 - m2, Matrix((-4, -4), (-4, -4)))

        with self.assertRaises(ValueError):
            m1 - m3

        with self.assertRaises(AttributeError):
            m1 - 10

        with self.assertRaises(AttributeError):
            m1 - 0.5

    def test_mul(self):
        """Test multiplication and reverse mul operators."""
        m1 = Matrix((1, 2), (3, 4))
        m2 = Matrix((5, 6), (7, 8))
        m3 = Matrix.ones(4)

        self.assertEqual(m1 * m2, Matrix((5, 12), (21, 32)))
        self.assertEqual(m1 * 10, Matrix((10, 20), (30, 40)))
        self.assertEqual(m1 * 0.5, Matrix((0.5, 1), (1.5, 2)))

        # reverse mul
        self.assertEqual(10 * m1, Matrix((10, 20), (30, 40)))
        self.assertEqual(0.5 * m1, Matrix((0.5, 1), (1.5, 2)))

        with self.assertRaises(ValueError):
            m1 * m3

        with self.assertRaises(AttributeError):
            m1 * (1, 2)

    def test_div(self):
        """Test true division operator operator."""
        m1 = Matrix((1, 2), (3, 4))
        m2 = Matrix((5, 6), (7, 8))
        m3 = Matrix.ones(4)

        self.assertEqual(m1 / 10, Matrix((0.1, 0.2), (0.3, 0.4)))
        self.assertEqual(m1 / 0.5, Matrix((2, 4), (6, 8)))

        with self.assertRaises(TypeError):
            m1 / m2

        with self.assertRaises(TypeError):
            m1 / m3

        with self.assertRaises(TypeError):
            m1 / (1, 2)

    def test_equal(self):
        """Test equal boolean operator."""
        self.assertEqual(
            Matrix.unity(3), Matrix((1, 0, 0), (0, 1, 0), (0, 0, 1)))

        self.assertEqual(
            Matrix.ones(2), Matrix((1, 1), (1, 1)))

    def test_not_equal(self):
        """Test not equal boolean operator."""
        self.assertNotEqual(Matrix((1, 2), (3, 4)), Matrix((5, 6), (7, 8)))
        self.assertNotEqual(Matrix((1, 2), (3, 4)), Matrix.ones(3))


class TestMatrixIteration(unittest.TestCase):
    """Test iteration support of Matrix."""
    def test_iteration(self):
        """Test __iter__ function."""
        self.assertEqual(tuple(Matrix.ones(2)), ((1, 1), (1, 1)))


class TestMatrixHashable(unittest.TestCase):
    """Test hash support of Matrix."""
    def test_hash(self):
        """Test __hash__ function and uses dictionary keys."""
        d = {Matrix((1, 1), (2, 2)): 2, Matrix((1, 1), (2, 3)): 3}

        self.assertEqual(d, {Matrix((1, 1), (2, 2)): 2,
                             Matrix((1, 1), (2, 3)): 3})

        self.assertNotEqual(hash(Matrix.ones(2)), hash(Matrix.unity(2)))


if __name__ == '__main__':
    unittest.main()
