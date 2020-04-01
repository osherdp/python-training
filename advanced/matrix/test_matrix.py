"""Unit testing for the Matrix class."""
import unittest

from matrix import Matrix


class TestMatrix(unittest.TestCase):
    """Test that matrix is initialized properly, and it's methods work as expected."""

    def setUp(self):
        """Initialize matrices a and b before tests."""
        self.mat_a = Matrix(((1, 2), (3, 4)))
        self.mat_b = Matrix(((3, 5), (6, 8)))

    def test_initialize(self):
        """Test initialization of matrix."""
        matrix_tuples = ((2, 5), (8, 3))
        my_matrix = Matrix(matrix_tuples)

        self.assertEqual(my_matrix.tuples, matrix_tuples)

        with self.assertRaises(TypeError):
            Matrix("hi")
            Matrix(((1, 2, 3), [4, 5, 6], 5))

        with self.assertRaises(ValueError):
            Matrix(((1, 2, 3), (1, 2, 3)))
            Matrix(((1, 2, 3), (1, 2)))

    def test_unity(self):
        """Test unity method - should return 1 on diagonal, 0 otherwise."""
        self.assertEqual(Matrix.unity(2), Matrix(((1, 0), (0, 1))))
        self.assertEqual(Matrix.unity(3), Matrix(((1, 0, 0), (0, 1, 0), (0, 0, 1))))

    def test_ones(self):
        """Test ones method - should return matrix of 1's at given size."""
        self.assertEqual(Matrix.ones(2), Matrix(((1, 1), (1, 1))))
        self.assertEqual(Matrix.ones(3), Matrix(((1, 1, 1), (1, 1, 1), (1, 1, 1))))

    def test_multiplication(self):
        """Test multiplication by scalar and of matrices."""
        self.assertEqual(self.mat_a * 10, Matrix(((10, 20), (30, 40))))
        self.assertEqual(self.mat_a * 0.9, Matrix(((0.9, 1.8), (2.7, 3.6))))
        self.assertEqual(self.mat_a * self.mat_b, Matrix(((15, 21), (33, 47))))
        self.assertEqual(10 * self.mat_a, Matrix(((10, 20), (30, 40))))

        with self.assertRaises(TypeError):
            self.mat_a * [1, 2, 3]

        with self.assertRaises(ValueError):
            self.mat_a * Matrix(((1, 2, 3), (1, 2, 3), (1, 2, 3)))

    def test_division(self):
        """Test the method for division of matrix by scalar."""
        self.assertEqual(self.mat_a / 2, Matrix(((0.5, 1.0), (1.5, 2.0))))
        self.assertEqual(self.mat_a / 0.1, Matrix(((10, 20), (30, 40))))

        with self.assertRaises(ZeroDivisionError):
            self.mat_a / 0

        with self.assertRaises(TypeError):
            self.mat_a / self.mat_b

    def test_addition(self):
        """Test the method for addition of 2 matrices."""
        # print("test_addition")
        self.assertEqual(self.mat_a + Matrix.unity(2), Matrix(((2, 2), (3, 5))))

        with self.assertRaises(TypeError):
            self.mat_a + 1

        with self.assertRaises(ValueError):
            self.mat_a + Matrix.ones(3)

    def test_subtraction(self):
        """Test the method for subtraction of 2 matrices."""
        # print("test_subtraction")
        self.assertEqual(self.mat_a - self.mat_b, Matrix(((-2, -3), (-3, -4))))

        with self.assertRaises(TypeError):
            self.mat_a - 1

        with self.assertRaises(ValueError):
            self.mat_a - Matrix.ones(3)

    def test_iter(self):
        """Test the iterator of the matrix."""
        # print("test_iter")
        lines = ""
        for line in self.mat_a:
            lines += f"{line}\n"
        self.assertEqual(lines, "(1, 2)\n(3, 4)\n")

    def test_eq(self):
        """Test the equality check between matrices."""
        # print("test_eq")
        self.assertEqual(self.mat_a == self.mat_b, False)

    def test_not_equal(self):
        """Test if two matrices are not equal."""
        # print("test_not_equal")
        self.assertEqual(self.mat_a != self.mat_b, True)

    def test_hash(self):
        """Test if hash method."""
        # print("test_hash")
        dictionary = {Matrix(((1, 1), (2, 2))): 2, Matrix(((1, 1), (2, 3))): 3}

        self.assertEqual(dictionary, {Matrix(((1, 1), (2, 2))): 2,
                                      Matrix(((1, 1), (2, 3))): 3})

    def test_repr(self):
        """Test matrix instance representation."""
        # print("test_repr")
        self.assertEqual(self.mat_a.__repr__(), "Matrix(((1, 2), (3, 4)))")

    def test_str(self):
        """Test textual representation of matrix instance."""
        # print("test_str")
        self.assertEqual(str(self.mat_a), "((1, 2), (3, 4))")


if __name__ == "__main__":
    unittest.main()
