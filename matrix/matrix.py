"""Matrix data type class."""


def _validate_operator_method(func):
    """Validate the other matrix given, in an operator method.

    Args:
        func (function): the operator function to validate.

    Returns:
        A wrapper function, which does the validation.
    """
    def operation_wrapper(self, other):
        dimension = len(self.tuples)

        if len(other.tuples) != dimension:
            raise ValueError(
                f"Dimension {len(other.tuples)} don't match {dimension}")

        return func(self, other)

    return operation_wrapper


class Matrix:
    """An immutable object representing a matrix data-type.

    Attributes:
        _matrix (tuple): contains the data about the matrix. Each line of
            the matrix is represented by a tuple.
    note:
        This implementation only supports squared matrices (n * n).
    """

    def __init__(self, lines):
        self._validate(lines)
        self._matrix = lines

    def _validate(self, data: tuple):
        """Check if the data given is valid.

        note:
            Valid data is defined if it contains tuples of the same length,
            Supports only squared matrices.
        """
        if not all([len(line) == len(data) for line in data]):
            raise ValueError("Matrix must be even-sided")

    @classmethod
    def unity(cls, dimension: int):
        """Generate a matrix with a main diagonal of 1's, elsewhere 0's."""
        unity_matrix = ()

        for i in range(dimension):
            unity_matrix += ((0,) * i + (1,) + (0,) * (dimension - i - 1),)

        return cls(unity_matrix)

    @classmethod
    def ones(cls, dimension):
        """Generate a matrix full of 1's."""
        return cls(((1,) * dimension,) * dimension)

    def __repr__(self):
        return f"'{self.__class__.__name__}({self._matrix})'"

    def __str__(self):
        """Return a string presentation of the matrix instance."""
        return repr(self._matrix)

    @property
    def tuples(self):
        """Return the matrix instance as a tuple of tuples."""
        return self._matrix

    @_validate_operator_method
    def _add_matrix(self, other):
        """Add two matrices.

        Args:
            other (Matrix): the other matrix to operate on.

        Returns:
            Matrix: the result of the addition.
        """
        dimension = len(self.tuples)
        empty_data = tuple([] for i in range(dimension))

        for i in range(dimension):
            for j in range(dimension):
                empty_data[i].append(self.tuples[i][j] + other.tuples[i][j])

        return Matrix(tuple(map(tuple, empty_data)))

    @_validate_operator_method
    def _matrix_mul_matrix(self, other):
        """Multiply two matrices.

        Args:
            other (Matrix): the other matrix to multiply.

        Returns:
            Matrix: the product.
        """
        dimension = len(self.tuples)
        empty_data = tuple([0] * dimension for i in range(dimension))

        for i in range(dimension):
            for k in range(dimension):
                for j in range(dimension):
                    empty_data[i][j] += self.tuples[i][k] * other.tuples[k][j]

        return Matrix(tuple(map(tuple, empty_data)))

    def __add__(self, other):
        """Add two matrices."""
        return self._add_matrix(other)

    def __sub__(self, other):
        """Subtract two matrices."""
        return self + (-1 * other)

    def __mul__(self, other):
        """Multiply two matrices or scalar by matrix."""
        if isinstance(other, Matrix):
            return self._matrix_mul_matrix(other)

        # if scalar multiplication
        return Matrix(tuple(
            [tuple(map(lambda x: x * other, line)) for line in self.tuples]))

    def __rmul__(self, other):
        """Define reverse multiplication as regular multiplication."""
        return self * other

    def __truediv__(self, other):
        """Divide matrix by scalar. Return floats if needed."""
        return self * (1.0 / other)

    def __eq__(self, other):
        """Compare two matrices. Return true if they are equal else false."""
        return self.tuples == other.tuples

    def __ne__(self, other):
        """The opposite of equal."""
        return not self == other

    def __iter__(self):
        """Enable to iterate on a matrix lines'."""
        return iter(self.tuples)

    def __hash__(self):
        """Enable to use a matrix as key of a dictionary."""
        return hash(self.tuples)
