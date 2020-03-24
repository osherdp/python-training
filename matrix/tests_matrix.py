import unittest

from matrix import Matrix


class TestMatrix(unittest.TestCase):
    def test_initialization(self):
        Matrix((1, 2), (3, 4))
        Matrix((1, 2), (5.5, 4))

        with self.assertRaises(ValueError):
            Matrix((1, 'a'), (3, 4))

        with self.assertRaises(ValueError):
            Matrix((1, 2), (3, [4, 5, 6]))

        with self.assertRaises(ValueError):
            Matrix((1, 2), (3, 4, 5))

    def test_modification(self):
        m = Matrix((1, 1), (2, 2))

        with self.assertRaises(AttributeError):
            m._matrix = ((1, 2), (3, 4))

        with self.assertRaises(AttributeError):
            m._matrix = "hello world!"

    def test_str(self):
        m = Matrix((1, 1, 1), (2, 2, 2), (3, 3, 3))

        self.assertEqual(str(m), str(((1, 1, 1), (2, 2, 2), (3, 3, 3))))

    def test_tuples(self):
        m = Matrix((1, 1), (2, 2))

        self.assertEqual(m.tuples, ((1, 1), (2, 2)))

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
        m2 = Matrix.ones(3)
        m3 = Matrix.ones(2)

        self.assertEqual(m1 + m2, Matrix((2, 2, 2), (2, 2, 2), (2, 2, 2)))

        with self.assertRaises(ValueError):
            _ = m1 + m3

        with self.assertRaises(ValueError):
            _ = m1 + 10

        with self.assertRaises(ValueError):
            _ = m1 + 0.5

        with self.assertRaises(ValueError):
            _ = m1 - "0.5"

    def test_sub(self):
        m1 = Matrix((1, 2), (3, 4))
        m2 = Matrix((5, 6), (7, 8))
        m3 = Matrix.ones(3)

        self.assertEqual(m1 - m2, Matrix((-4, -4), (-4, -4)))

        with self.assertRaises(ValueError):
            _ = m1 - m3

        with self.assertRaises(ValueError):
            _ = m1 - 10

        with self.assertRaises(ValueError):
            _ = m1 - 0.5

        with self.assertRaises(ValueError):
            _ = m1 - "0.5"

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
            _ = m1 * m3

        with self.assertRaises(ValueError):
            _ = m1 * "hi"

        with self.assertRaises(ValueError):
            _ = m1 * [1, 2, 3]

        with self.assertRaises(ValueError):
            _ = m1 * ["hi", "i'm", "a test"]

        with self.assertRaises(ValueError):
            _ = m1 * (1, 2)

        with self.assertRaises(ValueError):
            _ = m1 * ("hi", "i'm", "a test")

    def test_div(self):
        m1 = Matrix((1, 2), (3, 4))
        m2 = Matrix((5, 6), (7, 8))
        m3 = Matrix.ones(4)

        self.assertEqual(m1 / m2, Matrix((0.2, 2 / 6), (3 / 7, 0.5)))
        self.assertEqual(m1 / 10, Matrix((0.1, 0.2), (0.3, 0.4)))
        self.assertEqual(m1 / 0.5, Matrix((2, 4), (6, 8)))

        with self.assertRaises(ValueError):
            _ = m1 / m3

        with self.assertRaises(ValueError):
            _ = m1 / "hi"

        with self.assertRaises(ValueError):
            _ = m1 / [1, 2, 3]

        with self.assertRaises(ValueError):
            _ = m1 / ["hi", "i'm", "a test"]

        with self.assertRaises(ValueError):
            _ = m1 / (1, 2)

        with self.assertRaises(ValueError):
            _ = m1 / ("hi", "i'm", "a test")

    def test_equal(self):
        self.assertTrue(
            Matrix.unity(3) == Matrix((1, 0, 0), (0, 1, 0), (0, 0, 1)))

        self.assertFalse(Matrix((1, 2), (3, 4)) == Matrix((5, 6), (7, 8)))
        self.assertFalse(Matrix((1, 2), (3, 4)) == Matrix.ones(3))

    def test_not_equal(self):
        self.assertTrue(
            Matrix.unity(3) != Matrix.ones(3))

        self.assertTrue(
            Matrix.unity(3) != Matrix.ones(4))

        self.assertFalse(Matrix((1, 2), (3, 4)) != Matrix((1, 2), (3, 4)))

    def test_iteration(self):
        self.assertNotEqual(list(iter(Matrix.ones(3))), [])

        for line in Matrix.ones(2):
            self.assertEqual(line, (1, 1))

    def test_hash(self):
        d = {Matrix((1, 1), (2, 2)): 2, Matrix((1, 1), (2, 3)): 3}

        self.assertEqual(d, {Matrix((1, 1), (2, 2)): 2,
                             Matrix((1, 1), (2, 3)): 3})

        self.assertNotEqual(hash(Matrix.ones(2)), hash(Matrix.unity(2)))


if __name__ == '__main__':
    unittest.main()
