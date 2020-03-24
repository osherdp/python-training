import operator
from collections.abc import Iterable


class Matrix:
    """An immutable object representing a matrix data-type.

    Attributes:
        _matrix (tuple): contains the data about the matrix. Each line of
            the matrix is represented by a tuple.
    Note:
        This implementation only supports even-side matrices (n * n).
    """

    def __init__(self, *lines):
        self._validate(*lines)
        self._matrix = tuple(lines)

    def _validate(self, *data: tuple):
        """Check if the data given is valid.

        Note:
            Valid data is defined if it contains tuples of the same length
            (Matrix only supports n * n), items can't be iterable.
        """
        if not all(isinstance(line_data, tuple) for line_data in data):
            raise ValueError("Matrix lines must be tuple")

        if any(isinstance(item, Iterable) for line_data in data for item in
               line_data):
            raise ValueError("Matrix lines must be tuple")

        if not all([len(line) == len(data) for line in data]):
            raise ValueError("Matrix must be even-sided")

    @classmethod
    def unity(cls, dimension: int):
        """Generates a matrix with a main diagonal of 1's, everything else
        is 0's.
        """
        return cls(*[tuple((0,) * j + (1,) + (0,) * i) for j, i in enumerate(
            range(dimension - 1, -1, -1))])

    @classmethod
    def ones(cls, dimension):
        """Generates a matrix full of 1's."""
        return cls(*([tuple((1,) * dimension) for _ in range(dimension)]))

    def __repr__(self):
        return super(Matrix, self).__repr__()

    def __str__(self):
        """Returns a string presentation of the matrix instance."""
        return repr(self._matrix)

    @property
    def tuples(self):
        """Returns the matrix instance as a tuple of tuples."""
        return self._matrix

    def _by_matrix(self, operation, dimension_of_other,
                   self_item, other_item):
        """Calculates operation on two items.

        Args:
            operation (function): the function of the operator.
            dimension_of_other (int): the number of lines in the other matrix.
            self_item (number): current item from the current matrix instance.
            other_item (number): current item from the other matrix instance.

        Returns:
            number, the result of the operation.

        Note:
            Boolean operations supports different dimensions matrices but
            mathematical operations don't (except matrix division).
        """

        if dimension_of_other != len(self.tuples) and not any(
                [operation == operator.eq, operation == operator.ne]):
            raise ValueError("Matrices length don't match")

        if operation == operator.truediv:
            raise ValueError(f"{operation} not supported on "
                             f"{self.__class__.__name__}")

        return operation(self_item, other_item)

    def _by_scalar(self, operation, item, scalar):
        """Calculates operation on item by scalar.

        Args:
            operation (function): the function of the operator.
            item (number): current item from the current matrix instance.
            scalar (number): the scalar to operate by.

        Returns:
            number, the result of the operation.

        Note:
            Scalar must be a number. Operations with scalars are only * and /.
        """
        if is_number(scalar) and not any([operation == operator.mul,
                                          operation == operator.truediv]):
            raise ValueError(f'{operation} not supported on {type(scalar)}')

        return operation(item, scalar)

    def _calculate_matrix_operation(self, other, operation):
        """Does all the operations that can be done on a matrix.

        Args:
            other (Matrix or number): the other object to do the operation.
            operation (function): the function of the desired operator.

        Returns:
            If boolean operation, returns true if operation returned true
            else false. If mathematical operation, returns a new matrix with
            the calculated data.

        Note:
            Supported operations are addition, subtraction, multiplication and
            division(on matrix or by scalar). Also supports boolean
            operators == and !=.
        """
        calculated_matrix = []

        for i in range(len(self.tuples)):

            calculated_line = []
            for j in range(len(self.tuples)):
                try:
                    calculated_line.append(
                        self._by_matrix(operation, len(other.tuples),
                                        self.tuples[i][j], other.tuples[i][j]))
                except AttributeError:
                    calculated_line.append(
                        self._by_scalar(operation, self.tuples[i][j], other))

            calculated_matrix.append(tuple(calculated_line))

        return Matrix(*calculated_matrix)

    def __add__(self, other):
        """Adds two matrices."""
        return self._calculate_matrix_operation(other, operator.add)

    def __sub__(self, other):
        """Subtract two matrices."""
        return self._calculate_matrix_operation(other, operator.sub)

    def __mul__(self, other):
        """Multiply two matrices or scalar by matrix."""
        return self._calculate_matrix_operation(other, operator.mul)

    def __rmul__(self, other):
        """Defines to handle reverse multiplication (10 * matrix) as regular
        multiplication."""
        return self.__mul__(other)

    def __truediv__(self, other):
        """Divides two matrices or scalar by matrix. Returns floats if
        needed."""
        return self._calculate_matrix_operation(other, operator.truediv)

    def __floordiv__(self, other):
        """Defines to handle floor division (5 / 2 = 2) as regular
        division."""
        return self.__truediv__(other)

    def _check_bool_matrix(self, matrix, operation):
        """Returns true if all the items in the matrix are true else false."""
        func = {operator.eq: all, operator.ne: any}.get(operation)
        return func([item for line_data in matrix.tuples for item in line_data])

    def __eq__(self, other):
        """Compares two matrices. Returns true if they are equal else false."""
        return self._check_bool_matrix(self._calculate_matrix_operation(
            other, operator.eq), operator.eq)

    def __ne__(self, other):
        """Compares two matrices. Returns true if they are not equal else
        false."""
        return self._check_bool_matrix(self._calculate_matrix_operation(
            other, operator.ne), operator.ne)

    def __iter__(self):
        """Enables to iterate on a matrix lines'."""
        return iter(self.tuples)

    def __hash__(self):
        """Enables to use a matrix as key of a dictionary."""
        return hash(self.tuples)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
