"""Matrix data type class."""

import operator


class Matrix:
    """An immutable object representing a matrix data-type.

    Attributes:
        _matrix (tuple): contains the data about the matrix. Each line of
            the matrix is represented by a tuple.
    Note:
        This implementation only supports squared matrices (n * n).
    """

    def __init__(self, lines):
        self._validate(lines)
        self._matrix = lines

    def _validate(self, data: tuple):
        """Check if the data given is valid.

        Note:
            Valid data is defined if it contains tuples of the same length
            (Matrix only supports n * n), items can't be iterable.
        """
        if any(hasattr(item, '__len__') for line in data for item in line):
            raise TypeError("Matrix item type not supported")

        if not all([len(line) == len(data) for line in data]):
            raise ValueError("Matrix must be even-sided")

    @classmethod
    def unity(cls, dimension: int):
        """Generate a matrix with a main diagonal of 1's, elsewhere 0's."""
        return cls(
            tuple([tuple((0,) * i + (1,) + (0,) * (dimension - i - 1)) for i in
                   range(dimension)]))

    @classmethod
    def ones(cls, dimension):
        """Generate a matrix full of 1's."""
        return cls(tuple(([tuple((1,) * dimension) for _ in
                           range(dimension)])))

    def __repr__(self):
        return f'{self.__class__.__name__}{self._matrix}'

    def __str__(self):
        """Return a string presentation of the matrix instance."""
        return repr(self._matrix)

    @property
    def tuples(self):
        """Return the matrix instance as a tuple of tuples."""
        return self._matrix

    def _matrix_by_matrix(self, other, operation):
        """Calculate operation on two matrices.

        Args:
            operation (function): the function of the operator.
            other (Matrix): the other matrix to operate on.

        Returns:
            Matrix: the result of the operation.

        Note:
            Boolean operations supports un-squared matrices but
            mathematical operations don't.
        """
        if len(other.tuples) != len(self.tuples) and not any(
                [operation == operator.eq, operation == operator.ne]):
            raise ValueError("Matrices length don't match")

        calculated_matrix = []

        for i in range(len(self.tuples)):

            calculated_line = []
            for j in range(len(self.tuples)):
                calculated_line.append(
                    operation(self.tuples[i][j], other.tuples[i][j]))

            calculated_matrix.append(tuple(calculated_line))

        return Matrix(tuple(calculated_matrix))

    def _by_scalar(self, scalar, operation):
        """Calculate operation on matrix by scalar.

        Args:
            operation (function): the function of the operator.
            scalar (number): the scalar to operate by.

        Returns:
            Matrix: the result of the operation.

        Note:
            Scalar must be a number. Operations with scalars are only * and /.
        """
        calculated_matrix = []

        for i in range(len(self.tuples)):

            calculated_line = []
            for j in range(len(self.tuples)):
                calculated_line.append(operation(self.tuples[i][j], scalar))

            calculated_matrix.append(tuple(calculated_line))

        return Matrix(tuple(calculated_matrix))

    def __add__(self, other):
        """Add two matrices."""
        return self._matrix_by_matrix(other, operator.add)

    def __sub__(self, other):
        """Subtract two matrices."""
        return self + (-1 * other)

    def __mul__(self, other):
        """Multiply two matrices or scalar by matrix."""
        if isinstance(other, Matrix):
            return self._matrix_by_matrix(other, operator.mul)

        return self._by_scalar(other, operator.mul)

    def __rmul__(self, other):
        """Define to handle reverse multiplication (10 * matrix) as regular
        multiplication."""
        return self * other

    def __truediv__(self, other):
        """Divide matrix by scalar. Returns floats if
        needed."""
        return self * (1 / other)

    def _check_bool_matrix(self, matrix, operation):
        """Return true if all the items in the matrix are true else false."""
        func = {operator.eq: all, operator.ne: any}.get(operation)
        return func(
            [item for line_data in matrix.tuples for item in line_data])

    def __eq__(self, other):
        """Compare two matrices. Returns true if they are equal else false."""
        return self._check_bool_matrix(
            self._matrix_by_matrix(other, operator.eq), operator.eq)

    def __ne__(self, other):
        """Compare two matrices. Returns true if they are not equal else
        false."""
        return not self == other

    def __iter__(self):
        """Enable to iterate on a matrix lines'."""
        return iter(self.tuples)

    def __hash__(self):
        """Enable to use a matrix as key of a dictionary."""
        return hash(self.tuples)
