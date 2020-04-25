"""Matrix tests."""

import unittest
from matrix import Matrix


class TestMatrix(unittest.TestCase):
    """Tests my matrix methods."""

    def setUp(self):
        self.a = Matrix(((1, 2), (3, 4)))
        self.b = Matrix(((5, 6), (7, 8)))
        self.c = Matrix(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
        self.d = Matrix(((2, 3, 4), (5, 6, 7), (7, 8, 9)))

    def test_init(self):
        with self.assertRaises(ValueError):
            self.e = Matrix(((1, 2), (1, 2, 3)))  # not nXn

    def test_add(self):
        self.assertEqual(Matrix.__add__(self.a, self.b),
                         Matrix(((6, 8), (10, 12))))
        self.assertEqual(Matrix.__add__(self.c, self.d),
                         Matrix(((3, 5, 7), (9, 11, 13), (14, 16, 18))))

    def test_add_raises(self):
        with self.assertRaises(ValueError):
            Matrix.__add__(self.a, self.c)

    def test_sub(self):
        self.assertEqual(Matrix.__sub__(self.a, self.b),
                         Matrix(((-4, -4), (-4, -4))))
        self.assertEqual(Matrix.__sub__(self.d, self.c),
                         Matrix(((1, 1, 1), (1, 1, 1), (0, 0, 0))))

    def test_sub_raises(self):
        with self.assertRaises(ValueError):
            Matrix.__sub__(self.a, self.c)

    def test_mul(self):
        self.assertEqual(Matrix.__mul__(self.a, self.b),
                         Matrix(((19, 22), (43, 50))))
        self.assertEqual(
            Matrix.__mul__(self.c, self.d),
            Matrix(((33, 39, 45), (75, 90, 105), (117, 141, 165))))
        self.assertEqual(
            Matrix.__mul__(self.b, self.a),
            Matrix(((23, 34), (31, 46))))

    def test_rmul(self):
        self.assertEqual(Matrix.__rmul__(self.c, 2),
                         Matrix(((2, 4, 6), (8, 10, 12), (14, 16, 18))))

    def test_truediv(self):
        self.assertEqual(Matrix.__truediv__(self.a, 4),
                         Matrix(((0.25, 0.5), (0.75, 1.0))))
        self.assertEqual(Matrix.__truediv__(self.c, 2),
                         Matrix(((0.5, 1, 1.5), (2, 2.5, 3), (3.5, 4, 4.5))))
        # test division by a matrix
        self.assertEqual(Matrix.__truediv__(self.a, self.c), None)

    def test_eq(self):
        self.assertTrue(self.a != self.b)
        self.assertFalse(self.a == self.b)

    def test_unity(self):
        self.assertEqual(Matrix.unity(2), Matrix(((1, 0), (0, 1))))
        self.assertEqual(Matrix.unity(3),
                         Matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1))))

    def test_ones(self):
        self.assertEqual(Matrix.ones(2), Matrix(((1, 1), (1, 1))))
        self.assertEqual(Matrix.ones(3),
                         Matrix(((1, 1, 1), (1, 1, 1), (1, 1, 1))))

    def test_tuples(self):
        self.assertEqual(self.a.tuples, ((1, 2), (3, 4)))


if __name__ == '__main__':
    unittest.main()
