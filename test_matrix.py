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

    def test_add(self):
        z = Matrix(((5, 5), (5, 5)))
        self.assertEqual(self.x + self.y, z)
        t = Matrix(((-1, -1), (-1, -1)))
        f = Matrix(((-2, -3), (-4, -5)))
        self.assertEqual(self.x + f, t)
        self.assertEqual(self.three + self.three, Matrix(((2, 4, 0), (0, 2, 4), (4, 0, 2))))

    def test_mul(self):
        self.assertEqual(self.zeros * self.x, self.zeros)
        s = Matrix(((1, 1, 1), (1, 1, 1), (1, 1, 1)))
        self.assertEqual(s * self.three, Matrix(((3, 3, 3), (3, 3, 3), (3, 3, 3))))
        self.assertEqual(self.x * self.y, Matrix(((8, 5), (20, 13))))
        self.assertEqual(self.tens * self.half, self.tens)
        self.assertEqual(self.negative * self.negative, Matrix(((2, 2), (2, 2))))

    def test_scalar_mul(self):
        self.assertEqual(self.x * 3, Matrix(((3, 6), (9, 12))))
        self.assertEqual(self.x * 0, Matrix(((0, 0), (0, 0))))
        self.assertEqual(self.x * -0.5, Matrix(((-0.5, -1), (-1.5, -2))))

    def test_sub(self):
        z = Matrix(((-3, -1), (1, 3)))
        self.assertEqual(self.x - self.y, z)
        t = Matrix(((3, 5), (7, 9)))
        f = Matrix(((-2, -3), (-4, -5)))
        self.assertEqual(self.x - f, t)
        self.assertEqual(self.three - self.three, Matrix(((0, 0, 0), (0, 0, 0), (0, 0, 0))))

    def test_div(self):
        self.assertEqual(self.x / 2, Matrix(((0.5, 1), (1.5, 2))))
        self.assertEqual(self.x / 0.5, Matrix(((2, 4), (6, 8))))
        self.assertEqual(self.x / -1, Matrix(((-1, -2), (-3, -4))))

    def test_unity(self):
        self.assertEqual(Matrix.unity(3), Matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1))))

    def test_ones(self):
        self.assertEqual(Matrix.ones(3), Matrix(((1, 1, 1), (1, 1, 1), (1, 1, 1))))


if __name__ == '__main__':
    unittest.main()
