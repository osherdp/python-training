import unittest

import pytest
from matrix import Matrix


@pytest.fixture(scope="module")
def db_class(request):
    # set a class attribute on the invoking test context
    request.cls.db = Matrix()


class TestMatrix(unittest.TestCase):
    """Unit tests for Matrix class."""

    def test_initialization(self):
        self.assertIsInstance(Matrix((1, 2), (3, 4)), Matrix)
        self.assertIsInstance(Matrix((1, 2), (5.5, 4)), Matrix)

        with self.assertRaises(ValueError):
            Matrix((1, 2), (3, [4, 5, 6]))

        with self.assertRaises(ValueError):
            Matrix((1, 2), (3, 4, 5))

    def test_modification(self):
        m = Matrix((1, 1), (2, 2))

        with self.assertRaises(TypeError):
            m._matrix[0] = (1, 2)

    def test_str(self):
        data = (1, 1, 1), (2, 2, 2), (3, 3, 3)
        m = Matrix(*data)

        self.assertEqual(str(m), str(data))

    def test_tuples(self):
        data = (1, 1), (2, 2)
        m = Matrix(*data)

        self.assertEqual(m.tuples, data)

    def test_unity(self):
        self.assertEqual(
            Matrix.unity(2), Matrix((1, 0), (0, 1)))

        self.assertEqual(
            Matrix.unity(3), Matrix((1, 0, 0), (0, 1, 0), (0, 0, 1)))

    def test_ones(self):
        self.assertEqual(
            Matrix.ones(2), Matrix((1, 1), (1, 1)))

        self.assertEqual(
            Matrix.ones(3), Matrix((1, 1, 1), (1, 1, 1), (1, 1, 1)))

    def test_add(self):
        m1 = Matrix.ones(3)
        m2 = Matrix((11, 12, 13), (14, 15, 16), (17, 18, 19))
        m3 = Matrix.ones(2)

        self.assertEqual(m1 + m2,
                         Matrix((12, 13, 14), (15, 16, 17), (18, 19, 20)))

        with self.assertRaises(ValueError):
            m1 + m3

        with self.assertRaises(ValueError):
            m1 + 10

        with self.assertRaises(ValueError):
            m1 + 0.5

    def test_sub(self):
        m1 = Matrix((1, 2), (3, 4))
        m2 = Matrix((5, 6), (7, 8))
        m3 = Matrix.ones(3)

        self.assertEqual(m1 - m2, Matrix((-4, -4), (-4, -4)))

        with self.assertRaises(ValueError):
            m1 - m3

        with self.assertRaises(ValueError):
            m1 - 10

        with self.assertRaises(ValueError):
            m1 - 0.5

    def test_mul(self):
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

        with self.assertRaises(TypeError):
            m1 * (1, 2)

    def test_div(self):
        m1 = Matrix((1, 2), (3, 4))
        m2 = Matrix((5, 6), (7, 8))
        m3 = Matrix.ones(4)

        self.assertEqual(m1 / 10, Matrix((0.1, 0.2), (0.3, 0.4)))
        self.assertEqual(m1 / 0.5, Matrix((2, 4), (6, 8)))

        with self.assertRaises(ValueError):
            m1 / m2

        with self.assertRaises(ValueError):
            m1 / m3

        with self.assertRaises(TypeError):
            m1 / (1, 2)

    def test_equal(self):
        self.assertEqual(
            Matrix.unity(3), Matrix((1, 0, 0), (0, 1, 0), (0, 0, 1)))

        self.assertEqual(
            Matrix.ones(2), Matrix((1, 1), (1, 1)))

    def test_not_equal(self):
        self.assertNotEqual(Matrix((1, 2), (3, 4)), Matrix((5, 6), (7, 8)))
        self.assertNotEqual(Matrix((1, 2), (3, 4)), Matrix.ones(3))

    def test_iteration(self):
        self.assertEqual(tuple(Matrix.ones(2)), ((1, 1), (1, 1)))

    def test_hash(self):
        d = {Matrix((1, 1), (2, 2)): 2, Matrix((1, 1), (2, 3)): 3}

        self.assertEqual(d, {Matrix((1, 1), (2, 2)): 2,
                             Matrix((1, 1), (2, 3)): 3})

        self.assertNotEqual(hash(Matrix.ones(2)), hash(Matrix.unity(2)))
