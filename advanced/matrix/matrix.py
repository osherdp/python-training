class Matrix:
    """A class used to represent an immutable n*n matrix.

        Attributes:
            __matrix (tuple): a tuple of tuples representing a matrix.
    """
    def _is_even(self):
        """Check that matrix has equal number of rows and columns."""
        for mat_tuple in self.__matrix:
            if len(mat_tuple) != len(self.__matrix):
                raise ValueError("The matrix is not n*n")

    def _is_tuple(self):
        """Check that matrix is made of a tuple of tuples."""
        if isinstance(self.__matrix, tuple):
            for mat_tuple in self.__matrix:
                if not isinstance(mat_tuple, tuple):
                    raise TypeError("Object is not a tuple's matrix.")

        else:
            raise TypeError("Object is not a tuple's matrix.")

    def is_good_matrix(self):
        """Check that matrix given is valid."""
        self._is_tuple()
        self._is_even()

    def __init__(self, matrix_tuples):
        """Initialize instance of matrix and check for validity."""
        self.__matrix = matrix_tuples
        self.is_good_matrix()

    @property
    def tuples(self):
        """Return the matrix."""
        return self.__matrix

    @classmethod
    def unity(cls, size):
        """Create a unity tuple.

        Args:
            size (int): the number of rows and columns for new matrix.

        Returns:
            tuple: New tuple of tuples, matrix, main diagonal is 1, the rest 0.
        """
        lis = [tuple(1 if col == row else 0 for col in range(size))
               for row in range(size)]
        return cls(tuple(lis))

    @classmethod
    def ones(cls, size):
        """Create a new matrix in the given size filled with 1.

        Args:
            size: The size of the new matrix.

        Returns:
            tuple: Tuple of tuples filled with ones.
        """
        ones_mat = (((1,) * size,) * size)
        return cls(ones_mat)

    def _multiplication(self, sec_mat):
        """Calculate the multiplication of 2 matrices.

            Args:
                sec_mat (tuple): A matrix to multiply with.

            Returns:
                tuple: Result matrix of the multiplication between 2 matrices.
        """
        result = [tuple(sum(n_a * n_b for n_a, n_b in zip(a_row, b_col))
                        for b_col in zip(*sec_mat))
                  for a_row in self]
        return tuple(result)

    def _multiply_by_scalar(self, scalar):
        """Return new matrix multiplied by scalar."""
        return Matrix(tuple((tuple((num * scalar for num in each_tuple))
                             for each_tuple in self)))

    def __mul__(self, other):
        """Multiply matrix by scalar or another matrix.

        Args:
            other (int/Matrix): Scalar or another matrix.

        Returns:
            Matrix: The result matrix.
        """
        if isinstance(other, Matrix):
            return self._multiplication(other.tuples)
        return self._multiply_by_scalar(other)

    def __rmul__(self, other):
        """Return the regular multiplication of the objects when in reversed order."""
        return self * other

    def __truediv__(self, other):
        """Return new matrix divided by scalar."""
        if other == 0:
            raise ZeroDivisionError("Cannot divide by 0.")
        return self * (1 / other)

    def __add__(self, other):
        """Return result of 2 matrices addition."""
        add_result = ((tuple((x + y for x, y in zip(tuple1, tuple2))))
                      for tuple1, tuple2 in zip(self, other))
        return Matrix(tuple(add_result))

    def __sub__(self, other):
        """Return result of 2 matrices subtraction."""
        return self + (-1 * other)

    def __iter__(self):
        """Return an iterator on the matrix"""
        return iter(self.tuples)

    def __eq__(self, other):
        """Check for equality between matrices."""
        return self.tuples == other

    def __ne__(self, other):
        """Check if the two matrices are not equal."""
        return self.tuples != other

    def __hash__(self):
        """Get the hash value of matrix."""
        return hash(self.tuples)

    def __repr__(self):
        """Return a representation of the matrix instance."""
        return f"{self.__class__.__name__}({self.tuples})"

    def __str__(self):
        """Return string representation of the matrix instance."""
        return f"{self.tuples}"
