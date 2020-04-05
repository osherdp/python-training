"""Unit testing for the Matrix class."""
import unittest

from matrix import Matrix


class TestMatrix(unittest.TestCase):
    """Test the initialization and methods of the matrix"""

    def setUp(self):
        """Initialize matrices a and b before tests."""
        self.mat_a = Matrix(((1, 2), (3, 4)))
        self.mat_b = Matrix(((3, 5), (6, 8)))

    def test_tuples_property(self):
        """Test tuples property of matrix."""
        self.assertEqual(self.mat_a.matrix_rows, ((1, 2), (3, 4)))

    def test_type_validation(self):
        """Test that only a tuple of tuples is allowed in Matrix."""
        with self.assertRaises(TypeError):
            Matrix(((1, 2, 3), [4, 5, 6], 5))

    def test_value_validation(self):
        """Test that only n*n matrices are allowed."""
        with self.assertRaises(ValueError):
            Matrix(((1, 2, 3), (1, 2, 3)))

    def test_unity_2_dimensional(self):
        """Test unity method on 2 by 2 matrix."""
        self.assertEqual(Matrix.unity(2).matrix_rows, ((1, 0), (0, 1)))

    def test_unity_3_dimensional(self):
        """Test unity method on 3 by 3 matrix."""
        self.assertEqual(Matrix.unity(3).matrix_rows,
                         ((1, 0, 0), (0, 1, 0), (0, 0, 1)))

    def test_ones_2_dimensional(self):
        """Test ones method on 2 by 2 matrix."""
        self.assertEqual(Matrix.ones(2).matrix_rows, ((1, 1), (1, 1)))

    def test_ones_3_dimensional(self):
        """Test ones method on 3 by 3 matrix."""
        self.assertEqual(Matrix.ones(3).matrix_rows,
                         ((1, 1, 1), (1, 1, 1), (1, 1, 1)))

    def test_multiplication_by_int(self):
        """Test multiplication by int."""
        self.assertEqual((self.mat_a * 10).matrix_rows, ((10, 20), (30, 40)))

    def test_multiplication_by_float(self):
        """Test multiplication by float."""
        self.assertEqual((self.mat_a * 0.9).matrix_rows,
                         ((0.9, 1.8), (2.7, 3.6)))

    def test_multiplication_of_matrices(self):
        """Test multiplication of matrices."""
        self.assertEqual((self.mat_a * self.mat_b).matrix_rows,
                         ((15, 21), (33, 47)))

    def test_multiply_scalar_reversed(self):
        """Check reversed multiplication by scalar."""
        self.assertEqual((10 * self.mat_a).matrix_rows,
                         ((10, 20), (30, 40)))

    def test_multiply_matrices_reversed(self):
        """Check reversed multiplication of matrices."""
        self.assertEqual((self.mat_b * self.mat_a).matrix_rows,
                         ((18, 26), (30, 44)))

    def test_multiply_type_validation(self):
        """Test that you can only multiply numbers and matrices."""
        with self.assertRaises(TypeError):
            self.mat_a * [1, 2, 3]

    def test_multiply_value_validation(self):
        """Test that the matrices multiplied are of the same size."""
        with self.assertRaises(ValueError):
            self.mat_a * Matrix(((1, 2, 3), (1, 2, 3), (1, 2, 3)))

    def test_division_by_int(self):
        """Test the method for division of matrix by int."""
        self.assertEqual((self.mat_a / 2).matrix_rows,
                         ((0.5, 1.0), (1.5, 2.0)))

    def test_division_by_float(self):
        """Test the method for division of matrix by float."""
        self.assertEqual((self.mat_a / 0.1).matrix_rows, ((10, 20), (30, 40)))

    def test_division_Type_validation(self):
        """Test that division is only allowed with a number."""
        with self.assertRaises(TypeError):
            self.mat_a / self.mat_b

    def test_addition(self):
        """Test the method for addition of 2 matrices."""
        self.assertEqual((self.mat_a + self.mat_b).matrix_rows,
                         ((4, 7), (9, 12)))

    def test_addition_type_validation(self):
        """Test that addition is only allowed between 2 matrices."""
        with self.assertRaises(TypeError):
            self.mat_a + 1

    def test_addition_value_validation(self):
        """Test that only same sized matrices can be added."""
        with self.assertRaises(ValueError):
            self.mat_a + Matrix.ones(3)

    def test_subtraction(self):
        """Test the method for subtraction of 2 matrices."""
        self.assertEqual((self.mat_a - self.mat_b).matrix_rows,
                         ((-2, -3), (-3, -4)))

    def test_subtraction_type_validation(self):
        """Test that subtraction is only allowed between 2 matrices."""
        with self.assertRaises(TypeError):
            self.mat_a - 1

    def test_subtraction_value_validation(self):
        """Test that you can subtract only same sized matrices."""
        with self.assertRaises(ValueError):
            self.mat_a - Matrix.ones(3)

    def test_iter_a(self):
        """Test the iterator of the matrix a."""
        self.assertEqual(list(self.mat_a), [(1, 2), (3, 4)])

    def test_iter_b(self):
        """Test the iterator of the matrix b."""
        self.assertEqual(list(self.mat_b), [(3, 5), (6, 8)])

    def test1_eq(self):
        """Test the equality check between different matrices."""
        self.assertEqual(self.mat_a == self.mat_b, False)

    def test2_eq(self):
        """Test the equality check between equal matrices."""
        self.assertEqual(self.mat_a == self.mat_a, True)

    def test1_not_equal(self):
        """Test if two different matrices are not equal."""
        self.assertEqual(self.mat_a != self.mat_b, True)

    def test2_not_equal(self):
        """Test if two equal matrices are not equal."""
        self.assertEqual(self.mat_a != self.mat_a, False)

    def test_hash(self):
        """Test if hash method."""
        dictionary = {self.mat_a: 2, self.mat_b: 3}

        self.assertEqual(dictionary, {self.mat_a: 2,
                                      self.mat_b: 3})

    def test_repr(self):
        """Test matrix instance representation."""
        self.assertEqual(self.mat_a.__repr__(), "Matrix(((1, 2), (3, 4)))")

    def test_str(self):
        """Test textual representation of matrix instance."""
        self.assertEqual(str(self.mat_a), "((1, 2), (3, 4))")


if __name__ == "__main__":
    unittest.main()
