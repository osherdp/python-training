import unittest
from Matrix import Matrix


class Test_matrix(unittest.TestCase):
    def setUp(self):
        self.x = Matrix(((1, 2), (3, 4)))
        self.y = Matrix(((4, 3), (2, 1)))
        self.zeros = Matrix(((0, 0), (0, 0)))
        self.tens = Matrix(((10, 10), (10, 10)))
        self.negative = Matrix(((-1, -1), (-1, -1)))
        self.three = Matrix(((1, 2, 0), (0, 1, 2), (2, 0, 1)))
        self.half = Matrix(((0.5, 0.5), (0.5, 0.5)))

    def test_init_failed(self):
        with self.assertRaises(ValueError):
            (Matrix("hello"))
        with self.assertRaises(ValueError):
            (Matrix(((2, 1), (1, 2, 3))))

    def test_add(self):
        self.assertEqual(self.x + self.y, Matrix(((5, 5), (5, 5))))
        self.assertEqual(self.x + Matrix(((-2, -3), (-4, -5))), Matrix(((-1, -1), (-1, -1))))
        self.assertEqual(self.three + self.three, Matrix(((2, 4, 0), (0, 2, 4), (4, 0, 2))))

    def test_add_failed(self):
        with self.assertRaises(SyntaxError):
            (Matrix.__add__(self.x, 2))

    def test_mul(self):
        self.assertEqual(self.zeros * self.x, self.zeros)
        s = Matrix(((1, 1, 1), (1, 1, 1), (1, 1, 1)))
        self.assertEqual(s * self.three, Matrix(((3, 3, 3), (3, 3, 3), (3, 3, 3))))
        self.assertEqual(self.tens * self.half, self.tens)
        self.assertEqual(self.negative * self.negative, Matrix(((2, 2), (2, 2))))
        self.assertEqual(self.x * 3, Matrix(((3, 6), (9, 12))))
        self.assertEqual(self.x * 0, Matrix(((0, 0), (0, 0))))
        self.assertEqual(self.x * -0.5, Matrix(((-0.5, -1), (-1.5, -2))))

    def test_mul_failed(self):
        with self.assertRaises(SyntaxError):
            (Matrix.__mul__(self.x, "l"))

    def test_sub(self):
        self.assertEqual(self.x - self.y, Matrix(((-3, -1), (1, 3))))
        self.assertEqual(self.x - Matrix(((-2, -3), (-4, -5))), Matrix(((3, 5), (7, 9))))
        self.assertEqual(self.three - self.three, Matrix(((0, 0, 0), (0, 0, 0), (0, 0, 0))))

    def test_sub_failed(self):
        with self.assertRaises(SyntaxError):
            (Matrix.__sub__(self.x, 2))

    def test_div(self):
        self.assertEqual(self.x / 2, Matrix(((0.5, 1), (1.5, 2))))
        self.assertEqual(self.x / 0.5, Matrix(((2, 4), (6, 8))))
        self.assertEqual(self.x / -1, Matrix(((-1, -2), (-3, -4))))

    def test_div_failed(self):
        with self.assertRaises(TypeError):
            (Matrix.__truediv__(self.x, self.x))

    def zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            (Matrix.__truediv__(self.x, 0))

    def test_unity(self):
        self.assertEqual(Matrix.unity(3), Matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1))))

    def test_ones(self):
        self.assertEqual(Matrix.ones(3), Matrix(((1, 1, 1), (1, 1, 1), (1, 1, 1))))

    def test_eq(self):
        self.assertTrue(self.x.__eq__(self.x))
        self.assertFalse(self.x.__eq__(self.y))


if __name__ == '__main__':
    unittest.main()
